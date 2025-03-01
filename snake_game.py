import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 400
GRID_SIZE = 20
GRID_COUNT = WINDOW_SIZE // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Setup display
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

# Snake initial position and direction
snake = [(GRID_COUNT//2, GRID_COUNT//2)]
direction = [1, 0]
food = [random.randint(0, GRID_COUNT-1), random.randint(0, GRID_COUNT-1)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != [0, 1]:
                direction = [0, -1]
            elif event.key == pygame.K_DOWN and direction != [0, -1]:
                direction = [0, 1]
            elif event.key == pygame.K_LEFT and direction != [1, 0]:
                direction = [-1, 0]
            elif event.key == pygame.K_RIGHT and direction != [-1, 0]:
                direction = [1, 0]

    # Move snake
    new_head = [(snake[0][0] + direction[0]) % GRID_COUNT,
                (snake[0][1] + direction[1]) % GRID_COUNT]

    # Check collision with self
    if new_head in snake:
        running = False
    
    snake.insert(0, new_head)
    
    # Check if food eaten
    if new_head == food:
        food = [random.randint(0, GRID_COUNT-1), random.randint(0, GRID_COUNT-1)]
    else:
        snake.pop()

    # Draw
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN,
                        (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE,
                         GRID_SIZE-1, GRID_SIZE-1))
    pygame.draw.rect(screen, RED,
                    (food[0]*GRID_SIZE, food[1]*GRID_SIZE,
                     GRID_SIZE-1, GRID_SIZE-1))
    pygame.display.flip()
    
    clock.tick(10)

pygame.quit()
