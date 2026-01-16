import numpy as np


def generate_linear_data(n=20, noise=0.5):
    x = np.linspace(-3, 3, n)
    y = 0.8 * x + 1 + np.random.normal(0, noise, n)
    return x, y


def generate_nonlinear_data(n=25, noise=0.4):
    x = np.linspace(-3, 3, n)
    y = 0.3 * x**2 - 0.5 * x + 1 + np.random.normal(0, noise, n)
    return x, y
