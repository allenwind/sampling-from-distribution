import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 从拉普拉斯分布中采样

u = 0
b = 1 / np.sqrt(2)

u = np.random.uniform(size=10000)
y = -b * np.sign(u - 0.5) * np.log(1 - 2 * np.abs(u - 0.5))
x = np.linspace(np.min(y), np.max(y), len(y))
plt.hist(y, bins=100, density=True)
plt.plot(x, stats.laplace.pdf(x, scale=b))
plt.show()
