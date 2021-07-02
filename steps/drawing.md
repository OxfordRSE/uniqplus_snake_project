# Drawing on the screen

In this vignette, we are going to explain how to draw on the screen. We are going to need to do this so that we can draw both the snake and the food it eats.

## Drawing a rectangle

Pygame comes with the [pygame.draw.rect](http://www.pygame.org/docs/ref/draw.html) method which will draw a rectangle on the screen. The arguments to this function are:

1. the screen itself
2. the colour we wish to draw
3. a list of the form [left, top, width, height] which specifies the limits of the rectangle.

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
    pygame.display.update()

pygame.quit()
```

## Adding text to the screen

We are now going to add some text to the screen.

We can do this with a combination of functions starting with [pygame.font.SysFont](https://www.pygame.org/docs/ref/font.html), which selects the font we are goind to display the message in. This function takes as arguments:

1. a font name (here we specify None so as to get the default font)
2. a font size

We then create the message itself using `.render()` as shown in the below code snipped. The arguments to this function are:

1. the text we wish to display
2. whether to specify the characters as having smooth edges (here we always use `True` for this)
3. the text colour

The final thing we do is draw the object on the screen using `blit`. The arguments to this are:

1. the rendered message
2. a list specifying the horizontal and vertical positions of where we wish to display it

The following draws "UNIQ+ rocks!" near the top of the screen.

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
    
    # Draw text
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render("UNIQ+ rocks!", True, WHITE)
    screen.blit(mesg, [SCREEN_WIDTH // 2, 0])
    
    # Update display
    pygame.display.update()

pygame.quit()
```

