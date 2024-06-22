"""
@author: H24111057 統計系 姚博瀚
"""

import random
import time

def initialize_game():
    global board, board2, rows, cols, mines_coordinate

    # Initialize the game board and mines' board as dictionaries
    board = {(row, col): ' ' for row in range(1, 10) for col in range(1, 10)}
    board2 = {(row, col): 0 for row in range(1, 10) for col in range(1, 10)}

    # Set the number of rows and columns
    rows = 9
    cols = 9
    
def generate_mines_coordinates():
    global mines_coordinate
    # Generate 10 unique bomb coordinates in (1, 1)~(9, 9)
    while True:
        mines_coordinate = [(random.randint(1, 9), random.randint(1, 9)) for _ in range(10)]
        mines_coordinate.sort()

        # Check if the coordinates are unique by using set()'s characteristic which do not contain duplicate item
        # and exit the loop
        if len(set(mines_coordinate)) == len(mines_coordinate):
            break

    # Place mines on the mines' board (board2) and increase adjacent cell values
    for x, y in mines_coordinate:
        board2[(x, y)] = -1
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 1 <= x + dx <= 9 and 1 <= y + dy <= 9 and board2[(x + dx, y + dy)] != -1:
                    board2[(x + dx, y + dy)] += 1

# Modify the game board with the given symbol
def modify_board(row, col, symbol):
    board[(row, col)] = symbol

# Print the game board
def print_board(count):
    print("\n    a   b   c   d   e   f   g   h   i", end="")
    for x in range(1, rows + 1):
        print("\n  +---+---+---+---+---+---+---+---+---+")
        print(x, "|", end="")
        for y in range(1, cols + 1):
            if count == 0:
                print(" ", board[(x, y)], end="|")
            else:
                print("", board[(x, y)], end=" |")
    print("\n  +---+---+---+---+---+---+---+---+---+")

# Reveal the cell on the game board recursively if it's empty 
# and stops when it encounters cells adjacent to mines
def reveal_board(row, col):
    # the cell has either already been revealed or is flagged
    if board[(row, col)] != ' ':
        # exit the function reveal_board(row, col)
        return
    
    board[(row, col)] = str(board2[(row, col)])

    # no adjacent mines
    if board2[(row, col)] == 0:
        # calls itself recursively for all neighboring cells
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (1 <= row + dx <= 9) and (1 <= col + dy <= 9):
                    reveal_board(row + dx, col + dy)

def the_cell_to_reveal_is_flagged(row, col):
    if board[(row, col)] == 'F':
        return True
    
def the_cell_to_reveal_is_revealed(row, col):
    if board[(row, col)] in '012345678':
        return True
    
def the_cell_to_flag_is_revealed(row, col):
    if board[(row, col)] in '012345678':
        return True

# Check if the game is won
# should return True when all non-mine cells are revealed and all mines are flagged
def is_game_won():
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            if (board[(row, col)] == ' ' and board2[(row, col)] != -1) or (board[(row, col)] != 'F' and board2[(row, col)] == -1):
                return False
    return True

def play_again():
    while True:
        try:
            ask = input("Play again? (y/n): ")
            if ask.lower() in ['y','yes']:
                return True
            elif ask.lower() in ['n','no','q', 'quit']:
                return False
            else:
                raise ValueError
        except ValueError:
            print("Invalid input! Enter again.")
            continue

# determine whether the first action's coordinate is in mines' coordinates
def determine_first_action_in_mines_coordinate(action):
    col = 'abcdefghi'.index(action[0]) + 1
    row = int(action[1])
    if (row, col) in mines_coordinate:
        return True
    else:
        return False
    
