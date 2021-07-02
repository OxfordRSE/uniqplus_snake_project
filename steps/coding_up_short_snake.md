# Steps for coding up snake using object oriented programming

In this guide, we provide a list of ideas for coding up snake in using concepts from object oriented programming (OOP). Note, this is just one possible way to code up the game and many others are possible and may well be better!

Note also that, we provide a fully working version of the game using OOP in [this](./short_snake/) folder. We expect that it may be useful to consult our approach throughout the task to give you an idea as to how to proceed.

We first discuss the three Python classes that we are going to create:

* Bone

* Food
* Snake

These classes are going to be kept in the file `snake.py` and will be imported by the main script.

## Bone

Our snake and our food are going to be composed of bones. Computational bones are simpler than real bones. They have two properties:

* a `pos`: a list `[x,y]` of the bone's coordinates
* a `size`: the width or height of the bone (it's a square)

Bones also have a method that draws them at their given position on the canvas. Here, we would just use the `pyjama.draw.rect` method size the bones are squares. Note this function will need to take the screen as an input to be able to draw on it.

##Food 

The snake eats prey that we call "Food". The food only has one property: the single bone that comprises it.

Food is somewhat miraculous: each time a bit of food is eaten, another bit of food appears on the screen at a random location.

We want the locations at which the food appears to occur on grid values that will overlap with the position of our snake, so we ensure that this is the case using the following instantiation:

```python
class Food:
    def __init__(self, screen_width, screen_height, size=20):
        x = round(random.randrange(0, screen_width - size) / size) * size
        y = round(random.randrange(0, screen_height - size) / size) * size
        self.bone = Bone((x, y), size)
```

The food also has two methods:

* `draw()`: which draws the food on the screen by drawing the underlying bone
* `get_pos()`: which returns its position (this is going to be used by the `Snake` to check whether the food has been eaten)

## Snake

The snake is the most complex of beats in the game. It has the following properties:

* a `body` which comprises a single bone
* a `direction` in which it is currently travelling: this is a two-element list indicating the direction vector
* a `size`, which is the height / width of our square snake

It also has a number of methods:

* `change_direction` which updates the snake's direction according to a specified direction vector
* `draw` which draws the snake's bone
* `get_pos` which returns the current `[x,y]` position of the snake
* `get_new_pos` which updates the snake's position according to the direction in which it travels. Each time a snake moves, it moves by a distance equal to its `size`.
* `hits_side` which determines if the snake has hit any of the sides of the canvas
* `move_and_survive`: this moves the snake and then determines whether the snake is still surived after the move. This first uses `get_new_pos` to move the snake, then uses `hits_side` to determine if the new snake position has hit the side of the domain.
  * If the snake has hit the side of the domain the function return `False`.
  * If the snake has not hit the sides, it updates the snake's body to account for the new position and returns `True`.

## The main script file

Many of the things that are needed to code up the main script are contained within the various vignettes.   We make, however, the following suggestions that may help you to get up and running:

* Start with a `screen_height=400` and a `screen_width=600`
* Start the snake in the middle of the canvas and make it stationary
* Initialise the game with `speed=10` 
* In the game while loop:
  1. Check whether the game has been quit by the user clicking the box in the upper left corner of the canvas
  2. Determine which (if any) of the arrow keys have been pressed and use this to change the snake's direction
  3. Check whether the snake's position matches that of the food. If so, increment the speed by 1 unit
  4. If the snake hasn't fed, move the snake and check whether it has survived.
  5. If the snake hasn't survived terminate the game
  6. Otherwise draw the canvas, the snake and the food

