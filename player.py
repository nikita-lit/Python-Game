import pygame
import draw
from pygame.math import clamp
from entity import Entity
from mathF.vector2 import Vector2
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, DELTA_TIME

PLAYER_SPEED = 150
PLAYER_FRICTION = 15

class Player(Entity):
    wish_velocity = Vector2(0, 0)

    def __init__(self):
        super().__init__()

    def update(self):
        super().update()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.wish_velocity.x = -PLAYER_SPEED
        elif keys[pygame.K_d]:
            self.wish_velocity.x = PLAYER_SPEED
        else:
            self.wish_velocity.x = 0

        if keys[pygame.K_w]:
            self.wish_velocity.y = -PLAYER_SPEED
        elif keys[pygame.K_s]:
            self.wish_velocity.y = PLAYER_SPEED
        else:
            self.wish_velocity.y = 0

        if keys[pygame.K_r]:
            self.position = Vector2()

    def update_position(self):
        self.velocity = Vector2.lerp(self.velocity, self.wish_velocity, (PLAYER_FRICTION/100))
        self.position += self.velocity * DELTA_TIME
        self.position.clamp(Vector2(-WORLD_WIDTH,-WORLD_HEIGHT), Vector2(WORLD_WIDTH,WORLD_HEIGHT))

    def draw(self, screen):
        draw.rect(screen, (255,0,0), 
                    self.position.x, 
                    self.position.y, 
                    self.size.x, 
                    self.size.y)

