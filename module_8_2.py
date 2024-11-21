def personal_sum(numbers):
  result = 0
  incorrect_data = 0
  for num in numbers:
    try:
      result += num
    except TypeError:
      incorrect_data += 1
      print(f'Некорректный тип данных - {num}')
  return result, incorrect_data

def calculate_average(numbers):

  try:
    total, incorrect_data = personal_sum(numbers)
    if incorrect_data == len(numbers):
      print("Все данные в коллекции не являются числами")
      return 0
    return total / (len(numbers) - incorrect_data)
  except TypeError:
    print("В numbers записан некорректный тип данных")
    return None
  except ZeroDivisionError:
    return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')