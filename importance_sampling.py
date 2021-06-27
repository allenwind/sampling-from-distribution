import numpy as np

def importance_sampling(f, pf, qf, q_gen, nums=10000):
    """重要性采样，用于计算复杂概率密度pf关于f的期望
    """
    x = np.array([next(q_gen) for _ in range(nums)])
    return f(x) * pf(x) / qf(x)
