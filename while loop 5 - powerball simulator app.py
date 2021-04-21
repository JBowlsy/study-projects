#while loop challenge

import random 

print("--------------------------Power-Ball Simulator------------------------")

#generatte how many white balls to choose from
white_balls = int(input("How many white-balls to draw from for the 5 winning numbers (Normally 69): "))
if white_balls < 5:
    white_balls == 5

#generate how many red balls to choose from
red_balls = int(input("How many red-balls to draw from for the Power-Ball (Normally 26): "))
if red_balls < 1:
    red_balls == 1

#calculate the odds
odds = 1
for i in range(5):
    odds *= white_balls - i
odds *= red_balls/120
print("You have a 1 in " + str(odds) + " chance of winning this lottery.")


#choose how many tickets to purchase
ticket_interval = int(input("How many tickets would you like to purchase: "))

print("\n-------------------Welcome to the Power-Ball-------------------")

#generate the white balls and the red ball/s
win_numbers = []
while len(win_numbers) < 5:
    w = random.randint(1, white_balls)
    if w not in win_numbers:
        win_numbers.append(w)
win_numbers.sort()

r = random.randint(1, red_balls)
win_numbers.append(r)

str_win_numbers = [str(i) for i in win_numbers]
print("\nThe winning numbers are: " + " ".join(str_win_numbers))
#OR for number in win_numbers:
    #print(str(number), end=" ")

input("Press 'Enter' to begin purchasing tickets!!!")

tickets_purchased = 0
buying = True
tickets_sold = []

while win_numbers not in tickets_sold and buying == True:
    lottery_numbers = []
    while len(lottery_numbers) < 5:
        white_chosen = random.randint(1, white_balls)
        if white_chosen not in lottery_numbers:
            lottery_numbers.append(white_chosen)
    lottery_numbers.sort()

    red_chosen = random.randint(1, red_balls)
    lottery_numbers.append(red_chosen)

    if lottery_numbers not in tickets_sold:
        tickets_purchased += 1
        tickets_sold.append(lottery_numbers)
        print(tickets_purchased)
        print(lottery_numbers)

    else:
        print("Losing ticket generated: disregard...")

    if tickets_purchased % ticket_interval == 0:
        print(str(tickets_purchased) + " tickets purchased so far with no winner.")
        choice = input("\n buy more tickets (y/n): ")
        if choice != "y":
            buying = False
            
if lottery_numbers == win_numbers:
    print("\nWinning ticket: ", end= ' ')
    for number in lottery_numbers:
        print(str(number), end = ' ')
    print("\nPurchased a total of " + str(tickets_purchased) + " tickets.")

else:
    print("\nYou bought " + str(tickets_purchased) + " tickets and still lost.")
    print("Better luck next time")
        

print("\nThankyou for playing the lottery")
    
    
    





    
    
