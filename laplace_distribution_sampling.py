import numpy as np
import matplotlib.pyplot as plt

# 从拉普拉斯分布中采样

u = 0
b = 1 / np.sqrt(2)

u = np.random.uniform(size=10000)
x = -b * np.sign(u - 0.5) * np.log(1 - 2 * np.abs(u - 0.5))
plt.hist(x, bins=100)
plt.show()
