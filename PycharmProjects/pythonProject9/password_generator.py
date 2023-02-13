
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

selected_letters = []
for value in range(0, nr_letters):
    selected_letters.append(random.choice(letters))

selected_symbols = []
for value in range(0, nr_symbols):
    selected_symbols.append(random.choice(symbols))

selected_numbers = []
for value in range(0, nr_numbers):
    selected_numbers.append(random.choice(numbers))

password = selected_letters + selected_symbols + selected_numbers

hard_password = []
for value in range(0, len(password)):
    hard_password.append(random.choice(password))

generated_passport = " "
for item in hard_password:
    generated_passport += item + ''
print(f"Suggested strong password is {generated_passport}")









