"""  
author: H24111057 姚博瀚
"""
# request size of grid
size = int(input("Enter the size of the grid: "))
# initiate the grid by the size requested in a nested list
grid = [['_' for _ in range(size)] for _ in range(size)]

# debug use:
# print(grid)

# define fuction of printing grid
def print_grid():
    for row in grid:
        print(" ".join(row))

# define function of editting grid by coordinate and item to place
def modify_grid(row, col, item):
    grid[row][col] = item

# print the initiated grid before iterately requesting a cell to edit
print_grid()
# continue editting cells until enter done
while True:
    # request a coordinate of cell to edit
    coordinate = str(input("Enter the cell coordinates to edit (row, col): "))
    
    # end while loop when getting done
    if coordinate.lower() == 'done':
        print()
        break
    else:
        coordinate = coordinate.split(",")
        row, col = int(coordinate[0]), int(coordinate[1])
        
        # debug use:
        # print(f"row, col: {row}, {col}")
        
        # request a value to place in the cell 
        value_in_cell = str(input("Enter the new value for the cell: "))
        # Edit cell
        modify_grid(row, col, value_in_cell)
        # Print grid after being editted
        print_grid()
        
    