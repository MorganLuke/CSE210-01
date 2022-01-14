
# Tic Tac Toe Game
# By Morgan Luke

# Love is a game of tic-tac-toe,
# Constantly waiting for the next x or o.
#    -Lang Leav -


def main():
    try:
        # creates list for all 9 game spaces
        spaces= ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        index = 0
        win = False
        print('Tic-Tac-Toe Game')
        # displays the inital gameboard
        display_game(spaces)

        # loops through game until a win or a draw are determined. 
        while index != 9 and win == False:
            # determines whos turn it is. Startes with X.
            player = players_turn(index)
            # prompts player for which space thy want
            choice = prompt_player(player)
            # takes user choice and verifies that space is avilable
            # if space is not available it will prompt them for a new one
            verified_space = verify_space(choice, spaces, player)
            # when a verified space is returned it is then added to the spaces list
            spaces[verified_space - 1] = player
            # the new gameboard with player's coice is now displayed
            display_game(spaces)
            # the list is checked to see if a win is present and returns True or False
            win = verify_win(spaces, player, win)
            # Index increments to keep track of length of game
            index += 1

        # determines that if there isnt a win after all spaces are filled
        # then prints it is a draw
        if win == False:
            print('The game is a draw!')


    except ValueError as val_err:
        # The user entered at least one character that is
        # not between 1-9 or was not an int value.
        print("You entered an incorrect charachter")
        print("Please play again")


def display_game(spaces):
    """Prints the list "spaces" in a gameboard pattern of tic tac toe
    Parameter
        spaces: list of space numbers and player selections
    Return: nothing
    """
    # prints the game board from spaces list
    print(f'{spaces[0]} | {spaces[1]} | {spaces[2]}')
    print(f'- + - + -')
    print(f'{spaces[3]} | {spaces[4]} | {spaces[5]}')
    print(f'- + - + -')
    print(f'{spaces[6]} | {spaces[7]} | {spaces[8]}')


def players_turn(index):
    """Determines based off of index of game play location
    which players turn it is.
    Parameter
        index: location of game play
    Return: player
    """
    player = ''
    # divides the index by 2 and determines is there is a remainder
    # if the remainder is 0 it, is x's turn
    if index % 2 == 0:
        player = "X"
    else:
        # if the remainder is 1, it is o's turn
        player = "O"
    
    return player


def prompt_player(player):
    """Prompts player for a space selection. 
    Parameter
        player: player whos turn it is
    Return: choice
    """
    print()
    # promps player for a selection
    choice = int(input(f"{player}'s turn to choose a square (1-9): "))

    return choice


def verify_space(choice, spaces, player):
    """Determines if the players choice is in the "spaces" list.
    if it isnt then it displays an error message and re prompts
    the player for a new selection and then re verifies. It will keep
    looping until an available space is given. 
    Parameter
        choice: players game space choice
        spaces: list of space numbers and player selections
        player: player whos turn it is
    Return: choice
    """
    # checks the spaces list to see if choice is in it
    if str(choice) in spaces:
        # converts choice to an integer for later index use
        choice = int(choice)
    else:
        print()
        # prints error if same space or wrong number entered
        print('Try again.')
        # displays the the gameboard
        display_game(spaces)
        #  prompts player for a new choice
        choice = prompt_player(player)
        # verifies the new choice
        choice = verify_space(choice, spaces, player)

    return choice


def verify_win(spaces, player, win):
    """Determines if there is a win for any player on a row, column
    or diagonal. Displays that player if won. 
    Parameter
        spaces: list of space numbers and player selections
        player: player whos turn it is
        win: value to trigger a win
    Return: win
    """
    # determines and prints a horizontal win
    if spaces[0] == "X" and spaces[1] == 'X' and spaces[2] == 'X':
        print(f"{player}'s Won!")
        win = True
    elif spaces[3] == "X" and spaces[4] == 'X' and spaces[5] == 'X':
        print(f"{player}'s Won!")
        win = True
    elif spaces[6] == "X" and spaces[7] == 'X' and spaces[8] == 'X':
        print(f"{player}'s Won!")
        win = True
    elif spaces[0] == "O" and spaces[1] == 'O' and spaces[2] == 'O':
        print(f"{player}'s Won!")
        win = True
    elif spaces[3] == "O" and spaces[4] == 'O' and spaces[5] == 'O':
        print(f"{player}'s Won!")
        win = True
    elif spaces[6] == "O" and spaces[7] == 'O' and spaces[8] == 'O':
        print(f"{player}'s Won!")
        win = True
    # determines and prints a vertical win
    elif spaces[0] == "X" and spaces[3] == 'X' and spaces[6] == 'X':
        print(f"{player}'s Won!")
        win = True
    elif spaces[1] == "X" and spaces[4] == 'X' and spaces[7] == 'X':
        print(f"{player}'s Won!")
        win = True
    elif spaces[2] == "X" and spaces[5] == 'X' and spaces[8] == 'X':
        print(f"{player}'s Won!")
        quit()
    elif spaces[0] == "O" and spaces[3] == 'O' and spaces[6] == 'O':
        print(f"{player}'s Won!")
        win = True
    elif spaces[1] == "O" and spaces[4] == 'O' and spaces[7] == 'O':
        print(f"{player}'s Won!")
        win = True
    elif spaces[2] == "O" and spaces[5] == 'O' and spaces[8] == 'O':
        print(f"{player}'s Won!")
        quit()
    # determines and prints a diagonal win
    if spaces[0] == "X" and spaces[4] == 'X' and spaces[8] == 'X':
        print(f"{player}'s Won!")
        win = True
    elif spaces[2] == "X" and spaces[4] == 'X' and spaces[6] == 'X':
        print(f"{player}'s Won!")
        win = True
    elif spaces[0] == "O" and spaces[4] == 'O' and spaces[8] == 'O':
        print(f"{player}'s Won!")
        win = True
    elif spaces[2] == "O" and spaces[4] == 'O' and spaces[6] == 'O':
        print(f"{player}'s Won!")
        win = True

    return win


if __name__ == "__main__":
    main()