def nod(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        a = a % b
    else:
        b = b % a
    return nod(a, b)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
