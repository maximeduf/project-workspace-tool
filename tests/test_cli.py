from main.cli import *
from main.cli_args import CliArgs
from main.config import AliasConfig, ConfigList, Config, ConfigType, VarConfig
from unittest.mock import patch


class TestMain:
    def test_main_exists(self):
        main()

    @patch.object(Cli, "start")
    def test_main_makes_cli(self, mock):
        main()
        assert mock.called


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

        cli = Cli([
            AliasConfig(
                description=expected_description, alias=expected_alias)
        ])
        assert cli.configs[0].type == ConfigType.ALIAS

    def test_init_with_many_configs(self):
        configs = ConfigList()
        for i in range(10):
            configs.append(VarConfig(f"desc {i}", f"line {i}"))

        cli = Cli(configs)
        for i in range(len(configs)):
            assert cli.configs[i].description == f"desc {i}"
            assert cli.configs[i].line == f"line {i}"
