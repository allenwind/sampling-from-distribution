import numpy as np
import functools

def accept_reject_sampling(pf, qf, q_gen, M):
    """
    pf:目标采样概率密度函数
    qf:参考分布概率密度函数
    q_gen:参考分布采样生成器
    M:使得pf(x)<=qf(x)*M，qf(x)*M称为pf(x)的包络函数
    """
    for x in q_gen():
        u = np.random.uniform()
        if u < pf(x) / (M * qf(x)):
            yield x

def uniform_qf(x, a, b):
    if isinstance(x, np.ndarray):
        return np.array([1 / (b - a)] * len(x))
    return 1 / (b - a)

def normal_pf(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(- np.square(x) / 2)

def q_gen(a, b):
    while True:
        yield np.random.uniform(a, b)

def M(a, b):
    return (b - a) / np.sqrt(2 * np.pi)

if __name__ == "__main__":
    # 这里使用均匀分布作为参考分布，采样正太分布
    import matplotlib.pyplot as plt
    sigma = 1
    a = -5 * sigma
    b = 5 * sigma
    uniform_qf = functools.partial(uniform_qf, a=a, b=b)
    q_gen = functools.partial(q_gen, a=a, b=b)
    gen = accept_reject_sampling(normal_pf, uniform_qf, q_gen, M(a, b))

    rs = np.array([next(gen) for _ in range(10000)])
    plt.hist(rs, bins=100, density=True, label="sampling")

    x = np.linspace(np.min(rs), np.max(rs), len(rs))
    y1 = uniform_qf(x)
    y2 = normal_pf(x)
    plt.plot(x, y1 * M(a, b), label="reference distribution:uniform distribution")
    plt.plot(x, y2, label="object distribution:$N(0,1)$")
    plt.legend(loc="upper left")
    plt.show()


