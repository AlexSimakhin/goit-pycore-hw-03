from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
  today = datetime.today().date()
  upcoming_birthdays = []
  
  for user in users:
    # Перетворюємо дату народження в об'єкт datetime
    birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
    
    # Отримуємо день народження в поточному році
    birthday_this_year = birthday.replace(year=today.year)
    
    # Якщо день народження вже минув цього року, перевіряємо наступний рік
    if birthday_this_year < today:
      birthday_this_year = birthday_this_year.replace(year=today.year + 1)
    
    # Перевіряємо, чи знаходиться день народження в межах наступного тижня
    days_until_birthday = (birthday_this_year - today).days
    
    if 0 <= days_until_birthday <= 7:
      congratulation_date = birthday_this_year
      
      # Переносимо на наступний понеділок, якщо день народження - вихідний
      if congratulation_date.weekday() == 5:  # Субота
        congratulation_date += timedelta(days=2)
      elif congratulation_date.weekday() == 6:  # Неділя
        congratulation_date += timedelta(days=1)

      # Додаємо до списку
      upcoming_birthdays.append({
        "name": user["name"],
        "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
      })
  
  return upcoming_birthdays

users = [
  {"name": "John Doe", "birthday": "1991.01.01"},
  {"name": "John Smith", "birthday": "1992.10.05"},
  {"name": "John Johnson", "birthday": "1993.10.06"},
  {"name": "John Brown", "birthday": "1994.10.07"},
  {"name": "John Yellow", "birthday": "1995.10.08"},
  {"name": "John Saturday", "birthday": "1996.10.12"},
  {"name": "John Sunday", "birthday": "1997.10.13"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("This week's greetings list:", upcoming_birthdays)
