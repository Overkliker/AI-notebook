import numpy as np
import random

h = np.random.uniform(low=-100, high=100, size=(3, 6))

print(h)
print(type(h))


print(h[1 - 1:2 + 2, 3-1:3 + 1])
print()
print(h[2 - 1:2 + 1, 3-1:3 + 1])
print()
print(h[2 - 1:2, 3-1:3 + 1])