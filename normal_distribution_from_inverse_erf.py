import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

size = 100000
k = 1.7017 / 2

u = np.random.uniform(size=size)
x = -1/(2*k) * np.log(1/u - 1)
print(stats.normaltest(x))
plt.hist(x, bins=1000, density=True)

mu = np.mean(x)
sigma = np.std(x)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, size)
y = stats.norm.pdf(x, mu, sigma)

plt.plot(x, y, 'r')
plt.show()
