
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

numbers_in_interval = []

if 1 <= num1 <= 3:
    numbers_in_interval.append(num1)
if 1 <= num2 <= 3:
    numbers_in_interval.append(num2)
if 1 <= num3 <= 3:
    numbers_in_interval.append(num3)

print("Числа из интервала [1, 3]:", numbers_in_interval)

