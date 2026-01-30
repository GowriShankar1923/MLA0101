from collections import deque

goal = ((1,2,3),(4,5,6),(7,8,0))

def solve(start):
    q = deque([start])
    seen = {start}

    while q:
        s = q.popleft()
        if s == goal:
            print("Goal state reached")
            return

        for i in range(3):
            for j in range(3):
                if s[i][j] == 0:
                    x, y = i, j

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                n = [list(r) for r in s]
                n[x][y], n[nx][ny] = n[nx][ny], n[x][y]
                n = tuple(tuple(r) for r in n)
                if n not in seen:
                    seen.add(n)
                    q.append(n)

start = ((1,2,3),(4,0,6),(7,5,8))
solve(start)
