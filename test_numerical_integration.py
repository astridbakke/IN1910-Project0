""" To run this test use this command: pytest """

import numpy as np
import pytest
from numerical_integration import left_riemann_sum, midpoint, integrate, convergence_rate


def test_left_riemann_sum() -> None:
    f = lambda x: (3 * x**2) * np.exp(x**3)
    a, b = 0.0, 1.0
    exact_value = np.exp(1) - 1
    n = 5000
    approx_value = left_riemann_sum(f, a, b, n)
    error = abs(approx_value - exact_value)
    assert error < 0.001

def test_midpoint() -> None:
    f = lambda x: (3 * x**2) * np.exp(x**3)
    a, b = 0.0, 1.0
    
    exact_value = np.exp(1) - 1
    n = 100  
    
    approx_value = midpoint(f, a, b, n)
    
    error = abs(approx_value - exact_value)
    assert error < 0.001    

@pytest.mark.parametrize("method, n", [("midpoint", 1000), ("left_riemann_sum", 5000)])
def test_integrate(method: str, n: int) -> None:
    f = lambda x: (3 * x**2) * np.exp(x**3)
    a, b = 0.0, 1.0
    exact_value = np.exp(1) - 1
    
    approx_value = integrate(f, a, b, n, method=method)
    
    error = abs(approx_value - exact_value)
    assert error < 0.001

def test_integrate_raises_ValueError_for_invalid_method() -> None:
    with pytest.raises(ValueError):
        f = lambda x: (3 * x**2) * np.exp(x**3)
        integrate(f, a=0.0, b=1.0, n=10, method="ugyldig_metode") 

@pytest.mark.parametrize("method, expected_rate", [
    ("left_riemann_sum", 1.0),
    ("midpoint", 2.0)
])
def test_rate_of_convergence(method: str, expected_rate: float) -> None:
    f = lambda x: (3 * x**2) * np.exp(x**3)
    a, b = 0.0, 1.0
    exact_value = np.exp(1) - 1
    
    n_values = [32, 64, 128, 256]
    
    r = convergence_rate(f, a, b, exact_value, n_values, method=method)
    
    assert abs(r - expected_rate) < 0.1