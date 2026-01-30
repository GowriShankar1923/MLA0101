import heapq

graph = {
    'A':[('B',1),('C',4)],
    'B':[('D',2)],
    'C':[('D',1)],
    'D':[]
}

def best_first(start, goal):
    pq = [(0, start)]
    visited = []

    while pq:
        cost, node = heapq.heappop(pq)
        if node not in visited:
            visited.append(node)
            if node == goal:
                print("Path:", visited)
                return
            for n, c in graph[node]:
                heapq.heappush(pq, (c, n))

best_first('A','D')
