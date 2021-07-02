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

# Function which produces a message
def direction_message(msg):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, WHITE)
    screen.blit(mesg, [SCREEN_WIDTH // 2, 0])

# Run game loop
game_over=False
while not game_over:
    for event in pygame.event.get():
        print("event = ", event)
        if event.type==pygame.QUIT:
            game_over=True
    
    # Draw black canvas
    screen.fill(BLACK)
    # Draw rectangle
    size = 20
    pygame.draw.rect(
            screen, WHITE,
      			[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, 20]
        )
    
    # Display the keys that are pressed by the user
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_UP]:
        direction_message("Up!")
    elif keys_pressed[K_DOWN]:
        direction_message("Down!")
    elif keys_pressed[K_LEFT]:
        direction_message("Left!")
    elif keys_pressed[K_RIGHT]:
        direction_message("Right!")
    
    
    # Update display
    pygame.display.update()

pygame.quit()