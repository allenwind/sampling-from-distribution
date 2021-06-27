import numpy as np

def accept_reject_sampling(pf, qf, q_gen, M):
    """
    pf:目标采样概率密度函数
    qf:参考分布概率密度函数
    q_gen:参考分布采样生成器
    M:使得pf(x)<=qf(x)*M，qf(x)*M称为pf(x)的包络函数
    """
    for x in q_gen()
        u = np.random.uniform()
        if u < pf(x) / (M * qf(x)):
            yield x

if __name__ == "__main__":
    pass



