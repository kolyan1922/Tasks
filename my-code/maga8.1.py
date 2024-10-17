import random

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matrix = [[random.randint(0, 10) for _ in range(m)] for _ in range(n)]

print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(n):
    matrix[i].sort()
    
print("\n Отсортированная матрица:")
for row in matrix:
    print(row)