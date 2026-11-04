def safe(row, col):
    for r in range(n):
        c = board[r]
        if c != -1 and (c == col or abs(c - col) == abs(r - row)):
            return False
    return True

def solve(row):
    if row == n:
        for c in board:
            print(" ".join("Q" if j == c else "." for j in range(n)))
        print()
        return

    if board[row] != -1:
        solve(row + 1)
        return

    for col in range(n):
        if safe(row, col):
            board[row] = col
            solve(row + 1)
            board[row] = -1

n = int(input("Enter N: "))
r, c = map(int, input("Enter first queen position (row col): ").split())

board = [-1] * n
board[r - 1] = c - 1
solve(0)