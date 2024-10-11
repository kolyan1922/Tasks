import random

array = [random.randint(-10, 10) for _ in range(10)]

print("Исходный массив:", array)

for i in range(len(array)-1):
    if array[i] < 0 and array[i + 1] < 0:
        print(f"Пара отрицательных чисел: {array[i]}, {array[i + 1]}")