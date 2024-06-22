"""  
author: H24111057 姚博瀚
"""

def parse_matrix(input_str):
    """
    Parse the input string into a dictionary representing the matrix.
    
    Args:
    input_str (str): A string representation of the matrix where rows are 
                     separated by '|' and elements are separated by ','.
    
    Returns:
    tuple: A tuple containing:
           - matrix (dict): A dictionary with keys as tuples (i, j) representing the 
                            coordinates and values as the matrix elements.
           - n (int): The size of the matrix (number of rows/columns).
    """
    rows = input_str.strip().split('|')
    n = len(rows)
    matrix = {}
    for i, row in enumerate(rows):
        elements = list(map(int, row.split(',')))
        for j, value in enumerate(elements):
            matrix[(i, j)] = value
    return matrix, n

def multiply_matrices(U, V, n):
    """
    Multiply two square matrices U and V stored as dictionaries.
    
    Args:
    U (dict): The first matrix stored as a dictionary with keys as tuples 
              (i, j) and values as the matrix elements.
    V (dict): The second matrix stored as a dictionary with keys as tuples 
              (i, j) and values as the matrix elements.
    n (int): The size of the matrices (number of rows/columns).
    
    Returns:
    M (dict): A dictionary representing the resulting matrix M from multiplying 
              U and V, with keys as tuples (i, j) and values as the matrix elements.
    """
    M = {}
    for i in range(n):
        for j in range(n):
            M[(i, j)] = sum(U.get((i, k), 0) * V.get((k, j), 0) for k in range(n))
    return M

def print_matrix(M, n):
    """
    Print the matrix stored as a dictionary.
    
    Args:
    M (dict): The matrix stored as a dictionary with keys as tuples (i, j) 
              and values as the matrix elements.
    n (int): The size of the matrix (number of rows/columns).
    """
    for i in range(n):
        row = [M.get((i, j), 0) for j in range(n)]
        print(row)

def main():
    """
    Main function to execute the matrix multiplication.
    It takes input for matrices U and V, parses them, performs matrix 
    multiplication, and prints the resulting matrix.
    """
    # Input matrix U
    U_input = input("Enter matrix U: ")
    U, n = parse_matrix(U_input)
    
    # Input matrix V
    V_input = input("Enter matrix V: ")
    V, _ = parse_matrix(V_input)
    
    # Compute matrix M = U x V
    M = multiply_matrices(U, V, n)
    
    # Output the result
    print("M = U x V")
    print_matrix(M, n)

# Entry point of the program
if __name__ == "__main__":
    main()
