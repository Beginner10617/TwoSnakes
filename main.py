import pygame

CELL_SIZE = 40
HORIZONTAL_CELLS = 20
VERTICAL_CELLS = 10
THICKNESS = 1

def set_thickness(thickness):
    global THICKNESS
    THICKNESS = thickness

def set_cell_size(size):
    global CELL_SIZE
    CELL_SIZE = size

def set_grid_dimensions(horizontal_cells, vertical_cells):
    global HORIZONTAL_CELLS, VERTICAL_CELLS
    HORIZONTAL_CELLS = horizontal_cells
    VERTICAL_CELLS = vertical_cells

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((HORIZONTAL_CELLS * CELL_SIZE, VERTICAL_CELLS * CELL_SIZE))
    pygame.display.set_caption("Simple Pygame Window")

    # Make grid lines
    def draw_grid():
        for x in range(0, HORIZONTAL_CELLS * CELL_SIZE, CELL_SIZE):
            if(x==0): continue
            pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, VERTICAL_CELLS * CELL_SIZE), THICKNESS)
        for y in range(0, VERTICAL_CELLS * CELL_SIZE, CELL_SIZE):
            if(y==0): continue
            pygame.draw.line(screen, (255, 255, 255), (0, y), (HORIZONTAL_CELLS * CELL_SIZE, y), THICKNESS)

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