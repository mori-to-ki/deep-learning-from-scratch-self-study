from dataset.mnist import load_mnist

def main():
    print("===")
    print("最初のデータの呼び出しは数分待つらしい")
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=False, flatten=True)
    print("===")
    print("それぞれのデータの形状を出力")
    print(f">> x_train.shape: {x_train.shape} # (60000, 784)")
    print(f">> t_train.shape: {t_train.shape} # (60000,)")
    print(f">> x_test.shape: {x_test.shape} # (10000, 784)")
    print(f">> t_test.shape: {t_test.shape} # (10000,)")
    print("===")

if __name__ == "__main__":
    main()
