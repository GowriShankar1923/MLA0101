from collections import deque

def valid(m,c):
    return (m==0 or m>=c) and (3-m==0 or 3-m>=3-c)

start = (3,3,0)
goal = (0,0,1)
moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

def bfs():
    q = deque([(start, [])])
    visited = set()
    while q:
        state, path = q.popleft()
        if state == goal:
            return path+[state]
        for m,c in moves:
            if state[2]==0:
                new = (state[0]-m, state[1]-c,1)
            else:
                new = (state[0]+m, state[1]+c,0)
            if 0<=new[0]<=3 and 0<=new[1]<=3 and valid(new[0],new[1]):
                if new not in visited:
                    visited.add(new)
                    q.append((new, path+[state]))

print(bfs())
