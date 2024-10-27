def read_matrix_from_file(file_name):
    with open(file_name, 'r') as file:
        n, m = map(int, file.readline().split())
        matrix = [list(map(int, file.readline().split())) for _ in range(n)]
    return matrix, n, m

def write_matrix_to_file(file_name, matrix):
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

input_file = "Каширский_242_maga10_vvod.txt" 
output_file = "Каширский_242_maga10_vivod.txt"  

matrix, n, m = read_matrix_from_file(input_file)

print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(n):
    matrix[i].sort()

write_matrix_to_file(output_file, matrix)

print("\nОтсортированная матрица:")
for row in matrix:
    print(row)