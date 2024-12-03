import random

lst = [random.randint(0, 100) for _ in range(random.randint(1, 100))]
lst1 = [i for i in lst if i < 50]
lst2 = [i for i in lst if i >= 50]
print(sum(lst1) / len(lst1))
print(sum(lst2) / len(lst2))
