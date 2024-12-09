import unittest
from unittest.mock import patch
from click.testing import CliRunner
from multi_repo_workspace.cli import cli, main


class TestMain(unittest.TestCase):
    @patch('multi_repo_workspace.cli.cli')
    def test_main_calls_cli(self, mock_cli):
        main()
        mock_cli.assert_called_once()


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_default_command(self):
        result = self.runner.invoke(cli)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Welcome to Multi-Repo Workspace (MRW)!", result.output)

    def test_create_command(self):
        result = self.runner.invoke(
            cli, ['create', 'name-workspace', '-d', 'path/to/workspace'])
        self.assertIn("Hello! inside the create use case", result.output)
