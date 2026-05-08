# src/visualization.py
import matplotlib.pyplot as plt
import numpy as np

def plot_separability(xs, savepath=None):
    plt.figure(figsize=(8,4))
    plt.plot(xs)
    plt.title("Informational Separability x(t)")
    plt.xlabel("Time")
    plt.ylabel("x")
    if savepath:
        plt.savefig(savepath, dpi=200)
    plt.show()

def plot_gray_scott(u, v, savepath=None):
    fig, ax = plt.subplots(1,2, figsize=(10,5))
    ax[0].imshow(u, cmap='viridis')
    ax[0].set_title("u field")
    ax[1].imshow(v, cmap='inferno')
    ax[1].set_title("v field")
    if savepath:
        plt.savefig(savepath, dpi=200)
    plt.show()