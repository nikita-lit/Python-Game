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
    position = Vector2()
    rect = None
    velocity = Vector2()
    wish_velocity = Vector2()
    friction = 15
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
        self.velocity = Vector2.lerp(self.velocity, self.wish_velocity, (self.friction/100))
        self.position += self.velocity * DELTA_TIME
        self.position.clamp(Vector2(-WORLD_WIDTH,-WORLD_HEIGHT), Vector2(WORLD_WIDTH,WORLD_HEIGHT))

        #for ent in gv.Entities:
            #if ents_collide(self, ent):

    def move_to(self, ent, speed):
        direction = Vector2.direction(self.position, ent.position)
        #if not direction.is_near_to_zero():
            #self.wish_velocity = direction * speed
    
    def set_position(self, vector2):
        self.position = vector2

    def set_rect(self, _rect):
        self.rect = _rect
        