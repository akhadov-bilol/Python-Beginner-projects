current_age = input('Your current age: ')
years_left = 90 - int(current_age)
days_left = int(years_left) * 365
weeks = 365 // 7
weeks_left = int(weeks) * int(years_left)
months_left = int(years_left) * 12
print(f"You have {years_left} years, {months_left} months, {weeks_left} weeks, {days_left} days left to live")
