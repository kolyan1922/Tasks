def nod(a, b):
  
  while b:
    a, b = b, a % b
  return a

def nok(a, b):

  return (a * b) // nod(a, b)

a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))

НОД = nod(a, b)
НОК = nok(a, b)

print(f"НОД({a}, {b}) = {НОД}")
print(f"НОК({a}, {b}) = {НОК}")