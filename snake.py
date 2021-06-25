import pygame
import random

WHITE = (255, 255, 255)


class SnakeEatsItselfException(Exception):
    pass


class Snake:
    def __init__(self, position, size=20):
        head = Bone(position, size)
        tail = Bone((position[0] + size, position[1]), size)
        self.body = [tail, head]
        self.direction = [1, 0]
        self.size = size

    def get_head_pos(self):
        return self.body[-1].pos

    def get_new_head_pos(self):
        current_head_pos = self.get_head_pos()
        new_head_pos = (
            current_head_pos[0] + self.direction[0] * self.size,
            current_head_pos[1] + self.direction[1] * self.size,
        )
        return new_head_pos

    def change_direction(self, direction):
        self.direction = direction

    def update(self):
        self.body.pop(0)
        self.grow()

    def grow(self):
        new_head_pos = self.get_new_head_pos()
        # Check if new head pos coincides with any of the bones
        if new_head_pos in [bone.pos for bone in self.body]:
            raise SnakeEatsItselfException
        head = Bone(new_head_pos, self.size)
        self.body.append(head)

    def draw(self, screen):
        for bone in self.body:
            bone.draw(screen)


class Bone:
    def __init__(self, position, size):
        self.pos = position
        self.size = size

    def draw(self, screen):
        pygame.draw.rect(
            screen, WHITE, [self.pos[0], self.pos[1], self.size, self.size]
        )


class Food:
    def __init__(self, screen_width, screen_height, size=20):
        x = round(random.randrange(0, screen_width - size) / size) * size
        y = round(random.randrange(0, screen_height - size) / size) * size
        self.bone = Bone((x, y), size)

    def draw(self, screen):
        self.bone.draw(screen)

    def get_pos(self):
        return self.bone.pos
