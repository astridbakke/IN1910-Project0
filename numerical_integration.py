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


if __name__ == "__main__":
    def plot_integral(f, x, h=0.3, method="Left Riemann sum"):
        y = f(x)
        fig, ax = plt.subplots()
        ax.plot(x, y)

        for xi in np.arange(0, x[-1], h):
            yi = f(xi)
            ax.plot([xi, xi, xi + h, xi + h], [0, yi, yi, 0], color="r")
        
        ax.grid()
        ax.set_title(f"{method} (h = {h})")
        plt.show()

    x = np.linspace(0, 1)
    f = lambda x: (3 * x**2) * np.exp(x**3)
    
    resultat = left_riemann_sum(f, 0, 1, n=10)
    print(f"Areal (n=10): {resultat}")
    plot_integral(f, x)