from main.args import CliArgs, ParsedArgs
from main.config import AliasConfig, ConfigList, FunctionConfig, VarConfig


class SetupDevCli:
    cli_args: CliArgs
    configs: ConfigList


    def __init__(self, configs: ConfigList = None):
        self.cli_args = CliArgs()
        if configs is not None:
            self.configs = configs
        else:
            self.configs = ConfigList([
            AliasConfig("cd to code", "alias cdc='cd ~/c'"),
            AliasConfig("list all", "alias ll='ls -al'"),
            FunctionConfig(
                "function to do some funky stuff",
                "function do-some-funky() {",
                "    echo 'hello from function do-some-funky'",
                "}"
            ),
            VarConfig("an important environment variable",
                      "export somevar='some value'")
        ])

    def start(self):
        parsed: ParsedArgs = self.cli_args.parse()
        print(parsed.file)
        print(self.configs)


def main():
    cli = SetupDevCli()
    cli.start()


if __name__ == '__main__':
    main()
