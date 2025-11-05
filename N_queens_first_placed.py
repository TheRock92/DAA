def print_board(board):
    """Function to print the chessboard."""
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board, row, col, n):
    """Checks if it's safe to place a queen at board[row][col]."""
    
    # Check column (above)
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row, n):
    """Backtracking function to place queens row by row."""
    
    # Base case: all queens placed successfully
    if row == n:
        print("✅ Solution Found:")
        print_board(board)
        return True

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen

            # Recur to place rest of the queens
            if solve_nqueens(board, row + 1, n):
                return True  # Stop after finding one solution

            # Backtrack: remove queen
            board[row][col] = 0

    return False

# ---------- MAIN ----------
n = int(input("Enter the value of N: "))

# Initialize N×N board with all 0s
board = [[0] * n for _ in range(n)]

# Place first queen manually as mentioned in problem
board[0][0] = 1

# Start solving from second row (row = 1)
if not solve_nqueens(board, 1, n):
    print("No solution exists.")
