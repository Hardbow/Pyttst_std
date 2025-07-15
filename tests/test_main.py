import pytest
from src.main import Calculator


@pytest.mark.parametrize(
    "x, y, res",
    [
        (1, 2, 0.5),
        (5, -1, -5),


    ]
 )
def test_divide(x, y, res):
    x = 1
    y = 2
    res = 0.5
    assert Calculator().divide(x, y) == res



@pytest.mark.parametrize(
    "x, y, res",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (0.5, 0.5, 1)
    ]
)
def test_add(x, y, res):
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
