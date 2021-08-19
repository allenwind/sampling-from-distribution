import matplotlib.pyplot as plt
import numpy as np

# 随机向量正交-正太分布
k = 1000
rs = []
for _ in range(k):
    u1 = np.random.normal(0, 1/100, size=100)
    u2 = np.random.normal(0, 1/100, size=100)
    rs.append(np.sum(u1 * u2))
plt.hist(rs, bins=100)
plt.show()

# # 随机向量正交-均匀分布
k = 1000
rs = []
for _ in range(k):
    u1 = np.random.uniform(-1, 1, size=100)
    u2 = np.random.uniform(-1, 1, size=100)
    rs.append(np.sum(u1 * u2))
plt.hist(rs, bins=100)
plt.show()

# 随机矩阵正交-正太分布
n = 100
m = 200 # m > n， 特例 m = n
W = np.random.normal(loc=0, scale=np.sqrt(1/m), size=(m, n))
R = np.dot(W.T, W)
plt.imshow(R)
plt.colorbar()
plt.show()
print(np.square(R - np.eye(n)).mean())

# 随机矩阵正交-均匀分布
n = 100
m = 200 # m > n， 特例 m = n
a = np.sqrt(3/m)
W = np.random.uniform(-a, a, size=(m, n))
R = np.dot(W.T, W)
plt.imshow(R)
plt.colorbar()
plt.show()
print(np.square(R - np.eye(n)).mean())
