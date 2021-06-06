# 100 Days of Code
# DAY 014
# Created by eduardorabe
# Higher Lower Game


from art import logo, vs
from game_data import data
from random import choice
from subprocess import run

def game():
    score = 0
    wrong_answer = False

    artist_b = choice(data)

    print(logo)

    while not wrong_answer:
        artist_a = artist_b
        artist_b = choice(data)

        while artist_a == artist_b:
            artist_b = choice(data)

        print(f"Compare A: {artist_a['name']}, a {artist_a['description']}, from {artist_a['country']}.")
        print(vs)
        print(f"Against B: {artist_b['name']}, a {artist_b['description']}, from {artist_b['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if answer == 'A':
            if artist_a['follower_count'] > artist_b['follower_count']:
                score += 1
                run(["clear"])
                print(logo)
                print(f"You're right! Current score: {score}")
            else:
                wrong_answer = True
                run(["clear"])
                print(logo)
                print(f"Sorry, that's wrong. Final score {score}")
        elif answer == 'B':
            if artist_b['follower_count'] > artist_a['follower_count']:
                score += 1
                run(["clear"])
                print(logo)
                print(f"You're right! Current score: {score}")
            else:
                wrong_answer = True
                run(["clear"])
                print(logo)
                print(f"Sorry, that's wrong. Final score {score}")
        else:
            print(f"Sorry, that's wrong. Final score {score}")

game()

