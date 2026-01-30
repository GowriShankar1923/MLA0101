from collections import deque

def water_jug_problem():
    capacity_a = 4
    capacity_b = 3
    goal = 2

    visited = set()
    queue = deque([(0, 0)])

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        print((a, b))

        if a == goal or b == goal:
            print("Goal reached!")
            return

        # Possible operations
        queue.extend([
            (capacity_a, b),              # Fill A
            (a, capacity_b),              # Fill B
            (0, b),                       # Empty A
            (a, 0),                       # Empty B
            (a - min(a, capacity_b - b),  # Pour A → B
             b + min(a, capacity_b - b)),
            (a + min(b, capacity_a - a),  # Pour B → A
             b - min(b, capacity_a - a))
        ])

water_jug_problem()
