import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

# Set up grid
cols, rows = 50, 50
cell_size = width // cols

# Initialize grid with random values
grid = np.random.choice([0, 1], size=(rows, cols))

def draw_grid(surface, grid):
    for y in range(rows):
        for x in range(cols):
            color = (255, 255, 255) if grid[y][x] == 1 else (0, 0, 0)
            pygame.draw.rect(surface, color, (x * cell_size, y * cell_size, cell_size - 1, cell_size - 1))

def update_grid(grid):
    new_grid = np.copy(grid)
    for y in range(rows):
        for x in range(cols):
            # Count live neighbors
            neighbors = sum([grid[(y-1)%rows][(x-1)%cols], grid[(y-1)%rows][x], grid[(y-1)%rows][(x+1)%cols],
                             grid[y][(x-1)%cols], grid[y][(x+1)%cols],
                             grid[(y+1)%rows][(x-1)%cols], grid[(y+1)%rows][x], grid[(y+1)%rows][(x+1)%cols]])
            # Apply Conway's rules
            if grid[y][x] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[y][x] = 0
            elif grid[y][x] == 0 and neighbors == 3:
                new_grid[y][x] = 1
    return new_grid

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid = update_grid(grid)
    screen.fill((0, 0, 0))
    draw_grid(screen, grid)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()