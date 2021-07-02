# Creating a blank screen

## A screen that lives and dies quickly

In this first session, we are going to create a blank screen using pygame. This screen will be where our snake lives, roams and feeds.

Code to do this is below. Copy and paste it into a script file and run the script. Note that the below code if ran will appear then immediately close.

```python
import pygame

pygame.init()

# Create screen
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Define colours in red-green-blue form
BLACK = (0, 0, 0)

# Display screen
screen.fill(BLACK)
pygame.display.update()

# Quit
pygame.quit()
```

## A screen that lives for a specified amount of time

The trouble with the above code is that the screen closes too soon. To fix this, we are going to make an infinite game loop that continues to run forever.

```python
import pygame

pygame.init()

# Create screen
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Define colours in red-green-blue form
BLACK = (0, 0, 0)

# Run game loop
game_over=False
while not game_over:
  
  # Display screen
	screen.fill(BLACK)
	pygame.display.update()

pygame.quit()
```

Note, to make the screen disappear you will have to run `Ctrl+c` from the terminal.

## Making a screen that we can exit

To avoid the above issues of a screen that lives in perpetuity, we are going to make use of pygame's event handling functionality. Specifically, we are going to use [pygame.event.get()](https://www.pygame.org/docs/ref/event.html#pygame.event.get) which gets all inputs from the keyboard and mouse during the game. Here, we are going to use this to print to the Python console the events that happen throughout the game and also allow quitting of the game if a user hits the close button.

```python
import pygame

pygame.init()

# Create screen
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Define colours in red-green-blue form
BLACK = (0, 0, 0)

# Run game loop
game_over=False
while not game_over:
  	pygame.display.update()
    for event in pygame.event.get():
      	print("event = ", event)
        if event.type==pygame.QUIT:
            game_over=True
    
    # Display screen
		screen.fill(BLACK)
		pygame.display.update()

pygame.quit()
```

Running the above you should see a bunch of events printed to the Python console as you run it: indicating things like "MouseMotion" or "MouseButtonUp".

Then if you click the exit button in the top left of the game display, the game should terminate.

# Next vignette

The [next](.drawing.md) vignette shows how to draw our snake on the screen.