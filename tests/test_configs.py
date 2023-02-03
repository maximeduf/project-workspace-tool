import pytest
from main.config import *

expected_description = "a description"
expected_line = "a line"
expected_lines = ["some", "lines"]


class TestAliasConfig:
    def test_alias_config_init_default_not_none(self):
        config = AliasConfig()
        assert config != None

    def test_alias_config_init_default_has_type(self):
        config = AliasConfig()
        assert config.type == ConfigType.ALIAS

    def test_alias_config_init_with_arguments(self):
        config = AliasConfig(expected_description, expected_line)
        assert config.description == expected_description
        assert config.line == expected_line


class TestFunctionConfig:
    def test_function_config_init_default_not_none(self):
        config = FunctionConfig()
        assert config != None

    def test_function_config_init_default_has_type(self):
        config = FunctionConfig()
        assert config.type == ConfigType.FUNCTION

    def test_function_config_init_with_arguments_has_properties(self):
        config = FunctionConfig(expected_description, expected_lines)
        assert config.description == expected_description
        assert config.lines == expected_lines


class TestVarConfig:
    def test_var_config_init_default_not_none(self):
        config = VarConfig()
        assert config != None

    def test_var_config_init_default_has_type(self):
        config = VarConfig()
        assert config.type == ConfigType.ENV_VAR

    def test_var_config_init_with_arguments_has_properties(self):
        config = VarConfig(expected_description, expected_line)
        assert config.description == expected_description
        assert config.line == expected_line
