import random

#################################################################################
# Made by: Paul Ged
# Game: Tic Tac Toe with a AI opponent randomly choosing positions on the board
#################################################################################

# ASCII art empty board fo Tic Tac Toe
board = r'''
    a     b     c
      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     '''

# a dictionary which has the empty positions in the grid
board_matrix = {'a': {'1': 41, '2': 98, '3': 155},
                'b': {'1': 47, '2': 104, '3': 161},
                'c': {'1': 53, '2': 110, '3': 167}}

# resets the board and the board positions in the grid
def reset():
    global board
    global board_matrix
    board = r'''
    a     b     c
      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     '''

    board_matrix = {'a': {'1': 41, '2': 98, '3': 155},
                    'b': {'1': 47, '2': 104, '3': 161},
                    'c': {'1': 53, '2': 110, '3': 167}}
    print(board)

# validates if the number and letter entered by user is valid or not
def validator(letter, number):
    if not board_matrix[letter][number]:
        return False
    else:
        return True

# AI randomly generating a position on board and checks if the position is taken or not
def ai_validator():
    letter = random.choice(['a', 'b', 'c'])
    number = random.choice(['1', '2', '3'])
    position = []
    if board_matrix[letter][number] == False:
        return False
    else:
        position.append(letter)
        position.append(number)
        return position

# Initial console print of the board and variable declarations
print(board)
# counts the number of moves taken by user
counter = 0
# declaration of 'yes' to start game
declare = 'yes'

# game loop operating when there's less than 5 moves and if the user wants to play again
while declare != 'no':
    declare = input('Enter a position e.g. a1: ')
    parse = list(declare)
    board = list(board)
    # in case user doesn't enter position in the correct format they want
    try:
        # uses the validator function to check if the position is empty
        if validator(parse[0], parse[1]):
            # adds an 'X' to the board
            board[board_matrix[parse[0]][parse[1]]], board_matrix[parse[0]][parse[1]] = 'X', False
            AI_pos = ai_validator()
            # checks to see if the user has less than 5 moves and if the AI generated position is empty or not
            while not AI_pos and counter != 4:
                AI_pos = ai_validator()
            # tries to put a valid position for the AI if there's less than 5 moves and correct position is generated
            try:
                letter = AI_pos[0]
                number = AI_pos[1]
                board[board_matrix[letter][number]], board_matrix[letter][number] = 'O', False
            # if the AI has an invalid position, their position isn't added to the board
            except TypeError:
                pass
            board = ''.join(board)
            print(board)
        # if the user position fails the validators, error message pops up
        else:
            print(f'{declare} has already been played')
        counter += 1
        # if counter is 5, ask the user if they want to play again or not, resets the board, matrix and counter
        if counter == 5:
            declare = input('New Game? yes or no: ')
            if declare == 'yes':
                reset()
                counter = 0
    # this error pops up when the user enters a value which doesn't have the correct dict key in the matrix
    except KeyError:
        print(f'''This Position doesn't exist: {declare}''')
    # this error pops up when the user didn't type in enough characters for the program to recognise the position
    except IndexError:
        print(f'''You didn't type in enough characters for the Position''')
