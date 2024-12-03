from random import randint

a = [randint(-100, 100) for _ in range(15)]
print(a)

k = 5
m = 10
a = a[:k] + a[m:k-1:-1] + a[m+1:]
print(a)
