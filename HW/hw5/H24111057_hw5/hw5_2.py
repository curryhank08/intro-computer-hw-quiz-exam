"""
@author: H24111057 統計系 姚博瀚
"""
import random

def create_board(board_length=30, penalty_probability=0.3):
    board = ['_' for _ in range(board_length)]
    for i in range(board_length):
        if random.random() < penalty_probability:
            board[i] = 'P'
    return board

def roll_dice():
    return random.randint(1, 6)

def move_player(player, dice_roll, board):
    new_position = min(player[0] + dice_roll, len(board) - 1)
    if board[new_position] == 'P':
        skip_next_round = True
    else:
        skip_next_round = False
    return [new_position, skip_next_round]

def print_board(board, players):
    for i, square in enumerate(board):
        if square == 'P':  
            if i == players[0][0] and i == players[1][0]:
                print('x', end='')
            elif i == players[0][0]:
                print('A', end='')
            elif i == players[1][0]:
                print('B', end='')
            else:
                print('_', end='')
        else:
            if i == players[0][0] and i == players[1][0]:
                print('X', end='')
            elif i == players[0][0]:
                print('A', end='')
            elif i == players[1][0]:
                print('B', end='')
            else:
                print('_', end='')

def print_board_initiated(board):
    row = ''.join(board)
    print(row)

def play_game():
    board = create_board()
    players = [[0, False], [0, False]]
    
    while True:
        dices = []
        for i in range(2):
            # debug:
            # print(f"current i:{i}")
            
            if players[i][1] == True:
                players[i][1] = False
                dice_roll = 0
                dices.append(0)
                continue
            else:
                dice_roll = roll_dice()
                dices.append(dice_roll)
                players[i] = move_player(players[i], dice_roll, board)
                
        print_board(board, players)
        print(f" (A:{dices[0]}, B:{dices[1]})")
        #print()

        if players[0][0] == players[1][0] == len(board) - 1:
            print("Both players win!")
            print()
            print_board_initiated(board)
            return  # Exit the function when a player wins
        elif players[0][0] == len(board) - 1:
            print(f"Player {chr(65 + 0)} wins!")
            print()
            print_board_initiated(board)
            return
        elif players[1][0] == len(board) - 1:
            print(f"Player {chr(65 + 1)} wins!")
            print()
            print_board_initiated(board)
            return

play_game()

