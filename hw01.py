from datetime import datetime

def get_days_from_today(date) -> int:
  try:
    # Перетворюємо рядок з датою у формат "YYYY-MM-DD" на об'єкт дати
    given_date = datetime.strptime(date, "%Y-%m-%d").date()
    
    # Отримуємо поточну дату без часу
    current_date = datetime.today().date()
    
    # Обчислюємо різницю у днях між заданою датою і поточною
    return (current_date - given_date).days
  except ValueError:
    return 'Incorrect date format. Use the format "YYYY-MM-DD".'
      
print(get_days_from_today("2024-10-07"))
print(get_days_from_today("2024-10-06"))
print(get_days_from_today("2024-10-01"))
print(get_days_from_today("01-01-2025"))
print(get_days_from_today("2021-10-09"))

# У вимозі до задачі (2. ... Якщо задана дата пізніша за поточну, результат має бути від'ємним) 
# Суперечить прикладу, в якому майбутня дата результат невід'ємне число. Чи я вже заплутався з цими датами :D
# P.S. Побачив коммент у слаці (але я б зробив "return (given_date - current_date).days")