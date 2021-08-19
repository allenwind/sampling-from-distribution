import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def gen_normal():
    while True:
        x = np.random.uniform(-1, 1, 1)
        y = np.random.uniform(-1, 1, 1)
        r = x ** 2 + y ** 2
        if r <= 1:
            n1 = x * np.sqrt(-2 * np.log(r) / r)
            # n2 = y * np.sqrt(-2 * np.log(r) / r)
            yield n1

size = 10000
normal = gen_normal()
x = np.array([next(normal) for _ in range(size)])
print(stats.normaltest(x))
plt.hist(x, bins=100, density=True)

mu = np.mean(x)
sigma = np.std(x)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, size)
y = stats.norm.pdf(x, mu, sigma)
plt.plot(x, y, 'r')
plt.show()
