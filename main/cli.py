from main.cli_args import CliArgs
from main.config import ConfigList


def main():
    cli = Cli()
    cli.start()


class Cli:
    cli_args: CliArgs
    configs: ConfigList

    def __init__(self, config_list: ConfigList = []):
        print("cli init")
        self.cli_args = CliArgs()
        self.configs = ConfigList(config_list)

    def start(self):
        pass
