size = input('What size do you want? S, M,  or L ')
add_peperoni = input('Dou you want peperoni? Y or N ')
extra_cheese = input('Do you want cheese? Y or N ')
price = 0
if size == 'S':
    price = 15
    if add_peperoni == 'Y':
        print('Adding peperoni')
        price += 2

    if extra_cheese == 'Y':
        print('Adding extra cheese')
        price += 1

if size == 'M':
    price = 20
    if add_peperoni == 'Y':
        price += 3

    if extra_cheese == 'Y':
        price += 1

if size == 'L':
    price = 25
    if add_peperoni == 'Y':
        price += 3

    if extra_cheese == 'Y':
        price += 1

print(f"Your bill is $ {price}")
