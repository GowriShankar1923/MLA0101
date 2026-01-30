N = 8
board = [-1] * N

def safe(r, c):
    return all(board[i] != c and abs(board[i] - c) != r - i for i in range(r))

def solve(r):
    if r == N:
        print(board)
        return True
    for c in range(N):
        if safe(r, c):
            board[r] = c
            if solve(r + 1):
                return True
    return False

solve(0)
