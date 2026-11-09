"""Synthetic tests for the read-only document probe."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "doc_probe.py"
SAMPLE = "# Decisions\nintro\n## Approved\none\n### Detail\ntwo\n## Pending\nthree\n"


class DocumentProbeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.file = self.root / "decisions.md"
        self.file.write_text(SAMPLE, encoding="utf-8")
        (self.root / "architecture-proposal.md").write_text("# Proposal\n", encoding="utf-8")
        (self.root / "secret.bin").write_text("not included\n", encoding="utf-8")
        (self.root / "backups").mkdir()
        (self.root / "backups" / "old.md").write_text("# Old\n", encoding="utf-8")

    def run_probe(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, args)],
            capture_output=True, text=True, check=False,
        )

    def test_outline(self) -> None:
        result = self.run_probe("outline", self.file)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1: # Decisions", result.stdout)
        self.assertIn("3: ## Approved", result.stdout)
        self.assertIn("5: ### Detail", result.stdout)
        self.assertIn("7: ## Pending", result.stdout)

    def test_section_stops_at_peer(self) -> None:
        result = self.run_probe("section", self.file, "## Approved")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("4: one", result.stdout)
        self.assertIn("6: two", result.stdout)
        self.assertNotIn("## Pending", result.stdout)

    def test_section_is_bounded(self) -> None:
        result = self.run_probe("section", self.file, "## Approved", "--limit", "2")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("[TRUNCATED:", result.stdout)
        self.assertNotIn("6: two", result.stdout)

    def test_missing_or_ambiguous_heading(self) -> None:
        self.assertEqual(self.run_probe("section", self.file, "## Missing").returncode, 2)
        self.file.write_text(SAMPLE + "## Approved\nextra\n", encoding="utf-8")
        result = self.run_probe("section", self.file, "## Approved")
        self.assertEqual(result.returncode, 2)
        self.assertIn("ambiguous", result.stderr)

    def test_inventory_skips_reference_and_binary(self) -> None:
        result = self.run_probe("inventory", self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("decisions.md", result.stdout)
        self.assertIn("architecture-proposal.md", result.stdout)
        self.assertNotIn("old.md", result.stdout)
        self.assertNotIn("secret.bin", result.stdout)

    def test_fingerprint(self) -> None:
        result = self.run_probe("fingerprint", self.file)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(hashlib.sha256(SAMPLE.encode()).hexdigest(), result.stdout)

    def test_nonexistent_and_invalid_limit(self) -> None:
        self.assertEqual(self.run_probe("outline", self.root / "absent.md").returncode, 2)
        self.assertNotEqual(self.run_probe("outline", self.file, "--limit", "0").returncode, 0)

    def test_no_writes_and_symlink_refusal(self) -> None:
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        for name in ("inventory", "outline", "section", "fingerprint"):
            args = (self.root,) if name == "inventory" else (
                (self.file, "## Approved") if name == "section" else (self.file,)
            )
            self.assertEqual(self.run_probe(name, *args).returncode, 0)
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        try:
            link = self.root / "linked.md"
            link.symlink_to(self.file)
        except (OSError, NotImplementedError):
            return
        self.assertEqual(self.run_probe("outline", link).returncode, 2)


if __name__ == "__main__":
    unittest.main()
