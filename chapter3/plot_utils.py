import os
import numpy as np
import matplotlib.pylab as plt

def plot_function(func, filename, x_min=-5.0, x_max=5.0, y_min=-0.1, y_max=1.1):
    x = np.arange(x_min, x_max, 0.1)
    y = func(x)
    plt.plot(x, y)
    plt.ylim([y_min, y_max])

    # 画像保存のための共通処理
    current_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(current_dir, 'images')

    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    plt.savefig(os.path.join(images_dir, filename))
    plt.close()