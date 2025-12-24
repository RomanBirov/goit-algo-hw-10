import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


def f(x):
    return x ** 2


def monte_carlo_integral(func, a, b, num_points):
    max_y = max(func(a), func(b))

    hits = 0
    for _ in range(num_points):
        x = random.uniform(a, b)
        y = random.uniform(0, max_y)
        if y <= func(x):
            hits += 1

    rectangle_area = (b - a) * max_y
    return rectangle_area * (hits / num_points)


if __name__ == "__main__":
    random.seed(42)

    a = 0
    b = 2

    quad_result, quad_error = spi.quad(f, a, b)
    print(f"SciPy (quad) result: {quad_result:.8f} (err≈{quad_error:.2e})\n")

    print("| Num_points | Monte-Carlo   | Abs Error |")
    print("|------------|---------------|-----------|")

    for n in [1000, 100000]:
        mc_result = monte_carlo_integral(f, a, b, n)
        err = abs(mc_result - quad_result)
        print(f"| {n:<10} | {mc_result:<13.8f} | {err:<9.6f} |")

    # Графік
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=2)

    ix = np.linspace(a, b, 200)
    iy = f(ix)
    ax.fill_between(ix, iy, alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.axvline(x=a, linestyle="--")
    ax.axvline(x=b, linestyle="--")
    ax.set_title(f"Графік інтегрування f(x) = x^2 від {a} до {b}")
    ax.grid(True)
    plt.show()