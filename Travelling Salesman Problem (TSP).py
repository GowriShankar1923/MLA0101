import itertools

cities = ['A','B','C']
distance = {
    ('A','B'):10, ('B','A'):10,
    ('A','C'):15, ('C','A'):15,
    ('B','C'):20, ('C','B'):20
}

def total_distance(path):
    dist = 0
    for i in range(len(path)-1):
        dist += distance[(path[i], path[i+1])]
    return dist

min_path = None
min_dist = float('inf')

for perm in itertools.permutations(cities):
    d = total_distance(perm)
    if d < min_dist:
        min_dist = d
        min_path = perm

print("Shortest Path:", min_path)
print("Distance:", min_dist)
