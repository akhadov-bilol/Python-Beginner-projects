your_name = input("What is your name? ")
their_name = input("What is their name? ")
name1 = your_name.lower()
name2 = their_name.lower()
lovers = name1 + name2
lovers_count = 0
lovers_count += lovers.count('t')
lovers_count += lovers.count('r')
lovers_count += lovers.count('u')
lovers_count += lovers.count('e')

lovers_count1 = 0
lovers_count1 += lovers.count('l')
lovers_count1 += lovers.count('o')
lovers_count1 += lovers.count('v')
lovers_count1 += lovers.count('e')

total = str(lovers_count) + str(lovers_count1)
love_score = int(total)

if love_score < 10 or love_score > 90:
    print("You are like Cola and Mentos")
elif 40 < love_score < 50:
    print("You are alright together")
else:
    print(f"Your love score is {love_score}")
