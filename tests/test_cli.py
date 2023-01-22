# imports don't work when file executed directly
if __name__ == '__main__':
    print("Please execute tests as a module \nUsage: python -m unittest tests/tests.py")
    exit()

from main.cli import SetupDevCli
from main.config import ConfigList


def test_init_passing_configs():
    expected_configs = ConfigList()
    cli = SetupDevCli(expected_configs)
    assert cli.configs == expected_configs
