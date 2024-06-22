"""
author: H24111057 統計系 姚博瀚
"""

class ConnectFour:
    def __init__(self):
        # Initialize the game board dimensions and the board itself
        self.rows = 6
        self.cols = 7
        self.gameBoard = [["" for _ in range(self.cols)] for _ in range(self.rows)]
        # Initialize the turn counter
        self.turnCounter = 0

    # Method to print the game board
    def print_game_board(self):
        for x in range(self.rows):
            # Print horizontal lines to create the game board grid
            print("\n+---+---+---+---+---+---+---+")
            print("|", end="")
            for y in range(self.cols):
                # Print each cell of the game board
                if self.gameBoard[x][y] == "X":
                    print(" X ", end="|")
                elif self.gameBoard[x][y] == "x":
                    print(" x ", end="|")
                elif self.gameBoard[x][y] == "O":
                    print(" O ", end="|")
                elif self.gameBoard[x][y] == "o":
                    print(" o ", end="|")
                else:
                    print("   ", end="|")
        # Print the column indices at the bottom of the game board
        print("\n+---+---+---+---+---+---+---+")
        print("  0   1   2   3   4   5   6 ", end="")

    # Method to modify the game board with a player's move
    def modify_array(self, coordinate, turn):
        row, col = coordinate
        self.gameBoard[row][col] = turn

    # Method to check if a column is available for placing a chip
    def is_column_available(self, column):
        return self.gameBoard[0][column] == ""

    # Method to check for a winner on the game board
    def check_for_winner(self, chip):
        # List to store coordinates of winning chips
        winning_chips = []

        # Check horizontal lines
        for x in range(self.rows):
            for y in range(self.cols - 3):
                if all(self.gameBoard[x][y+i] == chip for i in range(4)):
                    winning_chips.extend([(x, y+i) for i in range(4)])

        # Check vertical lines
        for x in range(self.rows - 3):
            for y in range(self.cols):
                if all(self.gameBoard[x+i][y] == chip for i in range(4)):
                    winning_chips.extend([(x+i, y) for i in range(4)])

        # Check diagonal lines (upper right to bottom left)
        for x in range(self.rows - 3):
            for y in range(3, self.cols):
                if all(self.gameBoard[x+i][y-i] == chip for i in range(4)):
                    winning_chips.extend([(x+i, y-i) for i in range(4)])

        # Check diagonal lines (upper left to bottom right)
        for x in range(self.rows - 3):
            for y in range(self.cols - 3):
                if all(self.gameBoard[x+i][y+i] == chip for i in range(4)):
                    winning_chips.extend([(x+i, y+i) for i in range(4)])

        # Return coordinates of winning chips if there's a winner, otherwise return False
        return winning_chips if winning_chips else False

    # Method to start and play the game
    def play(self):
        print("Welcome to Connect Four")
        print("-----------------------")
        while True:
            # Print the current game board
            self.print_game_board()

            # Determine current player
            if self.turnCounter % 2 == 0:
                player = 'X'
            else:
                player = 'O'

            # Get player's move and handle input validation
            while True:
                try:
                    column_picked = input(
                        f"\n\nPlayer {player} >> column (Enter 'q' for quitting): ")
                    if column_picked.upper() == 'Q':
                        print("\nGame ended early due to user quitting. Thank you for playing!")
                        return
                    column_picked = int(column_picked)
                    if column_picked < 0 or column_picked > self.cols - 1:
                        raise ValueError()
                    if not self.is_column_available(column_picked):
                        print("This column is full. Please choose another column.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid column number.")

            # Find the lowest available row in the selected column
            coordinate = [self.rows - 1, column_picked]
            while self.gameBoard[coordinate[0]][coordinate[1]] != "":
                coordinate[0] -= 1
            # Modify the game board with the player's move
            self.modify_array(coordinate, player)
            # Check for a winner or a draw
            winner = self.check_for_winner(player)
            self.turnCounter += 1

            # Handle game ending scenarios
            if winner or self.turnCounter == self.rows * self.cols:
                if winner:
                    # Highlight winning chips and print the final game board
                    for x, y in winner:
                        self.gameBoard[x][y] = self.gameBoard[x][y].strip().lower()
                    self.print_game_board()
                    print(f"\n\nGame over. Winner: {player}")
                else:
                    # Print the final game board in case of a draw
                    self.print_game_board()
                    print("\n\nGame over. It's a draw!")

                # Ask if the players want to play again
                play_again = input("\nDo you want to play again? (Y/N): ")
                if play_again.lower() == 'n':
                    print("\nGoodbye!")
                    return
                else:
                    # Reset the game board and turn counter for a new game
                    self.gameBoard = [["" for _ in range(self.cols)] for _ in range(self.rows)]
                    self.turnCounter = 0


# Instantiate and start the game
connect_four_game = ConnectFour()
connect_four_game.play()
