import numpy as np

def chaos(r, x0, size=2000):
    y = []
    for i in range(size):
        x = r * x0 * (1-x0)
        y.append(x)
        x0 = x
    return np.array(y)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    x = chaos(r=3.89, x0=0.8989)
    plt.hist(x, bins=100, density=False)
    plt.show()

