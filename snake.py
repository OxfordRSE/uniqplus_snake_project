import pdb
import pygame

WHITE = (255, 255, 255)

class Snake:
    def __init__(self, position, size=10):
        bone = Bone(position, size)
        self.body = [bone]
        self.direction = [0, 0]
        self.size = size

    def draw(self, screen):
        for bone in self.body:
            bone.draw(screen)

    def change_direction(self, direction):
        self.direction = direction

    def update(self):
        direction = self.direction
        size = self.size
        current_head = self.body[0]
        current_pos = current_head.pos
        x = current_pos[0] + direction[0] * size
        y = current_pos[1] + direction[1] * size
        head = Bone([x, y], self.size)
        self.body.append(head)
        self.body.pop(0)


class Bone:
    def __init__(self, position, size):
        self.pos = position
        self.size = size

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, [self.pos[0], self.pos[1], self.size, self.size])

