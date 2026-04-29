# figures.py

# Visualization code for three error catastrophe figures

import numpy as np
import matplotlib.pyplot as plt

# Function for Finite-Size Scaling

def finite_size_scaling():
    sizes = np.linspace(10, 100, 10)
    data = [np.random.rand(size) for size in sizes]
    plt.figure(figsize=(10, 6))
    for size, d in zip(sizes, data):
        plt.plot(d, label=f'Size {size}')
    plt.title('Finite-Size Scaling')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.show()

# Function for Universal Scaling Collapse

def universal_scaling_collapse():
    # Sample data and scaling functions
    x = np.linspace(-3, 3, 100)
    y = np.abs(x) ** (1/2)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='Universal Scaling')
    plt.title('Universal Scaling Collapse')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.show()

# Function for 2D Lattice Transition

def lattice_transition():
    # Simulating a phase transition in a 2D lattice
    l = 20  # lattice size
    lattice = np.random.choice([0, 1], size=(l, l))
    plt.figure(figsize=(6, 6))
    plt.imshow(lattice, cmap='gray')
    plt.title('2D Lattice Transition')
    plt.axis('off')
    plt.show()

# Uncomment to run the functions:
# finite_size_scaling()
# universal_scaling_collapse()
# lattice_transition()