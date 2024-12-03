import random

A = []
s = 10
chet = 0
nechet = 0

while s != 0:
    i = random.randint(20, 100)
    A.append(i)
    s -= 1

for j in A:
    if j % 2 == 0:
        chet = chet + 1
    else:
        nechet = nechet + 1

print(chet, nechet)
