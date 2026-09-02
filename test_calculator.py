""" To run this test use this command: pytest """

from calculator import add, divide, factorial
import numpy as np
import pytest

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (5, 5, 10)
])
def test_add(x, y, expected):
    assert add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (0.1, 0.2, 0.3),
    (1.5, 2.5, 4.0),
    (-0.5, 0.5, 0.0)
])
def test_add_floats(x, y, expected):
    assert np.isclose(add(x, y), expected)

@pytest.mark.parametrize("x, y, expected", [
    (6, 2, 3),
    (5, 2, 2.5),
    (-9, 3, -3)
])
def test_divide(x, y, expected):
    assert np.isclose(divide(x, y), expected)

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (6, 720)
])
def test_factorial(n, expected):
    assert factorial(n) == expected           



