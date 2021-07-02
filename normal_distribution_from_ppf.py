import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 正太分布采样的逆变换法，函数为scipy.stats.norm.pdf
# 原理为分段近似

def gen_normal_curve(rs, u, s):
    x = np.linspace(np.min(rs), np.max(rs), len(rs))
    rs = 1 / (np.sqrt(2*np.pi)*s) * np.exp(-(x-u)**2/(2*s**2))
    return x, rs

x = stats.norm.ppf(np.random.uniform(size=10000))
print(stats.normaltest(x))
plt.hist(x, bins=100, density=True)
mu = 0
sigma = 1
x, c = gen_normal_curve(x, u=mu, s=sigma)
plt.plot(x, c, color="red", label="$N({},{}^2)$".format(mu, sigma))
plt.legend(loc="upper left")
plt.show()

