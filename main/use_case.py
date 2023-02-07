

from abc import ABC, abstractmethod, abstractclassmethod
from typing import TypeVar, Generic

# represent parameters needed for a use case
Params = TypeVar('Params')
# represent return type of a use case
Returns = TypeVar('Returns')
class UseCase(ABC, Generic[Params, Returns]):
    
    def __init__(self, params: Params):
        self.params = params
    
    @abstractclassmethod
    def __call__(self) -> Returns:
        pass
