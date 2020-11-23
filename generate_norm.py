import numpy as np
import matplotlib.pyplot as plt

def normal_by_box_muler(n, u=0, s=1):
    rs = np.zeros(n)
    for i in range(n):
        u1 = np.random.uniform(size=1)
        u2 = np.random.uniform(size=1)
        v = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
        v = u + s * v
        rs[i] = v
    return rs

def normal_by_fix_box_muller(n, u=0, s=1):
    pass

def gen_normal_curve(rs, u, s):
    x = np.linspace(np.min(rs), np.max(rs), len(rs))
    rs = 1 / (np.sqrt(2*np.pi)*s) * np.exp(-(x-u)**2/(2*s**2))
    return x, rs

def test_normal():
    u = 4
    s = 2
    rs = normal_by_box_muler(10000, u, s)
    plt.subplot(211)
    plt.plot(rs, "+", label="samples={}".format(len(rs)))
    plt.legend(loc="upper left")

    plt.subplot(212)
    plt.hist(rs, bins=300, density=True, label="samples histogram")
    x, c = gen_normal_curve(rs, u, s)
    plt.plot(x, c, color="red", label="$N({},{}^2)$".format(u, s))
    plt.legend(loc="upper left")
    plt.show()

if __name__ == "__main__":
    test_normal()
