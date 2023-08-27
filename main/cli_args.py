
from argparse import ArgumentParser


# TODO: add program arguments in parser
class CliArgs:
    parser: ArgumentParser
    def __init__(self):
        self.parser = ArgumentParser()

    def parse(self):
        self.parser.parse_args()