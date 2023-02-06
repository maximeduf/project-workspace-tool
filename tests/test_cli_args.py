from main.cli_args import CliArgs


class TestCliArgs:
    def test_init_default(self):
        args = CliArgs
        assert args != None
