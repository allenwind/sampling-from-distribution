import itertools
import numpy as np

# shuffle f(x) = x 的方式获得均匀分布

def uniform_generator(a, b, bins=None, bufsize=10000):
    buff = np.linspace(a, b, bufsize)
    np.random.shuffle(buff)
    for i in itertools.cycle(buff):
        yield i

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    a = 0
    b = 1
    rs = []
    g = uniform_generator(a, b)
    for _ in range(10000):
        rs.append(next(g))

    plt.hist(np.array(rs), bins=100, density=True, label="sampling")
    plt.hlines(1, 0, 1, color="red", label="U[0,1]")
    plt.legend(loc="upper left")
    plt.show()
