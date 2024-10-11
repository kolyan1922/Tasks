def sum_of_cubes(n):
  
  sum = 0
  for i in range(1, n+1):
    sum += i**3
  return sum

n = int(input("Введите натуральное число n: "))

sum_cubes = sum_of_cubes(n)

print(f"Сумма кубов натуральных чисел от 1 до {n} равна: {sum_cubes}")
