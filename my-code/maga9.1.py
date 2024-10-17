def print_digits_reversed(n):
  if n > 0:
    print(n % 10, end="   ")  
    print_digits_reversed(n // 10)  

n = int(input("Введите натуральное число: "))

print_digits_reversed(n)