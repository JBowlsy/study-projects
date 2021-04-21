#boolean challenge 5 - rock paper scissors
import random

#INPUTS for name and round numbers
print("\t\tROCK, PAPER, SCISSORS")
name = input("\nEnter your name for the tournament: ").title().strip()
print("\nWelcome " + name + " to the Rock, Paper, Scissors game")

matches = int(input("\nHow many rounds would you like to play: "))


Player_score = 0
comp_score = 0

#random choice generator and cheat code
for match in range(matches):
    comp_choice = random.randint(0, 2)
    #if comp_choice == 0:
    #    print("\nRock")
    #elif comp_choice == 1:
    #    print("\nPaper")
    #else:
    #    print("\nScissors")
    print("\nRound " + str(match + 1))

     
#Outcome generator
    choice = input("\nTime to guess....rock, paper or scissors: ").title().strip()
    if choice == "Rock" and comp_choice == 1:
        print("\n\tComputer: paper")
        print("\tPlayer: rock")
        print("\tRock is covered by paper")
        print("\tComputer won")
        comp_score += 1
        print("\nPlayer: " + str(Player_score) + "\tComputer: " + str(comp_score))
    elif choice == "Rock" and comp_choice == 2:
        print("\n\tComputer: scissors")
        print("\tPlayer: rock")
        print("\tRock smashes scissors")
        print("\tPlayer won")
        Player_score += 1
        print("\nPlayer: " + str(Player_score) + "\tComputer: " + str(comp_score))
    elif choice == "Rock" and comp_choice == 0:
        print("\n\tComputer: rock")
        print("\tPlayer: rock")
        print("\tRock looks at the other Rock")
        print("\tTie match")
        print("\nPlayer: " + str(Player_score) + "\tComputer: " + str(comp_score))
    elif choice == "Paper" and comp_choice == 2:
        print("\n\tComputer: scissors")
        print("\tPlayer: paper")
        print("\tPaper is cut by scissors")
        print("\tComputer won")
        comp_score += 1
        print("\nPlayer: " + str(Player_score) + "\tComputer: " + str(comp_score))
    elif choice == "Paper" and comp_choice == 0:
        print("\n\tComputer: rock")
        print("\tPlayer: paper")
        print("\tPaper covers rock")
        print("\tPlayer won")
        Player_score += 1
        print("\nPlayer: " + str(Player_score) + "\tComputer: " + str(comp_score))
    elif choice == "Paper" and comp_choice == 1:
        print("\n\tComputer: paper")
        print("\tPlayer: paper")
        print("\tPaper flaps at Paper")
        print("\tTie match")
        print("\nPlayer: " + str(Player_score) + "\tComputer: " + str(comp_score))
    elif choice == "Scissors" and comp_choice == 0:
        print("\n\tComputer: rock")
        print("\tPlayer: scissors")
        print("\tScissors are smashed by Rock")
        print("\tComputer won")
        comp_score += 1
        print("\nPlayer: " + str(Player_score) + "\tComputer: " + str(comp_score))
    elif choice == "Scissors" and comp_choice == 1:
        print("\n\tComputer: paper")
        print("\tPlayer: scissors")
        print("\tScissors cut Paper")
        print("\tPlayer won")
        Player_score += 1
        print("\nPlayer: " + str(Player_score) + "\tComputer: " + str(comp_score))
    elif choice == "Scissors" and comp_choice == 2:
        print("\n\tComputer: scissors")
        print("\tPlayer: scissors")
        print("\tScissors snips at scissors")
        print("\tTie match")
        print("\nPlayer: " + str(Player_score) + "\tComputer: " + str(comp_score))
    else:
        print("\nInvalid selection, point to computer")
        comp_score += 1
        print("\nPlayer: " + str(Player_score) + "\tComputer: " + str(comp_score))
        

#Resulrs
print("Final Game Results")
print("\tRounds played: " + str(matches))
print("\tPlayed score: " + str(Player_score))
print("\tComputer score: " + str(comp_score))
if Player_score == comp_score:
    print("\n\tThis tournament ended in a draw, what a waste of time.")
elif Player_score > comp_score:
    print("\n\t" + name + " was the winner with " + str(Player_score) + " points! Well done")
else:
    print("\n\tThe Computer defeated you by " + str(comp_score) + " points to " + str(Player_score) + "! Go cry in shame")
    
