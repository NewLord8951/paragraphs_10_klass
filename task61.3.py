g = []


def convert(b):
    if (b == 0):
        return g
    dig = b % 2
    g.append(dig)
    convert(b // 2)


a = int(input("Введите число: "))
convert(a)
g.reverse()
print("Двоичная форма числа:")
for i in g:
    print(i)
