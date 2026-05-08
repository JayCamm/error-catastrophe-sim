# src/recoverability.py
import numpy as np

def recoverability(x):
    return 1 - np.exp(-0.5 * x**2)

def beta(x, x_star):
    return np.exp(-x / x_star)

def propagate_failure(p0, xs, x_star):
    p = np.zeros_like(xs)
    p[0] = p0
    for t in range(1, len(xs)):
        p[t] = beta(xs[t], x_star) * p[t-1]
    return p