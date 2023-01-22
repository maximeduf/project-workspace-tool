from argparse import ArgumentParser, Namespace
from pathlib import Path
from dataclasses import dataclass


@dataclass
class ParsedArgs:
    all: Namespace
    file: Path


class CliArgs:
    PROGRAM_NAME = "cli"
    PROGRAM_DESC = "Tools to setup a linux dev environment."
    parsed_args: ParsedArgs

    # top level parser
    cli_parser = ArgumentParser(
        prog=PROGRAM_NAME,
        description=PROGRAM_DESC
    )
    subparsers = cli_parser.add_subparsers(
        help='The configuration includes aliases, functions and environment variables, to the file that makes sense to you.'
    )

    def __init__(self):
        self._setup_arguments()

    def parse(self) -> Path:
        arg_namespace = self.cli_parser.parse_args()
        self.parsed_args = ParsedArgs(
            all=arg_namespace, file=arg_namespace.file)
        return self.parsed_args

    def _setup_arguments(self) -> None:
        config_parser: ArgumentParser = self.subparsers.add_parser(
            'config', help="help for configuration"
        )
        config_parser.add_argument(
            '-f', '--file', help='path of the file to add environment configuration', type=Path, default=Path('')
        )
