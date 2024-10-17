def find_max():

  def find_max_recursive():
   
    number = int(input())
    if number == 0:
      return 0
    else:
      return max(number, find_max_recursive())

  return find_max_recursive()

max_value = find_max()
print("Максимальное значение:", max_value)