from main.cli import *
from main.args import CliArgs
from main.config import AliasConfig, ConfigList, Config, ConfigType
import pytest

class TestMain:
    def test_main_exists(self):
        main()

class TestCli:
    def test_init_default(self):
        cli = Cli()
        assert cli != None

    def test_init_default_has_cli_args(self):
        cli = Cli()
        assert cli.cli_args != None
        assert type(cli.cli_args) == CliArgs

    def test_init_default_has_configs(self):
        cli = Cli()
        assert cli.configs != None
        assert type(cli.configs) == ConfigList

    def test_init_with_config(self):
        expected_description = "An alias description"
        expected_alias = "alias cdc = cd ~/c"

        cli = Cli(config_list=[AliasConfig(description=expected_description, alias=expected_alias)])
        assert cli.configs.configs[0] == ConfigType.ALIAS
        