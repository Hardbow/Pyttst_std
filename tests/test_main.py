import pytest
from src.main import Calculator
from contextlib import nullcontext as does_not_raise


class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (1, 2, 0.5, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, "-1", -5, pytest.raises(TypeError)),
            (5, 0, -5, pytest.raises(ZeroDivisionError)),
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res",
        [
            (1, 2, 3),
            (-1, 1, 0),
            (0.5, "0.5", 1)
        ]
    )
    def test_add(self, x, y, res):
        with pytest.raises(TypeError):
            assert Calculator().add(x, y) == res

# def test_2():
#     assert 2 == 2
#
# def test_sum():
#     x = 1
#     y = 2
#     assert x + y == 3
#
# def test_division():
#     x = 1
#     y = 2
#     assert x / y == 0.5
