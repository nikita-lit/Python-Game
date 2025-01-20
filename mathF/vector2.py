import string
import math

class Vector2():
   def __init__(self, _x, _y):
       self.x = _x
       self.y = _y

   def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

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
           return

       return Vector2(self.x-vec.x,self.y-vec.y)

   def __mul__(self, scalar):
       return Vector2(self.x*scalar,self.y*scalar)

   def __str__(self) -> str:
       return f"{round(self.x, 3)}, {round(self.y, 3)}"

   @staticmethod
   def lerp(start, target, t):
        return start + (target - start) * t
    
   x = 0.0
   y = 0.0




