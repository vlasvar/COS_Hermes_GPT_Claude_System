import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / "schema/sheets.json").read_text(encoding="utf-8"))

    def test_core_tabs_are_unique(self):
        names = [tab["name"] for tab in self.schema["tabs"]]
        self.assertEqual(len(names), len(set(names)))

    def test_every_tab_has_a_stable_key(self):
        for tab in self.schema["tabs"]:
            with self.subTest(tab=tab["name"]):
                self.assertTrue(tab["key"].endswith("ID"))
                self.assertIn(tab["key"], tab["columns"])

    def test_every_agent_has_adapter_and_setup(self):
        expected = {
            "hermes": "HERMES.md",
            "chatgpt": "PROJECT_INSTRUCTIONS.md",
            "claude": "CLAUDE.md",
        }
        for adapter, instruction_file in expected.items():
            with self.subTest(adapter=adapter):
                folder = ROOT / "adapters" / adapter
                self.assertTrue((folder / "README.md").is_file())
                self.assertTrue((folder / instruction_file).is_file())

    def test_google_sheets_provisioner_matches_schema(self):
        script = (ROOT / "templates/google-sheets/Code.gs").read_text(encoding="utf-8")
        self.assertIn("@OnlyCurrentDoc", script)
        self.assertNotIn(".clear()", script)
        for tab in self.schema["tabs"]:
            with self.subTest(tab=tab["name"]):
                self.assertIn(f"name: '{tab['name']}'", script)
                for column in tab["columns"]:
                    self.assertIn(f"'{column}'", script)

    def test_public_tree_has_no_private_instance_directory(self):
        self.assertFalse((ROOT / "private").exists())
        self.assertFalse((ROOT / "instance").exists())

    def test_instance_generator_creates_each_adapter_bundle(self):
        expected_instruction = {
            "hermes": "AGENTS.md",
            "chatgpt": "PROJECT_INSTRUCTIONS.md",
            "claude": "CLAUDE.md",
        }
        with tempfile.TemporaryDirectory() as temporary_root:
            for adapter, instruction_file in expected_instruction.items():
                with self.subTest(adapter=adapter):
                    target = Path(temporary_root) / adapter
                    result = subprocess.run(
                        [
                            sys.executable,
                            str(ROOT / "scripts/create_instance.py"),
                            str(target),
                            "--adapter",
                            adapter,
                        ],
                        capture_output=True,
                        text=True,
                        check=False,
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertTrue((target / instruction_file).is_file())
                    self.assertTrue((target / "USER_PROFILE.md").is_file())
                    self.assertTrue((target / "system.yaml").is_file())
                    for kernel_file in ("SYSTEM.md", "CONTEXT.md", "PERMISSIONS.md", "WORKFLOWS.md"):
                        self.assertTrue((target / kernel_file).is_file())

    def test_instance_generator_rejects_target_inside_repository(self):
        target = ROOT / "instance-generator-must-reject"
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/create_instance.py"),
                str(target),
                "--adapter",
                "hermes",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
