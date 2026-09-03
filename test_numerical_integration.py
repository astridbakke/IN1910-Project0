import numpy as np
from numerical_integration import left_riemann_sum


def test_left_riemann_sum():
    f = lambda x: (3 * x**2) * np.exp(x**3)
    a, b = 0.0, 1.0
    exact_value = np.exp(1) - 1
    n = 5000
    approx_value = left_riemann_sum(f, a, b, n)
    error = abs(approx_value - exact_value)
    assert error < 0.001
