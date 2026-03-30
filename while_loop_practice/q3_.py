
# Question : Create a random number guessing game with python.

import random

num = random.randint(1,11)

tries = 1

while True:

    guess = int(input("Please guess a number btw 1 to 10 : "))

    if guess == num:
        print(f"Your Guess is Correct , Your guess in {tries} tries")
        tries += 1
        break

    elif guess > num:
        print(f"Go a little Lower , Your Tries = {tries}")
        tries += 1

    elif guess < num:
        print(f"Go a little Higher , Your Tries = {tries}")
        tries += 1
    
    else:
        print("Please guess between 1 to 10 ")





