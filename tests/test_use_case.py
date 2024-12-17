from multi_repo_workspace.core.cli_command import Command
import pytest


class TestCommand:
    def test_config_raises_when_child_class_doesnt_implement(self):
        class MyCommand(Command[int, str]):
            def __init__(self, params: int):
                super().__init__()
                self.params = params

            def __call__(self) -> str:
                super().__call__()

        with pytest.raises(NotImplementedError):
            command = MyCommand(0)
            command()

    def test_specific_command_generics(self):
        class AnotherCommand(Command[int, str]):
            def __init__(self, params: int):
                super().__init__()
                self.params = params

            def __call__(self) -> str:
                return "sup"
        a_command = AnotherCommand(3)
        assert a_command() == "sup"

    def test_specific_command_none_params(self):
        class NoneParamsCommand(Command[None, str]):
            def __init__(self):
                super().__init__()

            def __call__(self) -> str:
                return "supsup"
        none_param_command = NoneParamsCommand()
        assert none_param_command() == "supsup"
