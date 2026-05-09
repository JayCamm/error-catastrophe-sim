# src/gray_scott.py
import numpy as np
from scipy.ndimage import laplace

def gray_scott_step(u, v, Du, Dv, F, k, dt):
    Lu = laplace(u)
    Lv = laplace(v)

    uvv = u * v * v

    du = Du * Lu - uvv + F * (1 - u)
    dv = Dv * Lv + uvv - (F + k) * v

    u_next = u + dt * du
    v_next = v + dt * dv

    return u_next, v_next

def run_gray_scott(steps=2000, size=128, params=None):
    if params is None:
        params = dict(Du=0.16, Dv=0.08, F=0.035, k=0.065, dt=1.0)

    u = np.ones((size, size))
    v = np.zeros((size, size))

    # Seed perturbation
    r = size // 10
    u[size//2-r:size//2+r, size//2-r:size//2+r] = 0.50
    v[size//2-r:size//2+r, size//2-r:size//2+r] = 0.25

    trajectory = []

    for _ in range(steps):
        u, v = gray_scott_step(u, v, **params)
        trajectory.append((u.copy(), v.copy()))

    return trajectory

def run_gray_scott_frames(steps=400, dt=1.0, frame_interval=1):
    """
    Runs Gray-Scott and returns a list of frames (u fields).
    """
    u, v = initialize_fields()
    frames = []

    for t in range(steps):
        u, v = update(u, v, dt)

        if t % frame_interval == 0:
            frames.append(u.copy())

    return frames