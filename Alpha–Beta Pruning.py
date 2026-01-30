def alphabeta(depth, alpha, beta, isMax):
    if depth == 0:
        return 1

    if isMax:
        for i in range(2):
            alpha = max(alpha, alphabeta(depth-1, alpha, beta, False))
            if beta <= alpha:
                break
        return alpha
    else:
        for i in range(2):
            beta = min(beta, alphabeta(depth-1, alpha, beta, True))
            if beta <= alpha:
                break
        return beta

print("Alpha Beta Value:", alphabeta(3, -1000, 1000, True))
