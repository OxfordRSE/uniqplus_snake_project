# Programming snake in Python using object oriented programming

This repository represents a day long project providing an introduction to object oriented programming (OOP) in Python. The aim of the project is to code up a version of the once popular mobile game *snake* using OOP principles.

## What is snake?
[Snake](https://en.wikipedia.org/wiki/Snake_(video_game_genre)) is a common name for a game in which a player maneuvers a line which grows in length, where the main obstacle is the line itself. Although variants existed before, it became popular in the late 1990s when it was preloaded onto Nokia phones.

![example screenshot](https://www.silicon.co.uk/wp-content/uploads/2012/08/snakenokia3310.jpg)

## What are the rules of our snake game?
1. The snake begins as a single bone in the middle of the screen.
2. The player selects a direction for their snake to move (up, down, left or right) using the arrow keys.
3. If the snake encounters food, it grows by one bone.
4. If the snake hits itself, it dies.
5. If the snake hits the side of the domain, it dies.

## Other game characteristics
- Food appears at the start of the game in a random location on the screen.
- Each time a piece of food is eaten, another piece of food appears at a random location on the screen.

## How to get started
In this project, we are going to use the Python package `pygame`. To install it, you can run:

`pip install pygame`

from the command line. Note that this requires you to have the command line tool `pip` installed (see [here](https://pip.pypa.io/en/stable/installing/) for instructions on this).