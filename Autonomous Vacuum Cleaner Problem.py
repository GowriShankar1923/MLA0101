grid = [[1,0,1],
        [0,1,0],
        [1,0,1]]

for i in range(3):
    for j in range(3):
        if grid[i][j] == 1:
            grid[i][j] = 0
            print("Cleaned:", i, j)
