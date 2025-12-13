import random

print("Welcome to the number guessing game!")

check = True
guess_limit = 0

ans = input("I'm thinking of a number between 1 and 100. \nChoose a difficulty. Type 'easy' or 'hard':").lower()
while check:

    if ans == "easy":
        guess_limit = 10
        check = False
    elif ans == "hard":
        guess_limit = 5
        check = False
    else:
        print("Check your spelling.")
        ans = input("Type 'easy' or 'hard':\n")
        check = True

def increase(num):
    return num + 1

def decrease(num):
    return num - 1

play = True
target_num = random.randint(0, 100)

print(f"\nNumber to be guessed is {target_num}\n")
guessed_number = []

while play:
    ans = int(input(f"You have {guess_limit} attempts remaining to guess the number.\nMake a guess."))

    guessed_number.append(ans)

    if guess_limit == 0:
        play = False
        print("\nYou've exceeded your guess number.")
        break

    guess_limit = decrease(guess_limit)

    if ans < 0 and ans > 100:
        print("It should be between 0 and 100. Guess again, you didn't lose anything\n")
        guess_limit = increase(guess_limit)

    if ans < target_num:
        print("Too low.\n")
    elif ans > target_num:
        print("Too high.\n")
    elif ans == target_num:
        print("Congratulations!!! That was my guess!\n")
        play = False

    """if ans in guessed_number:
        print("well... That was embarrassing. pfft. What was that??? Loser. I won't decrease your guess limit, try again.")
        guess_limit = increase(guess_limit)"""

