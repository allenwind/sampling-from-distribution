import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def normal_generator():
    while True:
        u = np.random.uniform()
        x = np.sqrt(np.pi / 8) * np.log(u / (1 - u))
        r = np.roots([0.044715, 0, 1, -x])
        yield r[-1].real

def normal_generator2():
    p = 1 / 0.044715
    t = -np.sqrt(np.pi / 8) / 0.044715
    while True:
        u = np.random.uniform()
        u = np.log(u / (1 - u))
        q = t * u
        d = np.sqrt(q ** 2 / 4 + p ** 3 / 27)
        r = np.cbrt(-q / 2 + d) + np.cbrt(-q / 2 - d)
        yield r

size = 10000
gen = normal_generator2()
ns = np.array([next(gen) for _ in range(size)])
print(stats.normaltest(ns))
plt.hist(ns, bins=100, density=True)

mu = 0
sigma = 1
x = np.linspace(np.min(ns), np.max(ns), size)
y = stats.norm.pdf(x, mu, sigma)
plt.plot(x, y, 'r')
plt.show()
