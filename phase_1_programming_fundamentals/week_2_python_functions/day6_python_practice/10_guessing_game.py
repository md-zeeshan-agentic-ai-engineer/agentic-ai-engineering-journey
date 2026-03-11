# 10. Number guessing game

import random

def number_guessing_game():
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess number (1- 100): "))
        attempts += 1

        if guess == secret:
            print("Correct! Attempts: ", attempts)
            break
        elif guess < secret:
            print("Too low")
        else:
            print("Too high")

number_guessing_game()