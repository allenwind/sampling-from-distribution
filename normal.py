import numpy as np
import matplotlib.pyplot as plt

def normal(n):
    values = np.zeros(n)
    for i in range(n):
        u1 = np.random.uniform(size=1)
        u2 = np.random.uniform(size=1)
        v = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
        values[i] = v
    return values

def test_normal():
    values = normal(1000)
    plt.subplot(211)
    plt.plot(values)
    plt.subplot(212)
    plt.hist(values)
    plt.show()

if __name__ == "__main__":
    test_normal()
