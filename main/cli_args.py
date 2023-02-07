
from argparse import ArgumentParser


class CliArgs:
    parser: ArgumentParser
    def __init__(self):
        self.parser = ArgumentParser()

    def parse(self):
        self.parser.parse_args()