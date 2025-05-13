

import random

print("Let's kill some time.\nPlaying the random number guessing game!")
print("\nYou will get five chances.\n")


def guess_number():
    secret_num = random.randint(1, 50)
    chances = 0
    max_chances = 5

    while chances < max_chances:
        try:
            guess = int(input(f"Chance {chances + 1}: Enter a number between 1 and 50: "))


            if guess == secret_num:
                print(f" Congrats! Number matched.\nThe number is {secret_num}")
                break
            elif guess > secret_num:
                print("Your number is greater than the secret number.")
            else:
                print("Your number is lesser than the secret number.")

        except ValueError:
            print(" Invalid input! Please enter a number.")

        chances += 1

    if chances == max_chances and guess != secret_num:
        print(f" No more chances left. The secret number was {secret_num}.")


guess_number()





