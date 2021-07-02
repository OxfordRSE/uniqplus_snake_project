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
        self.body = [bone]
        self.direction = [0, 0]
        self.size = size

    def change_direction(self, direction):
        self.direction = direction

    def draw(self, screen):
        for bone in self.body:
            bone.draw(screen)

    def eats_itself(self, new_head_pos):
        # Check if new head pos coincides with any of the bones
        if len(self.body) > 1:
            if new_head_pos in [bone.pos for bone in self.body]:
                return True
        else:
            False

    def get_head_pos(self):
        return self.body[-1].pos

    def get_new_head_pos(self):
        current_head_pos = self.get_head_pos()
        new_head_pos = (
            current_head_pos[0] + self.direction[0] * self.size,
            current_head_pos[1] + self.direction[1] * self.size,
        )
        return new_head_pos

    def grow(self):
        new_head_pos = self.get_new_head_pos()
        head = Bone(new_head_pos, self.size)
        self.body.append(head)

    def hits_side(self, head_pos, screen_width, screen_height):
        # needs negative here for latter since head_pos[0] is left side
        if head_pos[0] == screen_width or head_pos[0] == -self.size:
            return True
        # needs negative here for latter since head_pos[1] is top side
        if head_pos[1] == screen_height or head_pos[1] == -self.size:
            return True
        return False

    def move_and_survive(self, screen_width, screen_height):
        new_head_pos = self.get_new_head_pos()
        has_eaten_itself = self.eats_itself(new_head_pos)
        if has_eaten_itself:
            return False
        has_hit_side = self.hits_side(new_head_pos, screen_width, screen_height)
        if has_hit_side:
            return False
        head = Bone(new_head_pos, self.size)
        self.body.append(head)
        self.body.pop(0)
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
