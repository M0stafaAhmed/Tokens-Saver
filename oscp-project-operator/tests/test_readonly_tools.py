import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
SCRIPTS = BASE / "scripts"
class ReadOnlyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "vault"
        self.root.mkdir()
    def tearDown(self):
        self.tmp.cleanup()
    def run_script(self, name, *args):
        return subprocess.run([sys.executable, str(SCRIPTS / name), *map(str, args)], capture_output=True, text=True)
    def test_inventory_counts_and_writes_reports(self):
        (self.root / "sub").mkdir()
        (self.root / "a.md").write_text("# A")
        (self.root / "sub" / "empty.txt").write_text("")
        json_out = Path(self.tmp.name) / "report.json"
        csv_out = Path(self.tmp.name) / "report.csv"
        result = self.run_script("inventory.py", self.root, "--json-out", json_out, "--csv-out", csv_out)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(json_out.read_text())
        self.assertEqual(data["file_count"], 2)
        self.assertEqual(data["directory_count"], 1)
        self.assertEqual(data["files"][1]["empty"], True)
        self.assertTrue(csv_out.exists())
    def test_inventory_rejects_report_inside_vault(self):
        result = self.run_script("inventory.py", self.root, "--json-out", self.root / "overwrite.md")
        self.assertEqual(result.returncode, 2)
        self.assertFalse((self.root / "overwrite.md").exists())
    def test_yaml_duplicate_bad_date_and_read_only(self):
        try:
            import yaml
        except ImportError:
            self.skipTest("PyYAML unavailable")
        (self.root / "ok.md").write_text('---\ntype: reusable-poc\nupdated: "2026-11-06"\n---\n# ok')
        (self.root / "duplicate.md").write_text("---\ntype: a\ntype: b\n---\n")
        (self.root / "bad-date.md").write_text('---\nupdated: "2026-99-99"\n---\n')
        (self.root / "missing.md").write_text("# no frontmatter\n")
        before = {path.name: path.read_bytes() for path in self.root.glob("*.md")}
        output = Path(self.tmp.name) / "yaml.json"
        result = self.run_script("validate_yaml.py", self.root, "--json-out", output)
        self.assertEqual(result.returncode, 1, result.stderr)
        rows = {Path(item["path"]).name: item for item in json.loads(output.read_text())["files"]}
        self.assertEqual(rows["ok.md"]["status"], "valid")
        self.assertEqual(rows["duplicate.md"]["status"], "invalid")
        self.assertIn("real calendar date", " ".join(rows["bad-date.md"]["issues"]))
        self.assertEqual(rows["missing.md"]["status"], "missing_frontmatter")
        self.assertEqual(before, {path.name: path.read_bytes() for path in self.root.glob("*.md")})
    def test_validators_reject_report_paths_inside_vault(self):
        note = self.root / "note.md"
        note.write_text("# keep")
        before = note.read_bytes()
        yaml_result = self.run_script("validate_yaml.py", self.root, "--json-out", note)
        link_result = self.run_script("audit_links.py", self.root, "--json-out", note)
        self.assertEqual(yaml_result.returncode, 2)
        self.assertEqual(link_result.returncode, 2)
        self.assertEqual(note.read_bytes(), before)
    def test_links_assets_alias_ambiguity_broken_relative_and_code(self):
        for folder in ("A", "B"):
            (self.root / folder).mkdir()
        (self.root / "A" / "user.md").write_text("# A")
        (self.root / "B" / "user.md").write_text("# B")
        (self.root / "A" / "Home.md").write_text("# Home")
        (self.root / "A" / "image.png").write_bytes(b"fake-image")
        (self.root / "A" / "sub").mkdir()
        (self.root / "A" / "sub" / "source.md").write_text("[[../Home]]")
        fence = chr(96) * 3
        (self.root / "index.md").write_text("[[user]] [[Missing]] [[A/image.png|screenshot]] [[A/not-user]]\n[relative](A/Home.md)\n" + fence + "\n[[Fake]]\n" + fence)
        output = Path(self.tmp.name) / "links.json"
        result = self.run_script("audit_links.py", self.root, "--json-out", output)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(output.read_text())
        statuses = [item["status"] for item in data["links"]]
        self.assertIn("ambiguous", statuses)
        self.assertIn("broken", statuses)
        asset = next(item for item in data["links"] if item["target"] == "A/image.png")
        self.assertEqual(asset["status"], "resolved")
        qualified = next(item for item in data["links"] if item["target"] == "A/not-user")
        self.assertEqual(qualified["status"], "broken")
        self.assertFalse(any(item["target"] == "Fake" for item in data["links"]))
        relative_wiki = next(item for item in data["links"] if item["source"].endswith("source.md"))
        self.assertEqual(relative_wiki["status"], "resolved")
        relative_md = next(item for item in data["links"] if item["kind"] == "markdown")
        self.assertEqual(relative_md["status"], "resolved")
if __name__ == "__main__":
    unittest.main(verbosity=2)
