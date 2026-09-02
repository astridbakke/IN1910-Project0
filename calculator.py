def add(x: float, y: float) -> float:
    """ Add two numbers together and return the sum. """
    return x + y

def divide(x: float, y: float) -> float:
    """ Divide x by y and return the result. """
    return x / y

def factorial(n: int) -> int:
    """ Computes the factorial of an integer n. """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sin(x: float, N: int = 20) -> float:
    """ Computes the sine of an angle using a Taylor series approximation. """
    total = 0.0
    for n in range(N):
        term = ((-1)**n * x**(2*n + 1)) / factorial(2*n + 1)
        total += term
    return total

def mean(x: list) -> float:
    """ Computes the mean of a list of numbers """
    return sum(x) / len(x)



