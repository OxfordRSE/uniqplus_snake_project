# Drawing on the screen

In this vignette, we are going to explain how to draw on the screen. We are going to need to do this so that we can draw both the snake and the food it eats.

## Drawing a rectangle

Pygame comes with the [pygame.draw.rect](http://www.pygame.org/docs/ref/draw.html) method which will draw a rectangle on the screen. The first argument to this function is the screen itself, the second is the colour we wish to draw and the last argument is a list of the form [left, top, width, height] which specifies the limits of the rectangle.

We are now going to draw a stationary white rectangle in the middle of the screen.

```python
import pygame

pygame.init()

# Create screen
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Define colours in red-green-blue form
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
    pygame.display.update()

pygame.quit()
```

## Adding text to the screen

We are now going to add some text to the screen. We can do this with [pygame.font.SysFont](https://www.pygame.org/docs/ref/font.html). This function takes as arguments:

1. a font name (here we specify None so as to get the default font)
2. a font size