# src/separability.py
import numpy as np

def ensemble_distance(S0, S1):
    return np.linalg.norm(S1 - S0)

def effective_dispersion(S):
    mean = np.mean(S, axis=0)
    return np.mean(np.linalg.norm(S - mean, axis=1)**2)

def separability(S0, S1, S):
    d = ensemble_distance(S0, S1)
    sigma_eff = effective_dispersion(S)
    return d / np.sqrt(sigma_eff + 1e-12)

import numpy as np

def separability_single(field):
    """
    Compute informational separability for a single 2D field.
    This reduces the field to a 1D distribution and measures
    how 'distinct' the values are.
    """

    # Flatten the field
    x = field.flatten()

    # Normalize to [0, 1]
    x = (x - x.min()) / (x.max() - x.min() + 1e-12)

    # Histogram as probability distribution
    hist, _ = np.histogram(x, bins=50, range=(0, 1), density=True)

    # Avoid zeros
    hist = hist + 1e-12
    hist = hist / hist.sum()

    # Shannon entropy
    H = -np.sum(hist * np.log(hist))

    # Convert entropy to separability (higher = more structure)
    # Max entropy for 50 bins is log(50)
    max_H = np.log(50)

    separability = 1 - (H / max_H)

    return separability