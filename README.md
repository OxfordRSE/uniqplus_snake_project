# Programming snake in Python using object oriented programming

This repository represents a day long project providing an introduction to object oriented programming (OOP) in Python. The aim of the project is to code up a version of the once popular mobile game *snake* using OOP principles.

## Course prerequisites
This course requires that individuals have a basic knowledge of the Python language. Participants do not need to have any knowledge of [pygame](https://www.pygame.org/news), which is the fantastic Python package we use here to make the games.

## What is snake?
[Snake](https://en.wikipedia.org/wiki/Snake_(video_game_genre)) is a common name for a game in which a player maneuvers a line which grows in length, where the main obstacle is the line itself. Although variants existed before, it became popular in the late 1990s when it was preloaded onto Nokia phones.

<img src="https://www.silicon.co.uk/wp-content/uploads/2012/08/snakenokia3310.jpg" width="200" height="300" />

## Getting up and running in pygame
To code up our snake game(s), we are going to use the Python package, [pygame](https://www.pygame.org/news). To install it, you can run:

`pip install pygame`

from the command line. Note that this requires you to have the command line tool `pip` installed (see [here](https://pip.pypa.io/en/stable/installing/) for instructions on this).

To help get you acquainted with pygame and to give some guidance of the task, we have created the following short vignettes that we recommend all coders go through:

- [Setting up a blank canvas](./steps/blank_screen.md)
- [Drawing on the canvas](./steps/drawing.md)
- [Accessing the keys pressed by a user](./steps/keys.md)
- [Moving a square across the canvas using the keys](./steps/moving.md)
- [Controlling the game speed](./steps/speed.md)

## Our snake games
Here, we offer two possible variants of the game of increasing difficulty:

1. *Short Snake*. The rules of this game are [here](./rules/short_snake.md)
2. *Growing Snake*. The rules of this game are [here](./rules/growing_snake.md)

We recommend that all game developers start with *Short Snake*. To help coders think about how to structure their code in an object oriented way, we have created this [step-by-step guide](./steps/coding_up_short_snake.md) to coding up *Short Snake*. We also provide a working version of the code in [this](./short_snake/) folder.

*Growing Snake* is harder but has much in common with *Short Snake*. Because of this, we do not provide a guide here. But, like for *Short Snake*, we do provide a working version of the game in [this](./growing_snake/) folder.

## Note
Our working versions of the game are _not_ meant to represent perfect code. Rather, they represent one interpretation of how to code up the games in a manner which is somewhat pedagogical with respect to OOP principles.

