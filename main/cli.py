
from main.args import CliArgs
from main.config import ConfigList

def main():
    pass

class Cli:
    cli_args: CliArgs
    configs: ConfigList
    
    def __init__(self, config_list: ConfigList = []):
        self.cli_args = CliArgs()
        self.configs = ConfigList(config_list)
