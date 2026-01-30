board = [' ']*9

def display():
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])

board[0] = 'X'
board[4] = 'O'
board[8] = 'X'
display()
