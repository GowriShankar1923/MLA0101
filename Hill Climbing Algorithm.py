def hill_climbing():
    current = 5
    while True:
        neighbor = current - 1
        if neighbor >= 0:
            current = neighbor
        else:
            break
    print("Optimal Solution:", current)

hill_climbing()
