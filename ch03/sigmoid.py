import numpy as np

from plot_utils import plot_function

def sigmoid(x):
    return 1 / (1 + np.exp(- x))

def main():
    plot_function(sigmoid, 'sigmoid.png')

if __name__ == "__main__":
    main()