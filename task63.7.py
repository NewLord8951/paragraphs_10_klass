import random

n = 6

array = []

for i in range(n):
    array.append(random.randint(1, 10))

print("Массив:")
print(*array)
