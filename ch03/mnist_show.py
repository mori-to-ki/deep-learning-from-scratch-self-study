import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

def main():
    print("===")
    print("最初のデータの呼び出しは数分待つらしい")
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=False, flatten=True)
    print("===")
    img = x_train[0]
    label = t_train[0]
    print("")
    print(f">> label: {label} # 5")
    print(f">> img.shape: {img.shape} # (784,)")
    print("===")
    img = img.reshape(28, 28)
    print(f">> (元のサイズに変形済み)img.shape: {img.shape} # (28, 28)")
    print("===")
    img_show(img)

if __name__ == "__main__":
    main()