"""
author: H24111057 統計系 姚博瀚
"""
def get_matrix_from_input():
    matrix = []
    print("Enter the matrix row by row (one row per line). Enter 'q' to finish:")
    while True:
        row_input = input().strip()
        if row_input.lower() == "q" or not row_input:
            break
        matrix.append([int(x) for x in row_input.split()])
    return matrix

def update_matrix(matrix, x, y, k):
    value = matrix[x][y]
    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)
        matrix[x][y] = k
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] == value:
                queue.append((nx, ny))
    return matrix

def main():
    x, y, k = map(int, input("Enter index x, y, k (separated by whitespace): ").split())
    matrix = get_matrix_from_input()
    updated_matrix = update_matrix(matrix, x, y, k)

    print("Updated Matrix:")
    for row in updated_matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
