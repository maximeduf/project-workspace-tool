from argparse import ArgumentParser
from main.cli_args import CliArgs
from unittest.mock import patch


class TestCliArgs:
    def test_init_default(self):
        args = CliArgs()
        assert args != None

    def test_init_has_arg_parser(self):
        args = CliArgs()
        assert args.parser != None
        assert isinstance(args.parser, ArgumentParser)

    @patch.object(ArgumentParser, "parse_args")
    def test_parse(self, mock):
        args = CliArgs()
        args.parse()
        assert mock.called
    # -v-- ArgumentParser's program name
    #      ---v-- subparser (use case group)
    #             ---v--- subparser's subparser (use case)
    # ldst config inspect
    # ldst config apply
    # ldst config list
    # ldst app inspect
    # ldst app apply
    # ldst app list
