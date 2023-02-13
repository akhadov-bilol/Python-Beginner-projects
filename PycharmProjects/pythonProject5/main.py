import random

tosh = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

qogoz = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

qaychi = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = 0
paper = 1
scissors = 2
game_images = [tosh, qogoz, qaychi]
you = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors "))
if you > 2 or you < 0:
    print('Invalid input')
else:
    print(game_images[you])
    computer = random.randint(0, 2)
    print(game_images[computer])
    if you == 0 and computer == 2:
        print('You won')
    elif you == 1 and computer == 0:
        print('You won')
    elif you == 2 and computer == 1:
        print('You won')
    elif computer == 0 and you == 2:
        print('You lost')
    elif computer == 1 and you == 0:
        print('You lost')
    elif computer == 2 and you == 1:
        print('You lost')
    else:
        print('draw')

