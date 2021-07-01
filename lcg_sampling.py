import numpy as np

def lcg(x0, a=1103515245, b=12345, m=2**31-1, normalize=True):
    """线性同余法"""
    while True:
        xt = np.mod(a*x0 + b, m)
        if normalize:
            x = xt / m
        else:
            x = xt
        yield x

        x0 = xt

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    x0 = 1023
    rs = []
    g = lcg(x0)
    for _ in range(10000):
        rs.append(next(g))

    plt.hist(np.array(rs), bins=100, density=True, label="sampling")
    plt.hlines(1, 0, 1, color="red", label="U[0,1]")
    plt.legend(loc="upper left")
    plt.show()

