# Programming snake in Python using object oriented programming

This repository represents a day long project providing an introduction to object oriented programming (OOP) in Python. The aim of the project is to code up a version of the once popular mobile game *snake* using OOP principles.

## What is snake?
[Snake](https://en.wikipedia.org/wiki/Snake_(video_game_genre)) is a common name for a game in which a player maneuvers a line which grows in length, where the main obstacle is the line itself. Although variants existed before, it became popular in the late 1990s when it was preloaded onto Nokia phones.

![example screenshot](https://www.silicon.co.uk/wp-content/uploads/2012/08/snakenokia3310.jpg)

## Our snake games
Here, we offer two possible variants of the game of increasing difficulty:

1. *Short Snake*. The rules of this game are [here](./rules/short_snake.md)
2. *Growing Snake*. The rules of this game are [here](./rules/growing_snake.md)

We recommend that all game developers start with *Short Snake* before moving on to *Growing Snake*.

## Installing pygame
In this project, we are going to use the Python package `pygame`. To install it, you can run:

`pip install pygame`

from the command line. Note that this requires you to have the command line tool `pip` installed (see [here](https://pip.pypa.io/en/stable/installing/) for instructions on this).

## Getting started with pygame
To help get you acquainted with pygame and to give some guidance of the task, we have created the following short vignettes:
- [Setting up a blank canvas](./steps/blank_screen.md)
- [Drawing on the canvas](./steps/drawing.md)
- [Accessing the keys pressed by a user](./steps/keys.md)
- [Moving a rectangle across the canvas using the keys](./steps/moving.md)
- [Controlling the game speed](./steps/speed.md)
