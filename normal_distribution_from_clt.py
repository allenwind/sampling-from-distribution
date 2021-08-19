import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

poisson = lambda: np.random.poisson(lam=100)
uniform = lambda: np.random.uniform()
normal = lambda: np.random.normal()
laplace = lambda: np.random.laplace()
gumbel = lambda: np.random.gumbel()
exponential = lambda: np.random.exponential()

probs = [poisson, uniform, normal, laplace, gumbel, exponential]

def gen_random(n=100, p=None):
    """中心极限定理表明多个独立统计量（可以具有不同分布）的平均值满足正太分布"""
    nums = []
    for _ in range(n):
        f = np.random.choice(probs, p=p)
        nums.append(f())
    return np.mean(nums)

size = 10000
nums = [gen_random(100) for _ in range(size)]
plt.hist(nums, bins=100, density=True)

mu = np.mean(nums)
sigma = np.std(nums)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, size)
y = stats.norm.pdf(x, mu, sigma)
plt.plot(x, y, 'r')
plt.show()
