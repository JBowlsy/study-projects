#Guess the word APP
import random 

print("\nWelcome to the Guess my word APP")

#dictionaries of categories
game_dict = {
"sports":["football", "rugby", "tennis", "bowling", "swimming", "climbing",],
"fruits":["apple", "melon", "strawberry", "orange", "banana", "pear"],
"instruments":["piano", "guitar", "drums", "voice", "triangle", "trumpet"],
"drinks":["water", "beer", "cola", "juice", "milkshake", "wine"],
}

game_keys = []
for keys in game_dict.keys():
    game_keys.append(keys)

#randomly choose a category and word from category
playing = True
while playing:
    game_cat = random.choice(game_keys)
    game_word = random.choice(game_dict[game_cat])
    
#give clue based on selected word
    print("\nGuess a " + str(len(game_word)) + " letter word from the following category: " + str(game_cat).title())
    blank_word = []
    for i in game_word:
        blank_word.append("-")
       

    guess = ""
    guess_count = 0

#increase count score
    while guess != game_word:
        print("".join(blank_word))
        guess = input("\nEnter your guess: ").lower()
        guess_count += 1
        print(guess_count)

#finish correct game
        if guess == game_word:
            print("Well done, you guessed the word in " + str(guess_count) + " attempts.")
            break
        
#replace letters
        else:
            print("That was incorrect, here is a clue to help")
            swapping = True
            while swapping:
                letter_index = random.randint(0, len(game_word)-1)
                if blank_word[letter_index] == "-":
                    blank_word[letter_index] = game_word[letter_index]
                    swapping = False
            
#play again?
    again = input("Would you like to play again (y/n): ").lower()
    if again == "n":
         break
print("\Thanks for playing")
            
    
        






