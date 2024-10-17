import random

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matrix = [[random.randint(2, 10) for _ in range(m)] for _ in range(n)]

print("Исходная матрица:")
for row in matrix:
    print(row)

new_matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    row = matrix[i]  
    min_element = min(row)
    min_index = row.index(min_element)

    for j in range(m):  
      new_matrix[i][j] = row[j]


    if min_element % 2 == 0:
        new_matrix[i][min_index] = 0
    else:
        new_matrix[i][min_index] = 1



# Выводим новую матрицу
print("\nНовая матрица:")
for row in new_matrix:
    print(row)