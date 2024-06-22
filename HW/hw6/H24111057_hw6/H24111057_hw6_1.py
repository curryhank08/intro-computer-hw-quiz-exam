"""  
author: H24111057 姚博瀚
"""

def read_board_from_file(filename):
    board = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split(',')))
            board.append(row)
    return board

def crush_candies(board):
    rows, cols = len(board), len(board[0])
    crushed = False
    to_be_crushed = [[False] * cols for _ in range(rows)]
    
    # Mark candies to be crushed
    for r in range(rows):
        for c in range(cols - 2):
            if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                to_be_crushed[r][c] = to_be_crushed[r][c+1] = to_be_crushed[r][c+2] = True
                crushed = True
        for c in range(cols):
            if r < rows - 2 and abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                to_be_crushed[r][c] = to_be_crushed[r+1][c] = to_be_crushed[r+2][c] = True
                crushed = True
    
    # Crush candies
    for r in range(rows):
        for c in range(cols):
            if to_be_crushed[r][c]:
                board[r][c] = 0
    
    return board, crushed

def move_candies(board):
    rows, cols = len(board), len(board[0])
    new_board = [[0] * cols for _ in range(rows)]
    
    # Move candies down column by column
    for c in range(cols):
        bottom = rows - 1
        for r in range(rows - 1, -1, -1):
            if board[r][c] != 0:
                new_board[bottom][c] = board[r][c]
                bottom -= 1
    
    return new_board

def candy_crush(filename):
    board = read_board_from_file(filename)
    while True:
        board, crushed = crush_candies(board)
        if not crushed:
            break
        board = move_candies(board)
    return board

def print_board_to_file(board, filename):
    with open(filename, 'w') as file:
        for row in board:
            file.write(','.join(map(str, row)) + '\n')


if __name__ == "__main__":
    input_filename = '/Users/yaohank/Library/CloudStorage/OneDrive-gs.ncku.edu.tw/計算機概論2/HW/hw6/candy_input1.txt'
    output_filename = 'output.txt'
    
    final_board = candy_crush(input_filename)
    print_board_to_file(final_board, output_filename)
