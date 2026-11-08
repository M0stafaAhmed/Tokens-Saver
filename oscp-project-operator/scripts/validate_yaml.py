#!/usr/bin/env python3
"""Read-only Markdown frontmatter validator. Requires PyYAML; never installs it."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

try:
    import yaml
    from yaml.constructor import ConstructorError
except ImportError:
    yaml = None
    ConstructorError = Exception


if yaml is not None:
    class UniqueLoader(yaml.SafeLoader):
        def construct_mapping(self, node, deep=False):
            self.flatten_mapping(node)
            result = {}
            for key_node, value_node in node.value:
                key = self.construct_object(key_node, deep=deep)
                try:
                    duplicate = key in result
                except TypeError as exc:
                    raise ConstructorError("mapping", node.start_mark,
                                           "found unhashable key", key_node.start_mark) from exc
                if duplicate:
                    raise ConstructorError("mapping", node.start_mark,
                                           f"duplicate key {key!r}", key_node.start_mark)
                result[key] = self.construct_object(value_node, deep=deep)
            return result


def check_file(path: Path, root: Path) -> dict:
    relative = path.relative_to(root).as_posix()
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeError) as exc:
        return {"path": relative, "status": "error", "issues": [str(exc)]}

    if not lines or lines[0].strip() != "---":
        return {"path": relative, "status": "missing_frontmatter",
                "issues": ["No opening frontmatter delimiter"]}
    end = next((i for i in range(1, len(lines)) if lines[i].strip() in ("---", "...")), None)
    if end is None:
        return {"path": relative, "status": "invalid", "issues": ["Unclosed frontmatter"]}

    raw = "\n".join(lines[1:end])
    issues = []
    if "\u00a0" in raw:
        issues.append(f"{raw.count(chr(160))} non-breaking spaces")
    if yaml is None:
        return {"path": relative, "status": "not_checked",
                "issues": issues + ["PyYAML unavailable; YAML not parsed"]}
    try:
        data = yaml.load(raw, Loader=UniqueLoader)
    except yaml.YAMLError as exc:
        return {"path": relative, "status": "invalid", "issues": issues + [str(exc).splitlines()[0]]}

    if data is None:
        data = {}
    if not isinstance(data, dict):
        return {"path": relative, "status": "invalid",
                "issues": issues + ["Frontmatter must be a mapping"]}

    if "type" in data and (not isinstance(data["type"], str) or
                           not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", data["type"])):
        issues.append("type should be lowercase kebab-case")

    if "updated" in data:
        updated = data["updated"]
        if not isinstance(updated, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", updated):
            issues.append("updated should be a quoted YYYY-MM-DD string")
        else:
            try:
                dt.date.fromisoformat(updated)
            except ValueError:
                issues.append("updated is not a real calendar date")

    if "tags" in data and not isinstance(data["tags"], (list, str)):
        issues.append("tags should be a list or string")
    if "related_machines" in data and not isinstance(data["related_machines"], list):
        issues.append("related_machines should be a list")

    return {"path": relative, "status": "review" if issues else "valid",
            "properties": sorted(str(key) for key in data), "issues": issues}


def ensure_output_outside(root: Path, output: Path) -> None:
    output = output.resolve(strict=False)
    try:
        output.relative_to(root.resolve())
    except ValueError:
        return
    raise ValueError(f"report output must be outside the source vault: {output}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Vault directory (read-only)")
    parser.add_argument("--json-out", type=Path, help="Optional JSON report destination")
    args = parser.parse_args()
    if yaml is None:
        print("PyYAML unavailable; no dependency installed", file=sys.stderr)

    try:
        root = args.root.resolve(strict=True)
        if not root.is_dir():
            raise NotADirectoryError(root)
        if args.json_out is not None:
            ensure_output_outside(root, args.json_out)
        files = [p for p in sorted(root.rglob("*.md")) if p.is_file() and not p.is_symlink()]
        rows = [check_file(path, root) for path in files]
        result = {
            "files_checked": len(rows),
            "valid": sum(item["status"] == "valid" for item in rows),
            "review": sum(item["status"] == "review" for item in rows),
            "invalid": sum(item["status"] == "invalid" for item in rows),
            "missing_frontmatter": sum(item["status"] == "missing_frontmatter" for item in rows),
            "not_checked": sum(item["status"] == "not_checked" for item in rows),
            "errors": sum(item["status"] == "error" for item in rows),
            "files": rows,
        }
        payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
        if args.json_out:
            args.json_out.parent.mkdir(parents=True, exist_ok=True)
            args.json_out.write_text(payload, encoding="utf-8")
            print(json.dumps({key: value for key, value in result.items() if key != "files"}))
        else:
            sys.stdout.write(payload)
        if yaml is None:
            return 2
        return 1 if result["invalid"] or result["missing_frontmatter"] or result["errors"] else 0
    except (OSError, ValueError) as exc:
        print(f"validation error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
