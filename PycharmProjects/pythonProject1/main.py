total_bill = input("What was the total bill? $ ")
total_bill1 = float(total_bill)
tip = input("What percentage tip you wanna give? 10, 12, 15: ")
tip1 = total_bill1 * int(tip) / 100
new_total_bill = total_bill1 + tip1
people = input("How many people to split the bill? ")
people_to_split = int(people)
payment = new_total_bill / people_to_split
each_person_bill = round(payment, 2)
print(f"Each person should pay $ {each_person_bill}")


