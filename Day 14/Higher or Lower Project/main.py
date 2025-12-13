import art
import game_data
import random

score = 0
# Choose from the list of choices randomly
# Create two choice 'A' and 'B'

random_number = random.randint(0, 49)

decisionA = [
    {
            'name': 'null',
            'follower_count': -1,
            'description': 'null',
            'country' : 'null'
    }]
decisionA[0]['name'] = game_data.data[random_number]['name']
decisionA[0]['follower_count'] = game_data.data[random_number]['follower_count']
decisionA[0]['description'] = game_data.data[random_number]['description']
decisionA[0]['country'] = game_data.data[random_number]['country']

random_number = random.randint(0, 49)

decisionB = [
    {
            'name': 'null',
            'follower_count': -1,
            'description': 'null',
            'country': 'null'
    }]
decisionB[0]['name'] = game_data.data[random_number]['name']
decisionB[0]['follower_count'] = game_data.data[random_number]['follower_count']
decisionB[0]['description'] = game_data.data[random_number]['description']
decisionB[0]['country'] = game_data.data[random_number]['country']

while True:
    # Print on the screen

    print(100 * "\n")
    print(art.logo)
    print(f"Compare A: {decisionA[0]['name']}, {decisionA[0]['description']}, from {decisionA[0]['country']}\n")
    print(art.vs, "\n")
    print(f"Compare B: {decisionB[0]['name']}, {decisionB[0]['description']}, from {decisionB[0]['country']}\n")

    # Ask the user to make a decision

    user_ans = input("Who has more followers? Type 'A' or 'B': ").lower()

    # If the user is right:
    # Take the users choice and update the choices 'A' and 'B'
    # Compare the followers of them and if the b smaller generate new b
    # Put the user choice on 'A' and create a random choice from the list
    # Count the score of the user
    # If the user is wrong:
    # Finish the game and ask 'Do you want to play again?'
    # And put everything in a loop

    if decisionA[0]['follower_count'] < decisionB[0]['follower_count'] and user_ans == 'b':
        decisionA[0]['name'] = decisionB[0]['name']
        decisionA[0]['follower_count'] = decisionB[0]['follower_count']
        decisionA[0]['description'] = decisionB[0]['description']
        decisionA[0]['country'] = decisionB[0]['country']

        random_number = random.randint(0, 49)

        decisionB[0]['name'] = game_data.data[random_number]['name']
        decisionB[0]['follower_count'] = game_data.data[random_number]['follower_count']
        decisionB[0]['description'] = game_data.data[random_number]['description']
        decisionB[0]['country'] = game_data.data[random_number]['country']
        score += 1

    elif decisionA[0]['follower_count'] > decisionB[0]['follower_count'] and user_ans == 'a':

        random_number = random.randint(0, 49)

        decisionB[0]['name'] = game_data.data[random_number]['name']
        decisionB[0]['follower_count'] = game_data.data[random_number]['follower_count']
        decisionB[0]['description'] = game_data.data[random_number]['description']
        decisionB[0]['country'] = game_data.data[random_number]['country']
        score += 1

    else:
        print(100 * "\n")
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
