import random

x = 2
a = [random.randint(0, 4) for i in range(100)]
indices = [i for i, y in enumerate(a) if y == x]
print(indices)
