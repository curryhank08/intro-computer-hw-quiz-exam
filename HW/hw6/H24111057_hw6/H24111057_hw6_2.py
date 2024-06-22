"""  
author: H24111057 姚博瀚
"""
import random

# Constants
ROWS = 10
COLS = 10
CANDY_TYPES = ['R', 'G', 'B', 'Y', 'O']  # Representing different candy colors

# Function to initialize the game board with random candies
def initialize_board(rows, cols):
    board = [[random.choice(CANDY_TYPES) for _ in range(cols)] for _ in range(rows)]
    return board

# Function to print the game board with row and column indices
def print_board(board):
    # Print column indices
    print("   ", end="")
    for c in range(len(board[0])):
        print(f"{c} ", end="")
    print()

    # Print row indices and board content
    for r in range(len(board)):
        print(f"{r}  ", end="")
        for c in range(len(board[r])):
            print(f"{board[r][c]} ", end="")
        print()
    print()

# Function to check if there are any possible moves left
def has_possible_moves(board):
    for r in range(ROWS):
        for c in range(COLS - 1):
            # Check horizontal adjacent candies
            if board[r][c] == board[r][c + 1]:
                return True
    for c in range(COLS):
        for r in range(ROWS - 1):
            # Check vertical adjacent candies
            if board[r][c] == board[r + 1][c]:
                return True
    return False

# Function to remove candies from the board after a match
def remove_matches(board, matches):
    for r, c in matches:
        board[r][c] = ' '

# Function to drop candies down after matches are removed
def drop_candies(board):
    for c in range(COLS):
        for r in range(ROWS - 1, -1, -1):
            if board[r][c] == ' ':
                for r_above in range(r - 1, -1, -1):
                    if board[r_above][c] != ' ':
                        board[r][c] = board[r_above][c]
                        board[r_above][c] = ' '
                        break

# Function to swap candies on the board
def swap_candies(board, r1, c1, r2, c2):
    board[r1][c1], board[r2][c2] = board[r2][c2], board[r1][c1]

# Function to check for matches after a swap
def check_for_matches(board, r, c):
    matches = set()
    
    # Check horizontally
    candy = board[r][c]
    count = 1
    # Check to the left
    c_left = c - 1
    while c_left >= 0 and board[r][c_left] == candy:
        matches.add((r, c_left))
        c_left -= 1
        count += 1
    # Check to the right
    c_right = c + 1
    while c_right < COLS and board[r][c_right] == candy:
        matches.add((r, c_right))
        c_right += 1
        count += 1
    if count >= 3:
        matches.add((r, c))
    
    # Check vertically
    count = 1
    # Check above
    r_up = r - 1
    while r_up >= 0 and board[r_up][c] == candy:
        matches.add((r_up, c))
        r_up -= 1
        count += 1
    # Check below
    r_down = r + 1
    while r_down < ROWS and board[r_down][c] == candy:
        matches.add((r_down, c))
        r_down += 1
        count += 1
    if count >= 3:
        matches.add((r, c))

    return matches

# Function to play the game
def play_game():
    board = initialize_board(ROWS, COLS)
    print("Welcome to Candy Crush!")
    print_board(board)

    while has_possible_moves(board):
        command = input("Enter 'q' to quit, or Select candies to swap (row col): ")
        if command.lower() == 'q':
            print("Quitting the game...")
            return
        
        try:
            r1, c1 = map(int, command.split())
            r2, c2 = map(int, input("Select candy to swap with (row col): ").split())

            if abs(r1 - r2) + abs(c1 - c2) != 1:
                print("Invalid move! You can only swap adjacent candies.")
                continue

            swap_candies(board, r1, c1, r2, c2)
            matches = set()
            matches.update(check_for_matches(board, r1, c1))
            matches.update(check_for_matches(board, r2, c2))

            if len(matches) < 3:
                print("No match. Swapping back.")
                swap_candies(board, r1, c1, r2, c2)
            else:
                print("Matching candies found!")
                remove_matches(board, matches)
                print_board(board)
                drop_candies(board)
                print("After dropping candies:")
                print_board(board)
        
        except ValueError:
            print("Invalid input! Please enter valid row and column indices.")

    print("No more possible moves or user quit. Game over!")

# Start the game
play_game()


