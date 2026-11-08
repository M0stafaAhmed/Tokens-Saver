#!/usr/bin/env python3
"""Read-only filename-based Obsidian wikilink and Markdown-link audit."""
from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

WIKILINK_RE = re.compile(r"!? \[\[([^\]]+)\]\]".replace(" ", ""))
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCED_CODE_RE = re.compile(r"(?ms)^\s*(\x60{3,}|~{3,}).*?^\s*\1\s*$")
INLINE_CODE_RE = re.compile(r"(\x60+).*?\1", re.DOTALL)


def strip_code(text: str) -> str:
    return INLINE_CODE_RE.sub("", FENCED_CODE_RE.sub("", text))


def all_files(root: Path) -> list[Path]:
    return [path for path in root.rglob("*") if path.is_file() and not path.is_symlink()]


def make_indexes(root: Path, files: list[Path]):
    exact = {}
    by_name = {}
    for path in files:
        relative = path.relative_to(root).as_posix()
        exact[relative.casefold()] = relative
        by_name.setdefault(path.name.casefold(), []).append(relative)
        if path.suffix.casefold() == ".md":
            exact[relative[:-3].casefold()] = relative
            by_name.setdefault(path.stem.casefold(), []).append(relative)
    return exact, by_name


def resolve_wikilink(target: str, source: Path, root: Path, exact: dict, by_name: dict):
    clean = target.strip().replace("\\", "/")
    if clean.startswith("#"):
        return "same_note_anchor", [source.relative_to(root).as_posix()]
    clean = unquote(clean.split("#", 1)[0]).lstrip("/")
    if not clean:
        return "same_note_anchor", [source.relative_to(root).as_posix()]

    candidates = [clean]
    if not Path(clean).suffix:
        candidates.append(clean + ".md")

    if "/" in clean:
        parent = source.relative_to(root).parent.as_posix()
        candidates.extend(posixpath.join(parent, item) for item in list(candidates))
        found = sorted({exact[posixpath.normpath(item).casefold()]
                        for item in candidates
                        if posixpath.normpath(item).casefold() in exact})
    else:
        found = []
        for item in candidates:
            key = posixpath.normpath(item).casefold()
            if key in exact:
                found.append(exact[key])
        if not found:
            found = sorted(set(by_name.get(Path(clean).name.casefold(), []) +
                               by_name.get(Path(clean).stem.casefold(), [])))
        else:
            found = sorted(set(found))

    if len(found) == 1:
        return "resolved", found
    if len(found) > 1:
        return "ambiguous", found
    return "broken", []


def resolve_markdown_link(target: str, source: Path, root: Path):
    raw = target.strip()
    if not raw:
        return "empty", []
    raw = raw.split('"', 1)[0].split("'", 1)[0].strip().strip("<>")
    parsed = urlsplit(raw)
    if parsed.scheme or parsed.netloc or raw.startswith("//"):
        return "external", []
    if not parsed.path:
        return "same_note_anchor", [source.relative_to(root).as_posix()]

    candidate = (source.parent / unquote(parsed.path)).resolve(strict=False)
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return "outside_vault", []
    if candidate.is_file():
        return "resolved", [candidate.relative_to(root).as_posix()]
    if not candidate.suffix:
        markdown_candidate = candidate.with_suffix(".md")
        if markdown_candidate.is_file():
            return "resolved", [markdown_candidate.relative_to(root).as_posix()]
    return "broken", []


def audit(root: Path) -> dict:
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise NotADirectoryError(root)
    files = all_files(root)
    markdown_files = [path for path in files if path.suffix.casefold() == ".md"]
    exact, by_name = make_indexes(root, files)
    records = []

    for source in markdown_files:
        text = strip_code(source.read_text(encoding="utf-8-sig"))
        source_relative = source.relative_to(root).as_posix()
        for match in WIKILINK_RE.finditer(text):
            raw = match.group(1).strip()
            target, _, alias = raw.partition("|")
            status, candidates = resolve_wikilink(target.strip(), source, root, exact, by_name)
            records.append({
                "source": source_relative, "kind": "wikilink", "target": target.strip(),
                "alias": alias.strip() or None, "status": status, "candidates": candidates,
            })
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip()
            status, candidates = resolve_markdown_link(target, source, root)
            records.append({
                "source": source_relative, "kind": "markdown", "target": target,
                "alias": None, "status": status, "candidates": candidates,
            })

    counts = {}
    for item in records:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    return {
        "root": str(root),
        "documents_scanned": len(markdown_files),
        "files_indexed": len(files),
        "link_count": len(records),
        "status_counts": dict(sorted(counts.items())),
        "links": records,
        "limitations": [
            "Read-only; no links are changed.",
            "Filename-based resolver; duplicate basenames are reported as ambiguous.",
            "Does not fully emulate Obsidian aliases, resolver settings, heading existence, block references, or every Markdown syntax variant.",
            "Links inside fenced and inline code are excluded.",
        ],
    }


def ensure_output_outside(root: Path, output: Path) -> None:
    output = output.resolve(strict=False)
    try:
        output.relative_to(root.resolve())
    except ValueError:
        return
    raise ValueError(f"report output must be outside the source vault: {output}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Vault directory to audit (read-only)")
    parser.add_argument("--json-out", type=Path, help="Optional JSON report destination")
    args = parser.parse_args()
    try:
        result = audit(args.root)
        if args.json_out is not None:
            ensure_output_outside(Path(result["root"]), args.json_out)
        payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
        if args.json_out:
            args.json_out.parent.mkdir(parents=True, exist_ok=True)
            args.json_out.write_text(payload, encoding="utf-8")
            print(json.dumps({key: value for key, value in result.items() if key != "links"}))
        else:
            sys.stdout.write(payload)
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"link audit error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
