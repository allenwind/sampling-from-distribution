import numpy as  np
import matplotlib.pyplot as plt

# 从指数分布中采样

a = 1
u = np.random.uniform(size=10000)
x = - 1 / a * np.log(1 - u)

def exponential_pdf(x, a):
    return a * np.exp(- a * x)

plt.hist(x, bins=100, density=True)


x1 = np.min(x)
x2 = np.max(x)
x = np.linspace(x1, x2, len(x))
plt.plot(x, exponential_pdf(x, a))

plt.show()
