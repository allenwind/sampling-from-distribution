import numpy as np

def shuffle(x):
    size = len(x)
    for i in range(size-2):
        j = i + np.random.randint(0, size-i)
        x[i], x[j] = x[j], x[i]

x = np.arange(20)
print(x)
shuffle(x)
print(x)
