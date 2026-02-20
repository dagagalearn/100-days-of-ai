# Guessing Game: Dagaga A. , Feb 20
import random

name = input("name: ")
print(f"hello {name}, welcome to guessing number game\nRules: \n\t1. Guess from 1 to 10 inclusive\n\t2. After 5 attempts you lose")

tries = 0
rand_number = random.randint(1, 10)

while True:
    cmd = int(input("Enter a number between 1 and 10 inclusive: "))
    tries += 1

    if cmd == rand_number:
        print(f"You won! after {tries} tries!")
        break
    elif cmd > rand_number:
        print("Try lower numbers")
    else:
        print("Try larger numbers")

    if tries >= 5:
        print("You lose!")
        print(f"The number was {rand_number}")
        break
    else:
        print(f"You have {5 - tries} tries left")
