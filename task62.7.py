from random import randint

lst = [randint(1000, 2000) for i in range(10)]
count = 0
for number in lst:
    if ((number % 100) // 10) % 2 == 0:
        count += 1
print(lst)
print(count)
