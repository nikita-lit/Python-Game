from pygame.display import update
from pygame.math import clamp
from mathF.vector2 import Vector2
from consts import DELTA_TIME
from consts import WIDTH
from consts import HEIGHT

class GameObject:
    position = Vector2(0, 0)
    size = Vector2(0, 0)
    velocity = Vector2(0, 0)

    #def __init__(self):
        

    def draw(self):
        pass

    def update(self):
        self.update_position()

    def update_position(self):
        self.position += self.velocity * DELTA_TIME
        self.position.x = clamp(self.position.x, 0, (WIDTH - self.size.x))
        self.position.y = clamp(self.position.y, 0, (HEIGHT - self.size.y))
    
    def set_position(self, vector2):
        self.position = vector2

    def set_size(self, vector2):
        self.size = vector2