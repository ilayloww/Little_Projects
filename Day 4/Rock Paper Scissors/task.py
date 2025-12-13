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
rand_num = random.randint(0, 2)
if rand_num == 0:
    print(rock)
elif rand_num == 1:
    print(paper)
elif rand_num == 2:
    print(scissors)

user = input("rock, paper, scissors?").lower()

if (user == "rock") and (rand_num == 0):
    print(f"Your choice: \n{rock}")
    print(f"My choice: \n{rock}")
    print("Try again, it's a draw.")
elif (user == "rock") and (rand_num == 1):
    print(f"Your choice: \n{rock}")
    print(f"My choice: \n{paper}")
    print("You lost.")
elif (user == "rock") and (rand_num == 2):
    print(f"Your choice: \n{rock}")
    print(f"My choice: \n{scissors}")
    print("You win!")


if (user == "paper") and (rand_num == 0):
    print(f"Your choice: \n{paper}")
    print(f"My choice: \n{rock}")
    print("You win!")
elif (user == "paper") and (rand_num == 1):
    print(f"Your choice: \n{paper}")
    print(f"My choice: \n{paper}")
    print("Try again, it's a draw.")
elif (user == "paper") and (rand_num == 2):
    print(f"Your choice: \n{paper}")
    print(f"My choice: \n{scissors}")
    print("You lost.")


if (user == "scissors") and (rand_num == 0):
    print(f"Your choice: \n{scissors}")
    print(f"My choice: \n{rock}")
    print("You lost.")
elif (user == "scissors") and (rand_num == 1):
    print(f"Your choice: \n{scissors}")
    print(f"My choice: \n{paper}")
    print("You win!")
elif (user == "scissors") and (rand_num == 2):
    print(f"Your choice: \n{scissors}")
    print(f"My choice: \n{scissors}")
    print("Try again, it's a draw.")