import numpy as np

def lcg_discrete(ar, br, x0=1023, a=1103515245, b=12345, m=2**31-1):
    """线性同余法生成离散的均匀分布"""
    while True:
        xt = np.mod(a*x0 + b, m)
        x = xt / m
        yield int(ar + (br - ar) * x)

        x0 = xt

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    rs = []
    g = lcg_discrete(0, 100)
    for _ in range(10000):
        rs.append(next(g))

    plt.hist(np.array(rs), bins=100, density=False, label="sampling")
    # plt.hlines(1, 0, 1, color="red", label="U[0,1]")
    plt.legend(loc="upper left")
    plt.show()

