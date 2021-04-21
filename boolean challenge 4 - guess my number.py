#boolean challenge 4 - guess my number app
import random

print("Welcome to the Guess My Number App")

#user name input
user_name = input("\nWhat is your name: ").title().strip()

print("Well " + str(user_name) + ", I am thinking of a number between 1 and 20.")

#random number generator
comp_num = random.randint(0, 20)
print(comp_num)

#guess attempts
for guesses in range(5):
    guess = int(input("\nTake a guess: "))
    if guess > comp_num:
        print("Your guess is too high")
    elif guess < comp_num:
        print("Your guess is too low")
    else:
        break

#outcomes
if guess == comp_num:
    print("Bingo, you guessed correctly in " + str(guesses + 1) + ".")
else:
    print("\nGame Over. The number I was thinking of was " + str(comp_num) + ".")


