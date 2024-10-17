import math

def area_quadrilateral(a, b, c, d, diagonal):

  # Используем теорему косинусов для вычисления углов
  angle1 = math.acos(((a ** 2) + (diagonal ** 2) - (b ** 2)) / (2 * a * diagonal))
  angle2 = math.acos(((c ** 2) + (diagonal ** 2) - (d ** 2)) / (2 * c * diagonal))

  # Вычисляем площадь как сумму площадей двух треугольников
  area = (0.5 * a * diagonal * math.sin(angle1)) + (0.5 * c * diagonal * math.sin(angle2))
  return area

a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))
d = float(input("Введите длину четвертой стороны: "))
diagonal = float(input("Введите длину диагонали: "))

area = area_quadrilateral(a, b, c, d, diagonal)

print(f"Площадь четырехугольника: {area:.2f}")