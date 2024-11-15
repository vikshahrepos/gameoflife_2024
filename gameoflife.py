def print_grid(grid):
    for row in grid:
        print(' '.join(str(cell) for cell in row))
    print()

def game_of_life_iteration(grid):
    grid_size = len(grid)
    new_grid = [[grid[i][j] for j in range(grid_size)] for i in range(grid_size)]

    for i in range(grid_size):
        for j in range(grid_size):
            live_neighbors = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if i + x >= 0 and i + x < grid_size and j + y >= 0 and j + y < grid_size:
                        live_neighbors += grid[i + x][j + y]
            if grid[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i][j] = 0
            else:
                if live_neighbors == 3:
                    new_grid[i][j] = 1

    for i in range(grid_size):
        for j in range(grid_size):
            grid[i][j] = new_grid[i][j]

# Example grid
initial_grid = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

print("Initial Grid:")
print_grid(initial_grid)

game_of_life_iteration(initial_grid)

print("Grid After One Iteration:")
print_grid(initial_grid)