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

def laplace_qf(x, b):
    return np.exp(-np.abs(x) / b) / (2 * b)

def normal_pf(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(- np.square(x) / 2)

def q_gen(b):
    while True:
        yield np.random.laplace(scale=1/b)

def M(b):
    return 2 * b * np.exp(1 / (2 * np.square(b))) / np.sqrt(2 * np.pi)

if __name__ == "__main__":
    # 这里使用Laplace分布作为参考分布，采样正太分布
    import matplotlib.pyplot as plt
    b = 1
    laplace_qf = functools.partial(laplace_qf, b=b)
    q_gen = functools.partial(q_gen, b=b)
    gen = accept_reject_sampling(normal_pf, laplace_qf, q_gen, M(b))

    rs = np.array([next(gen) for _ in range(10000)])
    plt.hist(rs, bins=100, density=True, label="sampling")

    x = np.linspace(np.min(rs), np.max(rs), len(rs))
    y1 = laplace_qf(x)
    y2 = normal_pf(x)
    plt.plot(x, y1 * M(b), label="reference distribution:Laplace distribution")
    plt.plot(x, y2, label="object distribution:$N(0,1)$")
    plt.legend(loc="upper left")
    plt.show()


