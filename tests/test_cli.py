from main.cli import *
from main.args import CliArgs
from main.config import ConfigList
import pytest

class TestMain:
    def test_main_exists(self):
        main()

class TestCli:
    def test_init_default(self):
        cli = Cli()
        assert cli is not None

    def test_init_default_has_cli_args(self):
        cli = Cli()
        assert cli.cli_args is not None
        assert type(cli.cli_args) is CliArgs

    def test_init_default_has_configs(self):
        cli = Cli()
        assert cli.configs is not None
        assert type(cli.configs) is ConfigList

    def test_cli_args_type(self, monkeypatch):
        cli = Cli()
        monkeypatch.setattr(cli, "cli_args", ["one", "two"])
        assert cli.cli_args == ["one", "two"]
