from abc import ABC, abstractmethod
from typing import TypeVar, Generic

import click

# represent parameters needed for a command
Params = TypeVar('Params')
# represent return type of a command
Returns = TypeVar('Returns')


class Command(ABC, Generic[Params, Returns]):

    @classmethod
    @abstractmethod
    def __call__(self) -> Returns:
        click.echo("This command has not been implemented yet.")
        raise NotImplementedError
