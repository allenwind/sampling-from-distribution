import numpy as np

def normal(mu=0, sigma=1, n=100):
    """
    根据中心极限定理
    u = u1 + ... + un
    ui ~ U[0, 1]
    """
    while True:
        yield (np.mean(np.random.uniform(size=n)) - 0.5) * np.sqrt(12 * n) * sigma + mu

def gen_normal_curve(rs, u, s):
    x = np.linspace(np.min(rs), np.max(rs), len(rs))
    rs = 1 / (np.sqrt(2*np.pi)*s) * np.exp(-(x-u)**2/(2*s**2))
    return x, rs

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    mu = 1
    sigma = 2
    g = normal(mu=mu, sigma=sigma)
    rs = [next(g) for _ in range(10000)]
    rs = np.array(rs)
    plt.hist(rs, bins=100, density=True)
    x, c = gen_normal_curve(rs, u=mu, s=sigma)
    plt.plot(x, c, color="red", label="$N({},{}^2)$".format(mu, sigma))
    plt.legend(loc="upper left")
    plt.show()

    print(np.mean(rs), np.var(rs))


