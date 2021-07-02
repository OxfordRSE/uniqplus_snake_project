import pygame
import random

WHITE = (255, 255, 255)


def losing_message(msg, screen, screen_width, screen_height):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, WHITE)
    screen.blit(mesg, [screen_width/2, screen_height/2])
    

def score_message(score, screen, screen_width, screen_height):
    font_style = pygame.font.SysFont(None, 50)
    value = font_style.render("Your Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])


class Snake:
    def __init__(self, position, size=20):
        bone = Bone(position, size)
        self.body = bone
        self.direction = [0, 0]
        self.size = size

    def change_direction(self, direction):
        self.direction = direction

    def draw(self, screen):
        self.body.draw(screen)

    def get_new_pos(self):
        current_pos = self.get_pos()
        new_pos = (
            current_pos[0] + self.direction[0] * self.size,
            current_pos[1] + self.direction[1] * self.size,
        )
        return new_pos
    
    def get_pos(self):
        return self.body.pos

    def hits_side(self, pos, screen_width, screen_height):
        # needs negative here for latter since pos[0] is left side
        if pos[0] == screen_width or pos[0] == -self.size:
            return True
        # needs negative here for latter since pos[0] is topside
        if pos[1] == screen_height or pos[1] == -self.size:
            return True
        return False

    def move_and_survive(self, screen_width, screen_height):
        new_pos = self.get_new_pos()
        has_hit_side = self.hits_side(new_pos, screen_width, screen_height)
        if has_hit_side:
            return False
        moved_bone = Bone(new_pos, self.size)
        self.body = moved_bone
        return True


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
