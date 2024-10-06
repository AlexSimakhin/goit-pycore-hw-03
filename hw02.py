import random

def get_numbers_ticket(min_val, max_val, quantity):
  # Перевіряємо, чи відповідають параметри заданим умовам
  if min_val < 1 or max_val > 1000 or quantity > (max_val - min_val + 1):
    return [] # Якщо параметри не відповідають вимогам, повертаємо порожній список
  
  # Генеруємо унікальний набір випадкових чисел у заданому діапазоні
  numbers = random.sample(range(min_val, max_val + 1), quantity)
  
  # Повертаємо відсортований список чисел
  return sorted(numbers)

print("Your lottery numbers #1:", get_numbers_ticket(1, 49, 6))
print("Your lottery numbers #2:", get_numbers_ticket(1, 1000, 50))
print("Your lottery numbers #3:", get_numbers_ticket(1, 1001, 50))
