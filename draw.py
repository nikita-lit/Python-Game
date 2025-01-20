import pygame
from consts import SCREEN_WIDTH, SCREEN_HEIGHT

#scree scale
def ss(num):
    return num * (SCREEN_WIDTH / 640.0)

def ssH(num):
    return num * (SCREEN_HEIGHT / 480.0)