from global_vars import *
from pygame.display import update
from pygame.math import clamp
from mathF.vector2 import Vector2
from consts import WORLD_WIDTH, WORLD_HEIGHT, DELTA_TIME

class Entity:
    position = Vector2(0, 0)
    size = Vector2(0, 0)
    velocity = Vector2(0, 0)

    def __init__(self):
        g_Entities.append(self)

    def draw(self):
        pass

    def update(self):
        self.update_position()

    def update_position(self):
        self.position += self.velocity * DELTA_TIME
        self.position.clamp(Vector2(-WORLD_WIDTH,-WORLD_HEIGHT), Vector2(WORLD_WIDTH,WORLD_HEIGHT))
    
    def set_position(self, vector2):
        self.position = vector2

    def set_size(self, vector2):
        self.size = vector2