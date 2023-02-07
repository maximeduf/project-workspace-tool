
from main.use_case import UseCase
from unittest.mock import patch
import pytest

class TestUseCase:
    def test_specific_use_case_must_implement_abc(self):
        class MyUseCase(UseCase[int, str]):
            pass
        with pytest.raises(TypeError):
            MyUseCase()

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
