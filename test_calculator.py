from calculator import add
import numpy as np


def test_add():
    assert add(1, 2) == 3

def test_add_floats():
    assert np.isclose(add(0.1, 0.2), 0.3)