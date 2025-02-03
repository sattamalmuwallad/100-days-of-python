from art import logo, vs
from game_data import data
import random


def f_data(format):
    format_name = format["name"]
    format_description = format["description"]
    format_country = format["country"]
    formated_data = print(f"{format_name}, a {format_description} , from: {format_country}")
    return formated_data


def check_answer(guess, Firstguess, Secondguess):
    if Firstguess > Secondguess:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game = True

while game:

    firstacc = random.choice(data)
    secondacc = random.choice(data)

    if firstacc == secondacc:
        secondacc = random.choice(data)

    print(f"The first account is: {firstacc["name"]}")
    print(vs)
    print(f"The second account is: {secondacc["name"]}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    firstacc_followers = firstacc["follower_count"]
    secondacc_followers = secondacc["follower_count"]

    correct = check_answer(guess, firstacc_followers, secondacc_followers)
    if correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game = False