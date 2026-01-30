graph = {
    'A':['B','C'],
    'B':['A','C'],
    'C':['A','B']
}

colors = ['Red','Green','Blue']
result = {}

def valid(node, color):
    for n in graph[node]:
        if result.get(n) == color:
            return False
    return True

def solve():
    for node in graph:
        for color in colors:
            if valid(node, color):
                result[node] = color
                break
    print("Graph Coloring:", result)

solve()
