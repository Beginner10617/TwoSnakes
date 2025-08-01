import pygame

CELL_SIZE = 40
HORIZONTAL_CELLS = 20
VERTICAL_CELLS = 10
THICKNESS = 1

def set_thickness(thickness):
    assert isinstance(thickness, int) and thickness > 0, "Thickness must be a positive integer."
    assert thickness <= CELL_SIZE, "Thickness must not exceed cell size."
    global THICKNESS
    THICKNESS = thickness

def set_cell_size(size):
    assert isinstance(size, int) and size > 0, "Cell size must be a positive integer."
    assert size >= THICKNESS, "Cell size must be greater than or equal to thickness."
    global CELL_SIZE
    CELL_SIZE = size

def set_grid_dimensions(horizontal_cells, vertical_cells):
    assert isinstance(horizontal_cells, int) and horizontal_cells > 0, "Horizontal cells must be a positive integer."
    assert isinstance(vertical_cells, int) and vertical_cells > 0, "Vertical cells must be a positive integer."
    assert horizontal_cells * CELL_SIZE > THICKNESS, "Grid width must be greater than thickness."
    assert vertical_cells * CELL_SIZE > THICKNESS, "Grid height must be greater than thickness."
    assert horizontal_cells > 1, "Horizontal cells must be greater than 1."
    assert vertical_cells > 1, "Vertical cells must be greater than 1."

    global HORIZONTAL_CELLS, VERTICAL_CELLS
    HORIZONTAL_CELLS = horizontal_cells
    VERTICAL_CELLS = vertical_cells

SNAKE_1 = [
    [2, 0],
    [1, 0],
    [0, 0]
]
SNAKE_1_CLR = (255, 0, 0) # Red color for snake 1

SNAKE_2 = [
    [HORIZONTAL_CELLS - 3, VERTICAL_CELLS - 1],
    [HORIZONTAL_CELLS - 2, VERTICAL_CELLS - 1],
    [HORIZONTAL_CELLS - 1, VERTICAL_CELLS - 1]
]
SNAKE_2_CLR = (0, 0, 255) # Blue color for snake 2

def move_snake(snake, direction):
    assert direction in ['U', 'D', 'L', 'R'], "Invalid direction. Use 'U', 'D', 'L', or 'R'."
    assert isinstance(snake, list) and all(isinstance(segment, list) and len(segment) == 2 for segment in snake), "Snake must be a list of [x, y] pairs."
    head = snake[0]
    if direction == 'U':
        new_head = [head[0], head[1] - 1]
    elif direction == 'D':
        new_head = [head[0], head[1] + 1]
    elif direction == 'L':
        new_head = [head[0] - 1, head[1]]
    elif direction == 'R':
        new_head = [head[0] + 1, head[1]]
    else:
        return snake  # no movement

    # Add new head and remove tail
    snake.insert(0, new_head)
    snake.pop()
    return snake

def draw_grid():
    for x in range(HORIZONTAL_CELLS):
        for y in range(VERTICAL_CELLS):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - THICKNESS, CELL_SIZE - THICKNESS)
            pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), rect, THICKNESS)

    # Draw snakes
    for segment in SNAKE_1:
        rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE - THICKNESS, CELL_SIZE - THICKNESS)
        pygame.draw.rect(pygame.display.get_surface(), SNAKE_1_CLR, rect)

    for segment in SNAKE_2:
        rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE - THICKNESS, CELL_SIZE - THICKNESS)
        pygame.draw.rect(pygame.display.get_surface(), SNAKE_2_CLR, rect)

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((HORIZONTAL_CELLS * CELL_SIZE, VERTICAL_CELLS * CELL_SIZE))
    pygame.display.set_caption("Simple Pygame Window")

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # fill the screen with black
        draw_grid()
        pygame.display.flip()    # update the display

    pygame.quit()

if __name__ == "__main__":
    main()