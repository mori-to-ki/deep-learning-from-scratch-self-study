import numpy as np

from plot_utils import plot_function


def step_function(x):
    return np.array(x > 0, dtype=int)

def main():
    plot_function(step_function, 'step_function.png')

if __name__ == "__main__":
    main()