# src/run_all.py
import numpy as np
from gray_scott import run_gray_scott
from separability import separability
from recoverability import recoverability, propagate_failure
from visualization import plot_separability, plot_gray_scott

def main():
    traj = run_gray_scott(steps=500)
    xs = []

    for t in range(2, len(traj)):
        u0, v0 = traj[t-2]
        u1, v1 = traj[t-1]
        u, v = traj[t]

        S0 = np.stack([u0, v0], axis=-1)
        S1 = np.stack([u1, v1], axis=-1)
        S  = np.stack([u,  v ], axis=-1)

        xs.append(separability(S0, S1, S))

    xs = np.array(xs)
    plot_separability(xs, savepath="../figures/separability.png")

    # Example catastrophe simulation
    p = propagate_failure(0.01, xs, x_star=0.5)

if __name__ == "__main__":
    main()