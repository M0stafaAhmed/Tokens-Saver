#!/usr/bin/env python3
"""Read-only, bounded inspection of project documents. No external dependencies."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path

HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$")
DOC_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".toml", ".txt"}
SKIP_DIRS = {".git", "__pycache__", "backups", "reference", ".venv"}
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_LIMIT = 500


def positive_limit(value: str) -> int:
    number = int(value)
    if not 1 <= number <= MAX_LIMIT:
        raise argparse.ArgumentTypeError(f"limit must be between 1 and {MAX_LIMIT}")
    return number


def safe_document(value: str) -> Path:
    source = Path(value).expanduser()
    if source.is_symlink() or not source.is_file():
        raise ValueError(f"missing, non-regular, or symlink input: {source}")
    if source.stat().st_size > MAX_FILE_BYTES:
        raise ValueError(f"input exceeds {MAX_FILE_BYTES} byte inspection limit: {source}")
    return source


def read_lines(value: str) -> list[str]:
    source = safe_document(value)
    return source.read_text(encoding="utf-8").splitlines()


def headings(lines: list[str]) -> list[tuple[int, int, str]]:
    found = []
    for position, line in enumerate(lines, start=1):
        match = HEADING.match(line)
        if match:
            found.append((position, len(match.group(1)), line))
    return found


def outline(value: str, limit: int) -> None:
    entries = headings(read_lines(value))
    for line_no, _, heading in entries[:limit]:
        print(f"{line_no}: {heading}")
    if len(entries) > limit:
        print(f"[TRUNCATED: {len(entries) - limit} more headings]")


def section(value: str, heading: str, limit: int) -> None:
    lines = read_lines(value)
    entries = headings(lines)
    matching = [(line, level) for line, level, label in entries if label.strip() == heading.strip()]
    if not matching:
        raise ValueError(f"heading not found: {heading!r}")
    if len(matching) != 1:
        raise ValueError(f"ambiguous heading ({len(matching)} matches): {heading!r}")
    start, depth = matching[0]
    stop = len(lines) + 1
    for line_no, level, _ in entries:
        if line_no > start and level <= depth:
            stop = line_no
            break
    selected = lines[start - 1:stop - 1]
    for offset, line in enumerate(selected[:limit]):
        print(f"{start + offset}: {line}")
    if len(selected) > limit:
        print(f"[TRUNCATED: {len(selected) - limit} more section lines]")


def fingerprint(values: list[str]) -> None:
    for value in values:
        source = safe_document(value)
        digest = hashlib.sha256()
        with source.open("rb") as stream:
            for chunk in iter(lambda: stream.read(65536), b""):
                digest.update(chunk)
        print(f"{digest.hexdigest()}  {source}  ({source.stat().st_size} bytes)")


def inventory(value: str, limit: int) -> None:
    root = Path(value).expanduser()
    if root.is_symlink() or not root.is_dir():
        raise ValueError(f"missing, non-directory, or symlink root: {root}")
    found = []
    total_seen = 0
    for dirname, dirnames, filenames in os.walk(root, followlinks=False):
        here = Path(dirname)
        depth = len(here.relative_to(root).parts)
        dirnames[:] = sorted(
            entry for entry in dirnames
            if entry not in SKIP_DIRS and not (here / entry).is_symlink()
        ) if depth < 2 else []
        for filename in sorted(filenames):
            candidate = here / filename
            if candidate.suffix.lower() not in DOC_SUFFIXES or candidate.is_symlink():
                continue
            if not candidate.is_file():
                continue
            total_seen += 1
            if len(found) < limit:
                found.append((candidate.relative_to(root).as_posix(), candidate.stat().st_size))
            if total_seen > limit:
                break
        if total_seen > limit:
            break
    for name, size in found:
        print(f"{name}\t{size} bytes")
    if total_seen > limit:
        print("[TRUNCATED: additional documents omitted]")
    else:
        print(f"[TOTAL: {total_seen} documents; depth <= 2; backups/reference excluded]")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    p_inventory = commands.add_parser("inventory", help="limited document list")
    p_inventory.add_argument("root")
    p_inventory.add_argument("--limit", type=positive_limit, default=40)
    p_outline = commands.add_parser("outline", help="Markdown headings and line numbers")
    p_outline.add_argument("file")
    p_outline.add_argument("--limit", type=positive_limit, default=80)
    p_section = commands.add_parser("section", help="one exact Markdown section")
    p_section.add_argument("file")
    p_section.add_argument("heading", help="exact heading, including # prefix")
    p_section.add_argument("--limit", type=positive_limit, default=100)
    p_fingerprint = commands.add_parser("fingerprint", help="SHA-256 and size")
    p_fingerprint.add_argument("files", nargs="+")
    args = parser.parse_args(argv)
    try:
        if args.command == "inventory":
            inventory(args.root, args.limit)
        elif args.command == "outline":
            outline(args.file, args.limit)
        elif args.command == "section":
            section(args.file, args.heading, args.limit)
        elif args.command == "fingerprint":
            fingerprint(args.files)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"doc_probe: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
