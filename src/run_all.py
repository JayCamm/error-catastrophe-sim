import os
import numpy as np

from separability import separability
from gray_scott import run_gray_scott
from logistic_map import run_logistic_map
from recoverability import failure_propagation
from visualization import (
    plot_separability,
    plot_gray_scott,
    plot_failure
)

# ---------------------------------------------------------
# Helper: ensure directory exists
# ---------------------------------------------------------
def ensure_dir(path):
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

# ---------------------------------------------------------
# Main execution
# ---------------------------------------------------------
def main():

    print("Running simulations...")

    # -----------------------------------------------------
    # 1. Logistic map separability demo
    # -----------------------------------------------------
    print("Computing separability x(t) for logistic map...")
    xs = separability()
    sep_path = "figures/separability.png"
    ensure_dir(sep_path)
    plot_separability(xs, savepath=sep_path)
    print(f"Saved separability figure to {sep_path}")

    # -----------------------------------------------------
    # 2. Gray-Scott simulation
    # -----------------------------------------------------
    print("Running Gray-Scott model...")
    u, v = run_gray_scott(steps=200)
    gs_path = "figures/gray_scott/fields.png"
    ensure_dir(gs_path)
    plot_gray_scott(u, v, savepath=gs_path)
    print(f"Saved Gray-Scott fields to {gs_path}")

    # -----------------------------------------------------
    # 3. Failure propagation (error catastrophe)
    # -----------------------------------------------------
    print("Running failure propagation model...")
    p = failure_propagation()
    fail_path = "figures/catastrophe/failure.png"
    ensure_dir(fail_path)
    plot_failure(p, savepath=fail_path)
    print(f"Saved failure propagation figure to {fail_path}")

    print("All simulations complete.")


if __name__ == "__main__":
    main()