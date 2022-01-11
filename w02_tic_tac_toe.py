
# Tic Tac Toe Game
# By Morgan Luke

# Love is a game of tic-tac-toe,
# Constantly waiting for the next x or o.
#    -Lang Leav -




def main():
    try:
        spaces= ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        index = 0

        print('Tic-Tac-Toe Game')
        display_game(spaces)

        while index != 9:
            player = players_turn(index)
            choice = prompt_player(player)
            verified_space = verify_space(choice, spaces, player)
            spaces[verified_space - 1] = player
            display_game(spaces)
            verify_win(spaces, player)
            index += 1

    except ValueError as val_err:
        # The user entered at least one character that is
        # not between 1-9 or was not an int value.
        print("Your selection is not possible.")
        print("Please enter a new number between 1-9.")

    except TypeError as type_err:
        # The user ented a number that was already selected
        print('That space was already selected')


def display_game(spaces):
    print(f'{spaces[0]} | {spaces[1]} | {spaces[2]}')
    print(f'- + - + -')
    print(f'{spaces[3]} | {spaces[4]} | {spaces[5]}')
    print(f'- + - + -')
    print(f'{spaces[6]} | {spaces[7]} | {spaces[8]}')


def players_turn(index):
    player = ''
    if index % 2 == 0:
        player = "X"
    else:
        player = "O"
    
    return player


def prompt_player(player):
    print()
    choice = int(input(f"{player}'s turn to choose a square (1-9): "))

    return choice


def verify_space(choice, spaces, player):
    if str(choice) in spaces:
        choice = int(choice)
    else:
        print('That space is already taken')
        print('Try again.')
        # choice = prompt_player(player)
        # verify_space(choice, spaces, player)



    return choice


def verify_win(spaces, player):
    # horizontal wins
    if spaces[0] == "X" and spaces[1] == 'X' and spaces[2] == 'X':
        print(f"{player}'s Won!")
        quit()
    elif spaces[3] == "X" and spaces[4] == 'X' and spaces[5] == 'X':
        print(f"{player}'s Won!")
        quit()
    elif spaces[6] == "X" and spaces[7] == 'X' and spaces[8] == 'X':
        print(f"{player}'s Won!")
        quit()
    elif spaces[0] == "O" and spaces[1] == 'O' and spaces[2] == 'O':
        print(f"{player}'s Won!")
        quit()
    elif spaces[3] == "O" and spaces[4] == 'O' and spaces[5] == 'O':
        print(f"{player}'s Won!")
        quit()
    elif spaces[6] == "O" and spaces[7] == 'O' and spaces[8] == 'O':
        print(f"{player}'s Won!")
        quit()
    # vertical wins
    elif spaces[0] == "X" and spaces[3] == 'X' and spaces[6] == 'X':
        print(f"{player}'s Won!")
        quit()
    elif spaces[1] == "X" and spaces[4] == 'X' and spaces[7] == 'X':
        print(f"{player}'s Won!")
        quit()
    elif spaces[2] == "X" and spaces[5] == 'X' and spaces[8] == 'X':
        print(f"{player}'s Won!")
        quit()
    elif spaces[0] == "O" and spaces[3] == 'O' and spaces[6] == 'O':
        print(f"{player}'s Won!")
        quit()
    elif spaces[1] == "O" and spaces[4] == 'O' and spaces[7] == 'O':
        print(f"{player}'s Won!")
        quit()
    elif spaces[2] == "O" and spaces[5] == 'O' and spaces[8] == 'O':
        print(f"{player}'s Won!")
        quit()
    # diagonal wins
    if spaces[0] == "X" and spaces[4] == 'X' and spaces[8] == 'X':
        print(f"{player}'s Won!")
        quit()
    elif spaces[2] == "X" and spaces[4] == 'X' and spaces[6] == 'X':
        print(f"{player}'s Won!")
        quit()
    elif spaces[0] == "O" and spaces[4] == 'O' and spaces[8] == 'O':
        print(f"{player}'s Won!")
        quit()
    elif spaces[2] == "O" and spaces[4] == 'O' and spaces[6] == 'O':
        print(f"{player}'s Won!")
        quit()



if __name__ == "__main__":
    main()