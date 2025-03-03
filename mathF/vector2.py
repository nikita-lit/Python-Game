import string
import math
from pygame.math import clamp

class Vector2():
   x = 0.0
   y = 0.0

   def __init__(self, _x = 0.0, _y = 0.0):
       self.x = _x
       self.y = _y

   def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

   def clamp(self, vec1, vec2):
       self.x = clamp(self.x, vec1.x, vec2.x)
       self.y = clamp(self.y, vec1.y, vec2.y)

   def normalize(self):
        length = self.length()
        if length == 0:
            return Vector2(0, 0)
        return Vector2(self.x / length, self.y / length)

   def __add__(self, vec):
       if not isinstance(vec, Vector2):
           return
           
       return Vector2(self.x+vec.x,self.y+vec.y)

   def __sub__(self, vec):
       if not isinstance(vec, Vector2):
           if isinstance(vec, float) or isinstance(vec, int):
               return Vector2(self.x-vec,self.y-vec)
           else:
               return

       return Vector2(self.x-vec.x,self.y-vec.y)

   def __truediv__(self, div):
       return Vector2(self.x/div,self.y/div)

   def __mul__(self, scalar):
       return Vector2(self.x*scalar,self.y*scalar)

   def __str__(self) -> str:
       return f"{round(self.x, 3)}, {round(self.y, 3)}"

   @staticmethod
   def lerp(start, target, t):
        return start + (target - start) * t

   @staticmethod
   def move_towards(start, target, speed):
       direction = Vector2(target.x - start.x, target.y - start.y)
       distance = math.sqrt(direction.x**2 + direction.y**2)

       if distance < speed:
           return target

       direction.x /= distance
       direction.y /= distance
       start += direction * speed
        
       return start




