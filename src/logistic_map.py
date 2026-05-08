# src/logistic_map.py
import numpy as np

def logistic_map(r, x0, steps=500):
    xs = np.zeros(steps)
    xs[0] = x0
    for t in range(1, steps):
        xs[t] = r * xs[t-1] * (1 - xs[t-1])
    return xs