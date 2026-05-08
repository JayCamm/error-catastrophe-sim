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