import numpy as np
import matplotlib.pyplot as plt

def nrand():
    while True:
        u1 = np.random.uniform(size=1)
        u2 = np.random.uniform(size=1)

        if np.sqrt(u1**2 + u2**2) <= 1:
            break

    n1 = np.sqrt(-0.5*np.log(u1)) * u1 / np.sqrt(u1**2 + u2**2)
    n2 = np.sqrt(-0.5*np.log(u1)) * u2 / np.sqrt(u1**2 + u2**2)
    return n1, n2

rs = []

for _ in range(10000):
    n1, n2 = nrand()
    rs.append(n1)

plt.subplot(211)
plt.plot(rs)
plt.subplot(212)
plt.hist(np.array(rs), bins=100)
plt.show()
