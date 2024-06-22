""" 
author: H24111057 姚博瀚
"""

import random
import os

def generate_path(N, M):
    # This function generates a random path through an NxM maze, represented as a dictionary. The keys are (i, j) tuples representing
    # coordinates of each cell in the maze and the values are integers: 0 for empty, 1 for obstacle, and 2 for path. The path starts 
    # from (0,0) and ends at (N-1,M-1), and the direction (right or down) at each step is chosen randomly. Exceptions for TypeError 
    # and KeyError are handled.
    try:
        maze = {(i, j): 0 for i in range(N) for j in range(M)}
        current = (0, 0)
        maze[current] = 2
        while current != (N-1, M-1):
            if current[0] == N-1:
                current = (current[0], current[1] + 1)
            elif current[1] == M-1:
                current = (current[0] + 1, current[1])
            else:
                current = random.choice([(current[0] + 1, current[1]), (current[0], current[1] + 1)])
            maze[current] = 2
        return maze
    except (TypeError, KeyError) as e:
        print(f"Error in generate_path: {e}")
        return None

def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles (represented as 1) to the empty cells (represented as 0) in the given maze until at least
    # min_obstacles have been added. If a KeyError occurs while trying to set an obstacle, it is caught and a message is printed.
    count = 0
    while count < min_obstacles:
        i, j = random.randint(0, N-1), random.randint(0, M-1)
        try:
            if maze[(i, j)] == 0:
                maze[(i, j)] = 1
                count += 1
        except KeyError as e:
            print(f"Error in add_obstacles: {e}")

def set_obstacle(maze, N, M):
    # This function allows a user to manually set an obstacle in the maze. The user is prompted to input the coordinates of the cell
    # where they want to place the obstacle. If the cell is part of the path or an obstacle is already present, an error message is 
    # displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.
    try:
        i, j = map(int, input("Enter the coordinates (row,column) to set an obstacle: ").split(','))
        if maze[(i, j)] == 2:
            print("Error: Cannot place an obstacle on the path.")
        elif maze[(i, j)] == 1:
            print("Error: An obstacle is already present at this location.")
        else:
            maze[(i, j)] = 1
            print("Obstacle set successfully.")
    except (KeyError, IndexError):
        print("Error: Coordinates out of bounds.")
    except ValueError:
        print("Error: Invalid input. Please enter two integers.")

def remove_obstacle(maze, N, M):
    # This function allows a user to manually remove an obstacle from the maze. The user is prompted to input the coordinates of the 
    # cell where they want to remove the obstacle. If the cell is part of the path or there's no obstacle at the given cell, an error 
    # message is displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.
    try:
        i, j = map(int, input("Enter the coordinates (row,column) to remove an obstacle: ").split(','))
        if maze[(i, j)] == 2:
            print("Error: Cannot remove a cell from the path.")
        elif maze[(i, j)] == 0:
            print("Error: No obstacle present at this location.")
        else:
            maze[(i, j)] = 0
            print("Obstacle removed successfully.")
    except (KeyError, IndexError):
        print("Error: Coordinates out of bounds.")
    except ValueError:
        print("Error: Invalid input. Please enter two integers.")

'''
def print_maze(maze, N, M):
    # This function prints the current state of the maze in a grid-like format. Each cell is represented by a 3-character string: 
    # '   ' for empty cells, ' X ' for obstacles, and ' O ' for path cells. If a KeyError occurs while trying to access a cell, it is 
    # caught and a message is printed.
    try:
        for i in range(N):
            for j in range(M):
                if maze[(i, j)] == 0:
                    print("   ", end="")
                elif maze[(i, j)] == 1:
                    print(" X ", end="")
                else:
                    print(" O ", end="")
            print()
    except KeyError as e:
        print(f"Error in print_maze: {e}")
'''

def print_maze(maze, N, M):
    # Goal: Print the maze map as a grid to the console using boundaries with "-", "|", and "+" symbols.
    # Detailed Instructions:
    # 1. For each row in the maze map:
    #   a. Print a horizontal boundary line with "+" symbols at the intersections and "-" symbols between them.
    #   b. For each cell in the row:
    #       If the cell is an obstacle, print an "X" symbol.
    #       Otherwise, print a space character.
    #   c. Print a vertical boundary line with "|" symbols at the ends.
    # 2. Print a horizontal boundary line with "+" symbols at the intersections and "-" symbols between them at the bottom of the maze map.
    
    print()
    print(f"Generated Maze Map:")
    print("+" + "---+" * M)
    for i in range(N):
        row_str = "|"
        for j in range(M):
            if maze[(i, j)] == 0:
                row_str += "   "
            elif maze[(i, j)] == 1:
                row_str += " X "
            elif maze[(i, j)] == 2:
                row_str += " O "
            row_str += "|"
        print(row_str)
        print("+" + "---+" * M)


def main():
    # This function serves as the main driver of the program. It reads the maze dimensions from a file, asks the user for the minimum 
    # number of obstacles to be added, generates the path and adds the obstacles, and then enters a loop where the user can choose to 
    # set or remove obstacles, print the maze, or exit the program. Exceptions for ValueError, IOError, and NameError are handled.
    
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        try:
            filename = input("Enter the maze grid file name: ")
            file_path = os.path.join(script_dir, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                N = (len(lines) - 1) // 2
                M = (len(lines[0].strip()) + 1) // 4
                break
        except IOError:
            print("Error: File not found. Please try again.")

    while True:
        try:
            min_obstacles = int(input(f"Enter the minimum number of obstacles(0-{N * M - (N + M - 1 -1)}): "))
            if min_obstacles < 0 or min_obstacles >= N * M - (N + M - 1):
                raise ValueError
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

    maze = generate_path(N, M)
    if maze:
        add_obstacles(maze, min_obstacles, N, M)
        print_maze(maze, N, M)
        while True:
            try:
                choice = input("\nOptions:\n1. Set obstacle\n2. Remove obstacle\n3. Exit\nEnter your choice: ")
                if choice == '1':
                    set_obstacle(maze, N, M)
                    print_maze(maze, N, M)
                elif choice == '2':
                    remove_obstacle(maze, N, M)
                    print_maze(maze, N, M)
                elif choice == '3':
                    break
                else:
                    print("Error: Invalid option. Please try again.")
            except NameError:
                print("Error: Choice not defined. Please try again.")

main()