import pygame
import time

from snake import Snake, Food, losing_message, score_message

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

# Create screen
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create an initially stationary snake
snake = Snake((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
direction = [0, 0]

# Instantiate score
score = 0

# Run until the user asks to quit
running = True
is_survived = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # Check whether snake changes direction by key pressing
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
    
    # Check whether snake eats, move the snake and see if they survive
    if snake.get_head_pos() == food.get_pos():
        snake.grow()
        del food
        food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
        score += 1
    else:
        is_survived = snake.move_and_survive(SCREEN_WIDTH, SCREEN_HEIGHT)
    if not is_survived:
        running = False

    # Draw things on screen
    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)
    score_message(score, screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.display.update()

    # Dictates snake speed
    clock.tick(10)
    
# Done! Time to quit.
losing_message("You lost", screen, SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.update()
time.sleep(2)
pygame.quit()
