import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images = [rock, paper, scissors]
you = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors "))
if you > 2 or you < 0:
    print('invalid input')
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

