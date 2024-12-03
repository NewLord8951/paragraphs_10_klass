a = input().split()
min1 = float(a)[0]
min2 = float(a)[0]
min3 = float(a)[0]
for i in range(len(a)):
    if float(a[i]) < min1:
        min3 = min2
        min2 = min1
        min1 = float(a[i])
    elif float(a[i]) < min2:
        min3 = min2
        min2 = float(a[i])
    elif float(a[i]) < min3:
        min3 = float(a[i])
print(min1)
print(min2)
print(min3)
