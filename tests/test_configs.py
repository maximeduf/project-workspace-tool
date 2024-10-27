import pytest
from multi_repo_workspace.config import (
    Config, ConfigType, AliasConfig, FunctionConfig, VarConfig, ConfigList
)

expected_description = "a description"
expected_line = "a line"
expected_lines = ["some", "lines", "}"]


class TestConfig:
    def test_config_raises_when_child_class_doesnt_implement(self):
        class FaultyConfigClass(Config):
            def __init__(self, desc=''):
                super().__init__(desc, ConfigType.ALIAS)

            # we trick the interpreter into thinking we implemented
            #  config methods
            def __str__(self):
                super().__str__()

        with pytest.raises(NotImplementedError):
            some_config = FaultyConfigClass()
            some_config.__str__()


class TestAliasConfig:
    default_config = AliasConfig()
    config = AliasConfig(expected_description, expected_line)

    def test_init_default_not_none(self):
        assert self.default_config is not None

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
        assert self.default_config is not None

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
        assert self.default_config is not None

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
        assert self.default_config_list is not None

    def test_init_default_with_configs(self):
        assert self.config_list == self.configs

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

    def test_set_item(self):
        config_to_set = AliasConfig("bop", "bwap")
        index_to_set = 1
        old_item_at_index = self.config_list[index_to_set]
        self.config_list[index_to_set] = config_to_set
        assert self.config_list[index_to_set] != old_item_at_index
        assert self.config_list[index_to_set].type == ConfigType.ALIAS
        assert self.config_list[index_to_set].line == "bwap"
        assert self.config_list[index_to_set].description == "bop"

    def test_insert(self):
        config_to_insert = AliasConfig("boop", "beep")
        index_to_insert = 1
        old_item_at_index = self.config_list[index_to_insert]
        self.config_list.insert(index_to_insert, config_to_insert)
        assert self.config_list[index_to_insert] != old_item_at_index
        assert self.config_list[index_to_insert].type == ConfigType.ALIAS
        assert self.config_list[index_to_insert].line == "beep"
        assert self.config_list[index_to_insert].description == "boop"

    def test_append(self):
        config_to_append = AliasConfig("boom", "tsee")
        old_last_item = self.config_list[-1]
        self.config_list.append(config_to_append)
        assert self.config_list[-1] != old_last_item
        assert self.config_list[-1].type == ConfigType.ALIAS
        assert self.config_list[-1].line == "tsee"
        assert self.config_list[-1].description == "boom"

    def test_extend_same(self):
        some_configs = ConfigList([
            AliasConfig("one", "two"),
            VarConfig("three", "four")
        ])
        configs_to_extend = ConfigList([
            FunctionConfig("a function", ["one", "two", "three lines"]),
            VarConfig("my fancy variable", "export stuff=things")
        ])

        len_old_configs = len(some_configs)
        len_extended = len(configs_to_extend)

        some_configs.extend(configs_to_extend)
        assert (len_old_configs + len_extended) == len(
                some_configs), (
                f"len of extended config should be {len_old_configs} + "
                f"{len_extended} = {len(some_configs)}"
            )

    def test_extend_different_iterable(self):
        some_configs = ConfigList([
            AliasConfig("one", "two"),
            VarConfig("three", "four")
        ])
        configs_to_extend = [
            FunctionConfig("a function", ["one", "two", "three lines"]),
            VarConfig("my fancy variable", "export stuff=things")
        ]

        len_old_configs = len(some_configs)
        len_extended = len(configs_to_extend)

        some_configs.extend(configs_to_extend)
        assert (len_old_configs + len_extended) == len(
                some_configs), (
                f"len of extended config should be {len_old_configs} + "
                f"{len_extended} = {len(some_configs)}"
            )
