import pygame

from snake import Snake

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

BLACK = (0, 0, 0)

pygame.init()
clock = pygame.time.Clock()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create a snake
snake = Snake((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
direction = [0, 0]
# Run until the user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_UP]:
        direction = [0, -1]
    elif keys_pressed[K_DOWN]:
        direction = [0, 1]
    elif keys_pressed[K_LEFT]:
        direction = [-1, 0]
    elif keys_pressed[K_RIGHT]:
        direction = [1, 0]

    snake.change_direction(direction)
    snake.update()

    screen.fill(BLACK)
    snake.draw(screen)

    pygame.display.update()

    # Limit to 30 fps
    clock.tick(30)
# Done! Time to quit.
pygame.quit()
