#challenge 4 - tic tac toe

print("\nWelcome to Tic-Tac-Toe")

def tic_nums(char_list):
    """print a number board or tictactoe board"""
    print("\n\t   Tic-Tac-Toe")
    print("\t-----------------")
    print("\t|| " + char_list[0] + " || " + char_list[1] + " || " + char_list[2]  + " ||")
    print("\t|| " + char_list[3] + " || " + char_list[4] + " || " + char_list[5]  + " ||")
    print("\t|| " + char_list[6] + " || " + char_list[7] + " || " + char_list[8]  + " ||")
    print("\t-----------------")


def player_input(player, char_list):
    """get a players move until it is valid"""
    while True:
        choice = int(input(player + ": Where would you like to go (1-9): "))
#check if space is on the board
        if choice > 0 and choice < 10:
             if char_list[choice - 1] == "_":
                 return choice
             else:
                 print("This spot has already been taken")
        else:
            print("your chosen move is not a place on the board")

#put character on the board
def place_char_on_board(player, choice, char_list):
    """put the character on the board"""
    char_list[choice - 1] = player

def is_winner(player, char_list):
    """all of the possible winning combinations"""
    """Return a Bool statement"""
            #horizontal wins
    return((char_list[0] == player and char_list[1] == player and char_list[2] == player) or
           (char_list[3] == player and char_list[4] == player and char_list[5] == player) or
           (char_list[6] == player and char_list[7] == player and char_list[8] == player) or
            #vertical wins
           (char_list[0] == player and char_list[3] == player and char_list[6] == player) or
           (char_list[1] == player and char_list[4] == player and char_list[7] == player) or
           (char_list[2] == player and char_list[5] == player and char_list[8] == player) or
           #diagonal wins
           (char_list[0] == player and char_list[4] == player and char_list[8] == player) or
           (char_list[2] == player and char_list[4] == player and char_list[6] == player))

#main code
#the players and their characters
player_1 = "X"
player_2 = "O"

c_list = ["_"]*9
n_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#draw the boards
tic_nums(n_list)
tic_nums(c_list)

while True:
    #player 1 turn
    move = player_input(player_1, c_list)
    #put move on board
    place_char_on_board(player_1, move, c_list)
    #redraw boards
    tic_nums(n_list)
    tic_nums(c_list)
    #check for winner or a tie
    if is_winner(player_1, c_list):
        print("player 1 wins!")
        break
    elif "_" not in c_list:
        print("Tie game")
        break
    
    #player 2 turn
    move = player_input(player_2, c_list)
    #put move on board
    place_char_on_board(player_2, move, c_list)
    #redraw boards
    tic_nums(n_list)
    tic_nums(c_list)
    #check for winner or a tie
    if is_winner(player_2, c_list):
        print("player 2 wins!")
        break
    elif "_" not in c_list:
        print("Tie game")
        break
    









           







    
