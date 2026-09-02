def add(x: float, y: float) -> float:
    """ Add two numbers together and return the sum. """
    return x + y

def divide(x: float, y: float) -> float:
    """ Divide x by y and return the result. """
    return x / y

def factorial(n: int) -> int:
    """ Computes the factorial of an integer n """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result




