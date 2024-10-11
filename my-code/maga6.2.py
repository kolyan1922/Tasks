import random

array = [random.randint(0, 10) for _ in range(10)]

print("Исходный массив:", array)

new_array = []
for element in array:
    if element not in new_array:
        new_array.append(element)

print("Массив без дубликатов:", new_array)