import draw
import math
import global_vars as gv
import pygame
from mathF.vector2 import Vector2
from consts import WORLD_WIDTH, WORLD_HEIGHT, DELTA_TIME

def ents_collide(ent1, ent2):
    rect1 = ent1.rect
    rect2 = ent2.rect

    return (
        ent1.position.x < ent2.position.x + rect2.width and
        ent1.position.x + rect1.width > ent2.position.x and
        ent1.position.y < ent2.position.y + rect2.height and
        ent1.position.y + rect1.height > ent2.position.y
    )

class Entity:
    position = Vector2(0, 0)
    rect = None
    velocity = Vector2(0, 0)
    name = ""

    def __init__(self, _rect, _position = Vector2()):
        gv.Entities.append(self)
        self.name = self.__class__
        self.position = _position
        self.rect = _rect

    def draw(self):
        draw.rect(pygame.Rect(self.position.x, self.position.y, self.rect.width, self.rect.height), 0, (255,0,0))

    def update(self):
        self.update_position()

    def update_position(self):
        self.position += self.velocity * DELTA_TIME
        self.position.clamp(Vector2(-WORLD_WIDTH,-WORLD_HEIGHT), Vector2(WORLD_WIDTH,WORLD_HEIGHT))

        for ent in gv.Entities:
            if ents_collide(self, ent):
                direction = self.position - ent.position
                print(direction)
    
    def set_position(self, vector2):
        self.position = vector2

    def set_rect(self, _rect):
        self.rect = _rect
        