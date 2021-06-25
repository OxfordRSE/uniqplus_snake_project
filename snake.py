import pygame
import random

WHITE = (255, 255, 255)


class SnakeEatsItselfException(Exception):
    pass


class Snake:
    def __init__(self, position, size=20):
        bone = Bone(position, size)
        bone2 = Bone((position[0] + 20, position[1]), size)
        self.body = [bone, bone2]
        self.direction = [0, 0]
        self.size = size

    def get_head_pos(self):
        return self.body[-1].pos

    def grow(self):
        direction = self.direction
        size = self.size
        current_head = self.body[-1]
        current_pos = current_head.pos
        new_head_pos = (
            current_pos[0] + direction[0] * size,
            current_pos[1] + direction[1] * size
        )
        # Check if new head pos coincides with any of the bones
        if new_head_pos in [bone.pos for bone in self.body]:
            raise SnakeEatsItselfException
        head = Bone(new_head_pos, self.size)
        self.body.append(head)

    def draw(self, screen):
        for bone in self.body:
            bone.draw(screen)

    def change_direction(self, direction):
        self.direction = direction

    def update(self):
        direction = self.direction
        size = self.size
        current_head = self.body[-1]
        current_pos = current_head.pos
        new_head_pos = (
            current_pos[0] + direction[0] * size,
            current_pos[1] + direction[1] * size
        )
        # Check if new head pos coincides with any of the bones except
        # tail (removed)
        if new_head_pos in [bone.pos for bone in self.body[1:]]:
            raise SnakeEatsItselfException
        head = Bone(new_head_pos, self.size)
        self.body.append(head)
        self.body.pop(0)


class Bone:
    def __init__(self, position, size):
        self.pos = position
        self.size = size

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, [self.pos[0], self.pos[1], self.size, self.size])


class Food:
    def __init__(self, screen_width, screen_height, size=20):
        x = round(random.randrange(0, screen_width - size)/size) * size
        y = round(random.randrange(0, screen_height - size)/size) * size
        self.bone = Bone((x, y), size)

    def draw(self, screen):
        self.bone.draw(screen)

    def get_pos(self):
        return self.bone.pos
