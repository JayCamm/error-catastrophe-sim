import os
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# Helper: ensure directory exists before saving
# ---------------------------------------------------------
def ensure_dir(path):
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

# ---------------------------------------------------------
# Plot separability x(t)
# ---------------------------------------------------------
def plot_separability(xs, savepath=None):
    plt.figure(figsize=(8, 4))
    plt.plot(xs, color='blue')
    plt.title("Informational Separability x(t)")
    plt.xlabel("Time")
    plt.ylabel("x")

    if savepath:
        ensure_dir(savepath)
        plt.savefig(savepath, dpi=200)

    plt.show()

# ---------------------------------------------------------
# Plot Gray-Scott fields (u and v)
# ---------------------------------------------------------
def plot_gray_scott(u, v, savepath=None):
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    ax[0].imshow(u, cmap='viridis')
    ax[0].set_title("u field")
    ax[0].axis('off')

    ax[1].imshow(v, cmap='inferno')
    ax[1].set_title("v field")
    ax[1].axis('off')

    if savepath:
        ensure_dir(savepath)
        plt.savefig(savepath, dpi=200)

    plt.show()

# ---------------------------------------------------------
# Plot failure propagation curve p(t)
# ---------------------------------------------------------
def plot_failure(p, savepath=None):
    plt.figure(figsize=(8, 4))
    plt.plot(p, color='red')
    plt.title("Failure Propagation p(t)")
    plt.xlabel("Time")
    plt.ylabel("p")

    if savepath:
        ensure_dir(savepath)
        plt.savefig(savepath, dpi=200)

    plt.show()