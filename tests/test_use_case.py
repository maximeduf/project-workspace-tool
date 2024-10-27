from multi_repo_workspace.use_case import UseCase
import pytest


class TestUseCase:
    def test_config_raises_when_child_class_doesnt_implement(self):
        class MyUseCase(UseCase[int, str]):
            def __init__(self, params: int):
                super().__init__(params)

            def __call__(self) -> str:
                super().__call__()

        with pytest.raises(NotImplementedError):
            usecase = MyUseCase(0)
            usecase()

    def test_specific_use_case_generics(self):
        class AnotherUseCase(UseCase[int, str]):
            def __call__(self) -> str:
                return "sup"
        a_use_case = AnotherUseCase(3)
        assert a_use_case() == "sup"

    def test_specific_use_case_none_params(self):
        class NoneParamsUseCase(UseCase[None, str]):
            def __init__(self):
                super().__init__(None)

            def __call__(self) -> str:
                return "supsup"
        none_param_use_case = NoneParamsUseCase()
        assert none_param_use_case() == "supsup"
