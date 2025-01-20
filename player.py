import pygame
import draw
from pygame.math import clamp
from mathF.vector2 import Vector2
from game_object import GameObject
from consts import WIDTH
from consts import HEIGHT
from consts import DELTA_TIME

PLAYER_SPEED = 150
PLAYER_FRICTION = 15

class Player(GameObject):
    acceleration = Vector2(0,0)

    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and self.position.x > 0:
            self.velocity.x = -PLAYER_SPEED
        elif keys[pygame.K_d] and self.position.x < (WIDTH - self.size.x):
            self.velocity.x = PLAYER_SPEED
        else:
            self.velocity.x = 0

        if keys[pygame.K_w] and self.position.y > 0:
            self.velocity.y = -PLAYER_SPEED
        elif keys[pygame.K_s] and self.position.y < (HEIGHT - self.size.y):
            self.velocity.y = PLAYER_SPEED
        else:
            self.velocity.y = 0

    def update_position(self):
        self.acceleration = Vector2.lerp(self.acceleration, self.velocity, (PLAYER_FRICTION/100))
        self.position += self.acceleration * DELTA_TIME
        self.position.x = clamp(self.position.x, 0, (WIDTH - self.size.x))
        self.position.y = clamp(self.position.y, 0, (HEIGHT - self.size.y))

    def draw(self, screen):
        draw.rect(screen, (255,0,0), 
                    self.position.x, 
                    self.position.y, 
                    self.size.x, 
                    self.size.y)

