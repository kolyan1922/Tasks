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

print("\nНовая матрица:")
for row in new_matrix:
    print(row)

write_matrix_to_file(output_file, new_matrix)