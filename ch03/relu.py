import numpy as np

from plot_utils import plot_function


def relu(x):
    return np.maximum(0, x)

def main():
    plot_function(relu, 'relu.png', y_min=-1, y_max=6.0)

if __name__ == "__main__":
    main()