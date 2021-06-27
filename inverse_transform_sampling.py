import numpy as np

def inverse_transform_sampling(invp):
    """
    逆变换采样
    invp:目标采样概率密度函数的逆函数
    """
    while True:
        u = np.random.uniform(-1, 1)
        yield invp(u) * np.sqrt(2)

def gen_normal_curve(rs, u, s):
    x = np.linspace(np.min(rs), np.max(rs), len(rs))
    rs = 1 / (np.sqrt(2*np.pi)*s) * np.exp(-(x-u)**2/(2*s**2))
    return x, rs

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from scipy.special import erfinv

    g = inverse_transform_sampling(invp=erfinv)
    rs = []
    for _ in range(10000):
        rs.append(next(g))
    rs = np.array(rs)
    print(np.mean(rs), np.var(rs))
    plt.hist(rs, bins=100, density=True, label="sampling")

    u = 0
    s = 1
    x, c = gen_normal_curve(rs, u, s)
    plt.plot(x, c, color="red", label="$N({},{}^2)$".format(u, s))
    plt.legend(loc="upper left")
    plt.show()
