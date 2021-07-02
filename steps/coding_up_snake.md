# Steps for coding up snake using object oriented programming

In this guide, we provide a list of ideas for coding up snake in using concepts from object oriented programming (OOP). Note, this is just one possible way to code up the game and many others are possible and may well be better!

Note also that, we provide a fully working version of the game using OOP in [this](./example_snake/) folder. We expect that it may be useful to consult our approach throughout the task to give you an idea as to how to proceed.

We first discuss the three Python classes that we are going to create:

* Bone

* Food
* Snake

## Bone

Our snake and our food are going to be composed of bones. Computational bones are simpler than real bones. They have two properties:

* A position: a list [x,y] of the bone's coordinates
* A size: the width / height of the bone

Bones also have a method that draws them at their given position on the canvas. Here, we would just use the `pyjama.draw.rect` method

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