# Main function to play the game
def play_game():
    while True:
        initialize_game()
        generate_mines_coordinates()
        
        # track whether the user wants to quit the game
        quit_game = False
        
        # initialize the times of input
        count = 0
        # initialize the number of flagged bombs
        num_flaggedbombs = 0
        
        print_board(count)
        print("Welcome to Minesweeper!")
        print("\nEnter the column followed by the row (ex: a1).To add or remove a flag,\nadd 'f' to the cell (ex:a5f). Type 'help' to show this message again.")
        
        # set start time
        start_time = time.time()
        
        while True:
            try:
                print()
                # Get user input for the move
                action = str(input("Enter the cell (%d mines left): "%(10 - num_flaggedbombs)))
                
                if action.lower() == 'q':
                    quit_game = True
                    break
                
                # keep the first action's coordinate do not in the generated mines' coordinate
                while determine_first_action_in_mines_coordinate(action) is True and count == 0:
                    generate_mines_coordinates()
                                
                if action.lower() == 'help':
                    print("\nEnter the column followed by the row (ex: a1).To add or remove a flag,\nadd 'f' to the cell (ex:a5f). Type 'help' to show this message again.")
                    continue
                        
                # add 'r' at the end of action if the input's length is 2 and aiming to reveal the cell
                if (len(action) == 2 and 
                    action[0] in 'abcdefghi' and 
                    (1 <= int(action[1]) <= 9)):
                    action = action + 'r'
                        
                # Validate the input and raise an error if it is invalid
                if (len(action) != 3 
                    or action[2] not in ['r', 'f'] 
                    or action[0] not in 'abcdefghi' 
                    or not (1 <= int(action[1]) <= 9)):
                    raise ValueError
                
                # Convert the input into row, column, and action
                row = int(action[1])
                col = 'abcdefghi'.index(action[0]) + 1
                symbol = 'F' if action[2].upper() == 'F' else board2[(row, col)]
                
                # add 1 into count after a round
                count += 1
                
                # the action is to reveal a cell
                if action[2] == 'r':
                    # Check if the cell to reveal is already flagged or revealed
                    if the_cell_to_reveal_is_flagged(row, col):
                        print("There is a flag!")
                        continue
                    elif the_cell_to_reveal_is_revealed(row, col):
                        print("That cell is already shown!")
                        continue
                    
                    # If the cell contains a mine
                    if symbol == -1:
                        print()
                        print("Game over!")

                        # Show all mines on the board and print the final board
                        for x, y in mines_coordinate:
                            modify_board(x, y, 'X')
                        print_board(count)
                        print()
                        break
                    # If the cell do not contain a mine (symbol = board2[row][col] != -1)
                    else:
                        # Reveal the cell and print the updated board
                        reveal_board(row, col)
                        print_board(count)

                        # Check if the game is won and end the game if it is
                        if is_game_won():
                            end_time = time.time()
                            time_taken = end_time - start_time
                            minutes = time_taken // 60
                            seconds = time_taken % 60
                            print("You win! It took you {:d} minutes and {:d} seconds.".format(int(minutes), int(seconds)))
                            print()
                            break
                        
                # action[2] == 'f'; action is to place or remove a flag 
                else:  
                    # Check if the input cell to flag is already revealed
                    if the_cell_to_flag_is_revealed(row, col):
                        print("Cannot put a flag there!")
                        continue
                    
                    # Place a flag on the cell and print the updated board
                    if board[(row, col)] == 'F': # The cell is already flagged 
                        # remove the flag so -1
                        num_flaggedbombs -= 1
                        modify_board(row, col, ' ')
                        print_board(count)
                    else: # The cell is not already flagged
                        # place a flag so +1
                        num_flaggedbombs += 1
                        modify_board(row, col, symbol)
                        print_board(count)

                    # Check if the game is won and end the game if it is
                    if is_game_won():
                        end_time = time.time()
                        time_taken = end_time - start_time
                        minutes = time_taken // 60
                        seconds = time_taken % 60
                        print("You win! It took you {:d} minutes and {:d} seconds.".format(int(minutes), int(seconds)))
                        print()
                        break
            except ValueError:
                print("Invalid cell. Enter the column followed by the row (ex: a1).To add or remove a flag,\nadd 'f' to the cell (ex:a5f).")
            
            except IndexError:
                print("Invalid cell. Enter the column followed by the row (ex: a1).To add or remove a flag,\nadd 'f' to the cell (ex:a5f).")
            
        # If the user entered 'q', break out of the outer loop without run rest code,
        # which means that do not ask user to play again
        if quit_game:
            break
        
        # Check whether to play again
        if play_again() is True:
            continue
        else:
            print()
            break
                        
play_game()
