import numpy as np
import matplotlib.pyplot as plt

def uniform(n, m=2**31-1, a=1103515245, b=12345):
    state = 0.66
    rs = np.zeros(n)
    for i in range(n):
        x = (a * state + b) % m
        u = x / m
        state = x
        rs[i] = u
    return rs

def test_uniform():
    rs = uniform(1000)
    plt.subplot(211)
    plt.plot(rs, "+")
    plt.subplot(212)
    plt.hist(rs, bins=100, density=True)
    plt.hlines(1, 0, 1, color="red")
    plt.show()

if __name__ == "__main__":
    test_uniform()

