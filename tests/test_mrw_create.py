import unittest
from unittest.mock import patch
from click.testing import CliRunner
from multi_repo_workspace.commands.mrw_create import (
    MrwCreate,
    MrwArguments
)
from pathlib import Path


class TestMrwCreate(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @patch('click.prompt')
    @patch('click.confirm')
    def test_create_workspace_with_prompts(self, mock_confirm, mock_prompt):
        mock_prompt.side_effect = ['test_workspace']
        mock_confirm.side_effect = [True]

        params = MrwArguments(workspace_name='', workspace_path=Path(''))
        use_case = MrwCreate(params)

        result = self.runner.invoke(use_case)

        self.assertIn("Hello! inside the create use case", result.output)
        self.assertIn("name confirmed!", result.output)
        mock_prompt.assert_called_once_with("Enter workspace name", type=str)
        mock_confirm.assert_called_once_with(
            "Are you sure you want to use 'test_workspace' as workspace name?",
            abort=False
        )


if __name__ == '__main__':
    unittest.main()
