from typing import Callable  # allows type annotations for functions, as seen below:
import matplotlib.pyplot as plt
import numpy as np


def left_riemann_sum(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    h = (b - a) / n
    total = 0.0
    for i in range(n):
        xi = a + i * h
        total += f(xi)
    return h * total


def midpoint(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """ Computes the integral using the midpoint/trapezoidal rule. """
    h = (b - a) / n
    total = 0.0
    for i in range(n):
        xi = a + i * h
        total += 0.5 * (f(xi) + f(xi + h))
    return h * total



def integrate(
    f: Callable[[float], float], a: float, b: float, n: int, method: str = "midpoint"
) -> float:
    """ function for calculating an integral using a chosen method. """
    if method == "midpoint":
        return midpoint(f, a, b, n)
    elif method == "left_riemann_sum":
        return left_riemann_sum(f, a, b, n)
    else:
        raise ValueError(f"Ugyldig metode: '{method}'. Bruk 'midpoint' eller 'left_riemann_sum'.")







if __name__ == "__main__":
    import matplotlib.pyplot as plt

    def plot_integral(f, x, h=0.3, method="Midpoint"):
        y = f(x)

        fig, ax = plt.subplots()
        ax.plot(x, y)

        for xi in np.arange(0, x[-1], h):
            if method == "Midpoint":
                yi = 0.5 * (f(xi) + f(xi + h))
            else:
                yi = f(xi)
            ax.plot([xi, xi, xi + h, xi + h], [0, yi, yi, 0], color="r")
        ax.grid()
        ax.set_title(f"{method} (h = {h})")
        plt.show()

    x = np.linspace(0, 1)
    f = lambda x: (3 * x**2) * np.exp(x**3)

    plot_integral(f, x, method="Left Riemann sum")