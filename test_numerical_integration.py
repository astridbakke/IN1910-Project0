import numpy as np
import pytest
from numerical_integration import left_riemann_sum, midpoint, integrate


def test_left_riemann_sum():
    f = lambda x: (3 * x**2) * np.exp(x**3)
    a, b = 0.0, 1.0
    exact_value = np.exp(1) - 1
    n = 5000
    approx_value = left_riemann_sum(f, a, b, n)
    error = abs(approx_value - exact_value)
    assert error < 0.001

def test_midpoint():
    f = lambda x: (3 * x**2) * np.exp(x**3)
    a, b = 0.0, 1.0
    
    exact_value = np.exp(1) - 1
    n = 100  
    
    approx_value = midpoint(f, a, b, n)
    
    error = abs(approx_value - exact_value)
    assert error < 0.001    

@pytest.mark.parametrize("method, n", [("midpoint", 1000), ("left_riemann_sum", 5000)])
def test_integrate(method, n):
    f = lambda x: (3 * x**2) * np.exp(x**3)
    a, b = 0.0, 1.0
    exact_value = np.exp(1) - 1
    
    approx_value = integrate(f, a, b, n, method=method)
    
    error = abs(approx_value - exact_value)
    assert error < 0.001

def test_integrate_raises_ValueError_for_invalid_method():
    with pytest.raises(ValueError):
        f = lambda x: (3 * x**2) * np.exp(x**3)
        integrate(f, a=0.0, b=1.0, n=10, method="ugyldig_metode")    
