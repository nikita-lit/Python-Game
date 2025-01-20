import pygame
from consts import WIDTH
from consts import HEIGHT

#scree scale
def ss(num):
    return num * (WIDTH / 640.0)

def ssH(nusm):
    return num * (HEIGHT / 480.0)

def rect(screen, color, x, y, w, h):
    pygame.draw.rect(screen, color, 
                    (normalize_screenX(x), 
                    normalize_screenY(y), 
                    w, 
                    h))

def normalize_screenX(x):
    return (x*WIDTH) 

def normalize_screenY(y):
    return (y*HEIGHT) 