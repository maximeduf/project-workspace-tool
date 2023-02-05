import pytest
from main.config import *

expected_description = "a description"
expected_line = "a line"
expected_lines = ["some", "lines", "}"]


class TestConfig:
    def test_error_instantiation_of_abc(self):
        with pytest.raises(TypeError):
            config = Config()

    def test_children_must_implement_abstract_method(self):
        class SomeConfig(Config):
            def __init__(self, desc=''):
                super().__init__(desc, ConfigType.ALIAS)

            def __str__(self):
                super().__str__()

        with pytest.raises(NotImplementedError):
            some_config = SomeConfig()
            some_config.__str__()


class TestAliasConfig:
    default_config = AliasConfig()
    config = AliasConfig(expected_description, expected_line)

    def test_init_default_not_none(self):
        assert self.default_config != None

    def test_init_default_has_type(self):
        assert self.default_config.type == ConfigType.ALIAS

    def test_init_with_arguments(self):
        assert self.config.description == expected_description
        assert self.config.line == expected_line

    def test_str_has_three_lines(self):
        assert len(self.config.__str__().splitlines()) == 3

    def test_str_first_line_is_comment_with_description(self):
        first_line = self.config.__str__().splitlines()[0]
        assert first_line.find("#") == 0
        assert first_line.find(expected_description) != -1

    def test_str_second_line_is_shell_alias(self):
        second_line = self.config.__str__().splitlines()[1]
        assert second_line.find(expected_line) != -1

    def test_str_last_line_is_empty(self):
        last_line = self.config.__str__().splitlines()[-1]
        assert last_line == ''


class TestFunctionConfig:
    default_config = FunctionConfig()
    config = FunctionConfig(expected_description, expected_lines)

    def test_init_default_not_none(self):
        assert self.default_config != None

    def test_init_default_has_type(self):
        assert self.default_config.type == ConfigType.FUNCTION

    def test_init_with_arguments_has_properties(self):
        assert self.config.description == expected_description
        assert self.config.lines == expected_lines

    def test_str_has_two_lines_plus_lines_of_function(self):
        assert len(self.config.__str__().splitlines()) == (
            2 + len(expected_lines))

    def test_str_first_line_is_comment_with_description(self):
        first_line = self.config.__str__().splitlines()[0]
        assert first_line.find("#") == 0
        assert first_line.find(expected_description) != -1

    def test_str_middle_lines_are_the_shell_function(self):
        middle_lines = self.config.__str__().splitlines()[1:-2]
        for index, line in enumerate(middle_lines):
            assert line == expected_lines[index]

    def test_str_last_line_is_empty(self):
        last_line = self.config.__str__().splitlines()[-1]
        assert last_line == ''


class TestVarConfig:
    default_config = VarConfig()
    config = VarConfig(expected_description, expected_line)

    def test_init_default_not_none(self):
        assert self.default_config != None

    def test_init_default_has_type(self):
        assert self.default_config.type == ConfigType.ENV_VAR

    def test_init_with_arguments_has_properties(self):
        assert self.config.description == expected_description
        assert self.config.line == expected_line

    def test_str_has_three_lines(self):
        assert len(self.config.__str__().splitlines()) == 3

    def test_str_first_line_is_comment_with_description(self):
        first_line = self.config.__str__().splitlines()[0]
        assert first_line.find("#") == 0
        assert first_line.find(expected_description) != -1

    def test_str_middle_lines_are_the_shell_function(self):
        middle_lines = self.config.__str__().splitlines()[1:-2]
        for index, line in enumerate(middle_lines):
            assert line == expected_lines[index]

    def test_str_last_line_is_empty(self):
        last_line = self.config.__str__().splitlines()[-1]
        assert last_line == ''


class TestConfigList:
    alias = AliasConfig(expected_description, expected_line)
    function = FunctionConfig(expected_description, expected_lines)
    var = VarConfig(expected_description, expected_line)
    configs = [alias, function, var]

    default_config_list = ConfigList()
    config_list = ConfigList(configs)

    def test_init_default(self):
        assert self.default_config_list != None

    def test_init_default_with_configs(self):
        assert self.config_list.configs == self.configs

    def test_str_has_str_of_each_config(self):
        lines = self.config_list.__str__().splitlines()

        alias_lines = self.alias.__str__().splitlines()
        function_lines = self.function.__str__().splitlines()
        var_lines = self.var.__str__().splitlines()

        line_count = 0
        for line in alias_lines:
            assert line == lines[line_count]
            line_count += 1

        for line in function_lines:
            assert line == lines[line_count]
            line_count += 1

        for line in var_lines:
            assert line == lines[line_count]
            line_count += 1

        assert len(lines) == line_count
