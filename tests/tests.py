# imports don't work when file executed directly
if __name__ == '__main__':
    print("Please execute tests as a module \nUsage: python -m unittest tests/tests.py")
    exit()

import pathlib
import unittest
from main.cli import SetupDevCli
from main.config import ConfigList


class SetupDevCliTests(unittest.TestCase):
    def test_init_passing_configs(self):
        expected_configs = ConfigList()
        cli = SetupDevCli(expected_configs)
        self.assertEqual(cli.configs, expected_configs)
