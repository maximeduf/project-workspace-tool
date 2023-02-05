from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List


class ConfigType(Enum):
    FUNCTION = "Function"
    ENV_VAR = "Variable"
    ALIAS = "Alias"


class Config(ABC):
    FSTRING = "# {}\n{}\n\n"
    type: ConfigType
    description: str

    def __init__(self, description: str, type: ConfigType):
        self.description = description
        self.type = type

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError


class AliasConfig(Config):
    line: str

    def __init__(self, description: str = '', alias: str = ''):
        super().__init__(description, ConfigType.ALIAS)
        self.line = alias

    def __str__(self) -> str:
        return self.FSTRING.format(self.description, self.line)


class FunctionConfig(Config):
    lines: List[str]

    def __init__(self, description: str = '', lines: List[str] = []):
        super().__init__(description, ConfigType.FUNCTION)
        self.lines = lines

    def __str__(self) -> str:
        function_string: str = ""
        for line in self.lines:
            function_string += line

        return self.FSTRING.format(self.description, "\n".join(self.lines))


class VarConfig(Config):
    line: str

    def __init__(self, description: str = '', line: str = ''):
        super().__init__(description, ConfigType.ENV_VAR)
        self.line = line

    def __str__(self) -> str:
        return self.FSTRING.format(self.description, self.line)


@dataclass
class ConfigList:
    configs: List[Config] = None

    def __str__(self) -> str:
        configs_string = ""
        for config in self.configs:
            configs_string += str(config)
        return configs_string
