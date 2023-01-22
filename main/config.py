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
    desc: str

    def __init__(self, desc: str, type: ConfigType):
        self.desc = desc
        self.type = type

    @abstractmethod
    def __str__(self) -> str:
        ...


class AliasConfig(Config):
    line: str

    def __init__(self, desc: str, alias: str):
        super().__init__(desc, ConfigType.ALIAS)
        self.line = alias

    def __str__(self) -> str:
        return self.FSTRING.format(self.desc, self.line)


class FunctionConfig(Config):
    lines: List[str]

    def __init__(self, desc: str, *lines: List[str]):
        super().__init__(desc, ConfigType.FUNCTION)
        self.lines = lines

    def __str__(self) -> str:
        function_string: str = ""
        for line in self.lines:
            function_string += line

        return self.FSTRING.format(self.desc, "\n".join(self.lines))


class VarConfig(Config):
    line: str

    def __init__(self, desc: str, line: str):
        super().__init__(desc, ConfigType.ENV_VAR)
        self.line = line

    def __str__(self) -> str:
        return self.FSTRING.format(self.desc, self.line)


@dataclass
class ConfigList:
    configs: List[Config] = None

    def __str__(self) -> str:
        configs_string = ""
        for config in self.configs:
            configs_string += str(config)
        return configs_string
