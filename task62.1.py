a1 = int(input("Введите число a1: "))
d = int(input("Введите число d: "))
n = int(input("Введите число n: "))
progressive = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*progressive)
