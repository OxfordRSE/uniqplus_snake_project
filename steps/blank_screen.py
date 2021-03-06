import pygame
# import constants used by pygame to map each key
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)

pygame.init()

# Create screen
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Define colours in red-green-blue form
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Function which draws square at some point
def draw_square(x, y, size=20):
    pygame.draw.rect(
            screen, WHITE,
      			[x, y, size, size]
        )

# Function which moves square
def move_square(direction, current_x, current_y, size=20):
    new_x = current_x + size * direction[0]
    new_y = current_y + size * direction[1]
    return new_x, new_y

# Initialise rectangle position and velocity
x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
direction = [0, 0]

# Create clock and specify the frame rate
clock = pygame.time.Clock()
speed = 10

# Run game loop
game_over=False
while not game_over:
    for event in pygame.event.get():
        print("event = ", event)
        if event.type==pygame.QUIT:
            game_over=True
    
    # Draw black canvas
    screen.fill(BLACK)

    
    # Display the keys that are pressed by the user
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_UP]:
        direction = [0, -1]
    elif keys_pressed[K_DOWN]:
        direction = [0, 1]
    elif keys_pressed[K_LEFT]:
        direction = [-1, 0]
    elif keys_pressed[K_RIGHT]:
        direction = [1, 0]
    
    # Update square position
    x, y = move_square(direction, x, y)
    draw_square(x, y)
    
    # Update display
    pygame.display.update()
    
    # Delay game updates according to frame rate
    clock.tick(speed)

pygame.quit()