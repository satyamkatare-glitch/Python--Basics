
# Question : Create a random number guessing game with python.

import random

num = random.randint(1,11)

tries = 0

while True:

    guess = int(input("Please guess a number btw 1 to 10 : "))

    if guess == num:
        tries += 1
        print(f"Your Guess is Correct , Your guess in {tries} tries")
        break

    elif guess > num:
        tries += 1
        print(f"Go a little Lower , Your Tries = {tries}")

    elif guess < num:
        tries += 1
        print(f"Go a little Higher , Your Tries = {tries}")
    
    else:
        print("Please guess between 1 to 10 ")





