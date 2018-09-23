"""A number-guessing game."""

import random

target = random.randint(1, 100)

name = input("Howdy, what's your name? ")
print("%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name)

tries = 0
while True:
    guess = int(input("Your guess? "))
    tries += 1
    if guess < target:
        print("Your guess is too low, try again.")
    elif guess > target:
        print("Your guess is too high, try again.")
    else:
        print("Well done, %s! You found my number in %d tries!" % (name, tries))
        break
