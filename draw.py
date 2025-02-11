import pygame
from consts import SCREEN_WIDTH, SCREEN_HEIGHT
import global_vars as gv
from mathF.vector2 import *
from camera import *

def rect(screen, color, rect):
    world_x = rect.left
    world_y = rect.top
    screen_pos = world_to_screen(Vector2(world_x, world_y), gv.Camera.position)
    rect.left = screen_pos.x
    rect.top = screen_pos.y
    pygame.draw.rect(screen, color, rect)

def circle(screen, color, pos, radius):
    screen_pos = world_to_screen(pos, gv.Camera.position)
    pygame.draw.circle(screen, color, (screen_pos.x, screen_pos.y), radius)