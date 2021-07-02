# Moving objects

In this vignette, we are going to describe how we can use objects move across the screen in response to arrow keys being pressed.

We are going to start with our square in the middle of the screen and allow it to move left, right, up or down in response to pressing of the keys. We are going to do this in such a way that the square continues to move in a direction unless keys are pressed which make it move in a different direction.

To do this, we are first going to write a function which draws the square at a given location in the screen.

```python
def draw_square(x, y, size=20):
    pygame.draw.rect(
            screen, WHITE,
      			[x, y, size, size]
        )
```

Next we are going to make a function that takes the current (x,y) position of the square and moves it according to a direction.

The direction is going to be a list indicating the vector of movements on the canvas.

In each frame, we are going to move the square by discrete jumps equal to its size length.

This function will be executed each time the loop goes round and will update the position of the square.

```python
def move_square(direction, current_x, current_y, size=20):
    new_x = current_x + size * direction[0]
    new_y = current_y + size * direction[1]
    return new_x, new_y
```

We get the direction vectors from whichever key is pressed:

```python
keys_pressed = pygame.key.get_pressed()
if keys_pressed[K_UP]:
    direction = [0, -1]
elif keys_pressed[K_DOWN]:
    direction = [0, 1]
elif keys_pressed[K_LEFT]:
    direction = [-1, 0]
elif keys_pressed[K_RIGHT]:
    direction = [1, 0]
```

Note that, confusingly, pygame treats up and down the opposite way to which you might expect, so that's why we choose -1 for up and +1 for down.

Finally, we put everything together into a script that allows a user to move the square according to the key they press.

Note that, when you execute the below, the square should shoot off the screen very quickly. That's why we need to control the speed of the game, which we illustrate in the [next](./speed.md) vignette.

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
    

# Initialise square position and velocity
x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
direction = [0, 0]


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

pygame.quit()
```

