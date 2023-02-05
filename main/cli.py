
from main.cli_args import CliArgs
from main.config import ConfigList

def main():
    cli = Cli()
    cli.parse_args()


class Cli:
    cli_args: CliArgs
    configs: ConfigList
    
    def __init__(self, config_list: ConfigList = []):
        self.cli_args = CliArgs()
        self.configs = ConfigList(config_list)

    def parse_args(self):
        pass