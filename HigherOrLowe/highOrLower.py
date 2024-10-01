from art import logo, vs
from game_data import data 
import random

print(logo)


def get_info(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return name, description, country


def choice_a_or_b(guess, account_a, account_b):
    if account_a > account_b:
        return guess == 'A'
    else:
        return guess == 'B'

score = 0
continue_playing = True
player_b = random.choice(data)

while continue_playing:
    player_a = player_b
    while player_a == player_b:  
        player_b = random.choice(data)

    print(f"Compare: {get_info(player_a)}")
    print(vs)
    print(f"Against: {get_info(player_b)}")

    guess = input("What is your guess? Type 'A' or 'B': ").upper()

    compare_followers_user1 = player_a["follower_count"]
    compare_followers_user2 = player_b["follower_count"]

    is_correct = choice_a_or_b(guess, compare_followers_user1, compare_followers_user2)
    if is_correct:
        score += 1
        print(f"You're right! You scored {score}.")
        continue 
    else:
        print(f"You're wrong! You scored {score}.")
        continue_playing = False

    option = input("Do you want to play again? Type 'Y' or 'N': ").upper()
    if option == "Y":
        continue_playing = True
    else:
        continue_playing = False