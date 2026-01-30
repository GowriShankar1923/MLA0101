def minimax(depth, isMax):
    if depth == 0:
        return 1

    if isMax:
        return max(minimax(depth-1, False), minimax(depth-1, False))
    else:
        return min(minimax(depth-1, True), minimax(depth-1, True))

print("Minimax Value:", minimax(3, True))
