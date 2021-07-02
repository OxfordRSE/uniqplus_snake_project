# Key pressing

In this vignette, we are going to use some of pygame's functionality to determine which arrow key has been pressed and print this information to the screen.

The code to accomplish this is below.

```python
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
        if event.type==pygame.QUIT:
            game_over=True
    
    # Draw black canvas
    screen.fill(BLACK)
    # Draw rectangle
    size = 20
    pygame.draw.rect(
            screen, WHITE,
      			[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, size, size]
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
```

This code has a few new elements:

```python
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)
```

imports the numeric constants that pygame uses as keys in the dictionary that is returned by:

```python
keys_pressed = pygame.key.get_pressed()
```

So that `keys_pressed[K_UP]` returns True if the up arrow key is pressed; `keys_pressed[K_RIGHT]` returns True if the right arrow key is pressed; and so on.

We then create a function:

```python
def direction_message(msg):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, WHITE)
    screen.blit(mesg, [SCREEN_WIDTH // 2, 0])
```

which takes a message as its argument and prints the message near the middle of the screen.

The last addition to the code is:

```python
keys_pressed = pygame.key.get_pressed()
if keys_pressed[K_UP]:
  direction_message("Up!")
elif keys_pressed[K_DOWN]:
  direction_message("Down!")
elif keys_pressed[K_LEFT]:
  direction_message("Left!")
elif keys_pressed[K_RIGHT]:
  direction_message("Right!")
```

which then prints each direction to the screen if a key is pressed.