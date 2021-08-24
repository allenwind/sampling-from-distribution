import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 从拉普拉斯分布中采样
# 参考https://en.wikipedia.iwiki.eu.org/wiki/Laplace_distribution

def laplace_generator():
    while True:
        u1, u2 = np.random.uniform(size=2)
        yield np.log(u1 / u2)

gen = laplace_generator()
n = 10000
y = np.array([next(gen) for _ in range(n)])
x = np.linspace(np.min(y), np.max(y), len(y))
plt.hist(y, bins=100, density=True)
plt.plot(x, stats.laplace.pdf(x))
plt.show()
