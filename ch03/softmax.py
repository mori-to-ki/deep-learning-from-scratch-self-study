import numpy as np

def softmax(x):
    c = np.max(x)
    exp_x = np.exp(x - c)
    sum_exp_x = np.sum(exp_x)
    return exp_x / sum_exp_x

def main():
    x = np.array([0.3, 2.9, 4.0])
    y = softmax(x)
    print("===")
    print("1.0が表示されればOK")
    print(f">> {np.sum(y)}") # 1.0 ならOK
    print("===")

if __name__ == "__main__":
    main()