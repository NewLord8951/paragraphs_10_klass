import random

n = int(input("Введите количество элементов в массиве: "))

arr = [random.randint(1, 100) for i in range(n)]
print("Исходный массив: ", arr)

if n % 2 != 0:
    mid = arr[n // 2]
    left_arr = arr[:n // 2]
    right_arr = arr[n // 2 + 1:]
else:
    left_arr = arr[:n // 2]
    right_arr = arr[n // 2:]

for i in range(len(left_arr)):
    for j in range(len(left_arr) - 1 - i):
        if left_arr[j] > left_arr[j + 1]:
            left_arr[j], left_arr[j + 1] = left_arr[j + 1], left_arr[j]

for i in range(len(right_arr)):
    min_idx = i
    for j in range(i + 1, len(right_arr)):
        if right_arr[j] > right_arr[min_idx]:
            min_idx = j
        right_arr[i], right_arr[min_idx] = right_arr[min_idx], right_arr[i]

if n % 2 != 0:
    arr = left_arr + [mid] + right_arr
else:
    arr = left_arr + right_arr

print("Отсортированный массив: ", arr)
