from abc import ABC, abstractmethod
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


class ConfigList(List):
    def __init__(self, configs: List[Config] = []):
        super().__init__(config for config in configs)

    def __setitem__(self, index, config):
        super().__setitem__(index, config)

    def __str__(self) -> str:
        configs_string = ""
        for config in self:
            configs_string += str(config)
        return configs_string

    def insert(self, index, config: Config):
        super().insert(index, config)

    def append(self, config: Config):
        super().append(config)

    def extend(self, other: Config):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(config for config in other)


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
