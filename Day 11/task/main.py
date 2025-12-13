import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
should_play = True

while should_play == True:
    game_over = False

    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    answer = "y"

    while answer == "y" and game_over == False:

        calculate_score(user_cards)
        calculate_score(computer_cards)

        if calculate_score(user_cards) == 0 or calculate_score(computer_cards) == 0:
            print(f"Your cards: {user_cards}, Total of {calculate_score(user_cards)}")
            print(f"Dealers cards: {computer_cards}, Total of {calculate_score(computer_cards)}\n")

            print("User wins. It's a blackjack")
            game_over = True
            should_play = input("Would you like to play again? Answer 'y' or 'n'").lower()
            if should_play == "y":
                should_play = True
            elif should_play == "n":
                should_play = False
            print("\n" * 100)
            print(art.logo)


        elif calculate_score(user_cards) > 21:
            print(f"Your cards: {user_cards}, Total of {calculate_score(user_cards)}")
            print(f"Dealers cards: {computer_cards}, Total of {calculate_score(computer_cards)}\n")

            print("You lose.")
            game_over = True
            should_play = input("Would you like to play again? Answer 'y' or 'n'").lower()
            if should_play == "y":
                should_play = True
            elif should_play == "n":
                should_play = False
            print("\n" * 100)
            print(art.logo)


        elif game_over == False:
            print(f"Your cards: {user_cards}, Total of {calculate_score(user_cards)}")
            answer = input("Do you want to draw another card? Answer 'y' or 'n'.\n").lower()
            if answer == "y":
                user_cards.append(deal_card())

    if game_over == False:
        while calculate_score(computer_cards) < 17:
            computer_cards.append(deal_card())

        if calculate_score(computer_cards) > 21:
            print(f"Your cards: {user_cards}, Total of {calculate_score(user_cards)}")
            print(f"Dealers cards: {computer_cards}, Total of {calculate_score(computer_cards)}\n")
            print("User wins")
            game_over = True
            should_play = input("Would you like to play again? Answer 'y' or 'n'").lower()
            if should_play == "y":
                should_play = True
            elif should_play == "n":
                should_play = False
            print("\n" * 100)
            print(art.logo)



        elif calculate_score(user_cards) > calculate_score(computer_cards):
            print(f"Your cards: {user_cards}, Total of {calculate_score(user_cards)}")
            print(f"Dealers cards: {computer_cards}, Total of {calculate_score(computer_cards)}\n")
            print("User wins.")
            game_over = True
            should_play = input("Would you like to play again? Answer 'y' or 'n'").lower()
            if should_play == "y":
                should_play = True
            elif should_play == "n":
                should_play = False
            print("\n" * 100)
            print(art.logo)


        elif calculate_score(user_cards) < calculate_score(computer_cards):
            print(f"Your cards: {user_cards}, Total of {calculate_score(user_cards)}")
            print(f"Dealers cards: {computer_cards}, Total of {calculate_score(computer_cards)}\n")
            print("Dealer wins")
            game_over = True
            should_play = input("Would you like to play again? Answer 'y' or 'n'").lower()
            if should_play == "y":
                should_play = True
            elif should_play == "n":
                should_play = False
            print("\n" * 100)
            print(art.logo)


        else:
            print(f"Your cards: {user_cards}, Total of {calculate_score(user_cards)}")
            print(f"Dealers cards: {computer_cards}, Total of {calculate_score(computer_cards)}\n")
            print("Draw")
            game_over = True
            should_play = input("Would you like to play again? Answer 'y' or 'n'").lower()
            if should_play == "y":
                should_play = True
            elif should_play == "n":
                should_play = False
            print("\n" * 100)
            print(art.logo)
