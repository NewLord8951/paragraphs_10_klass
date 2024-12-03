import random

a = [random.randint(1, 100) for i in range(100)]

b = sum([a[i*2:i*2+2][::-1] for i in range((len(a)+1)//2)],)

print(a)
print(b)
