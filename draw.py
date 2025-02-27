import pygame
import global_vars as gv
from consts import SCREEN_WIDTH, SCREEN_HEIGHT
from mathF.vector2 import *
from camera import *

def rect(color, rect: pygame.Rect, width: int = 0):
    screen_pos = world_to_screen(Vector2(rect.x, rect.y))
    rect.width = screen_scale(rect.width)
    rect.height = screen_scale(rect.height)
    rect.x = screen_pos.x
    rect.y = screen_pos.y
    pygame.draw.rect(gv.Screen, color, rect, width)

def circle(color, pos: Vector2, radius: float, width: int = 0):
    screen_pos = world_to_screen(pos)
    pygame.draw.circle(gv.Screen, color, (screen_pos.x, screen_pos.y), screen_scale(radius), int(screen_scale(width)))

def world_text(text: str, pos: Vector2, font: pygame.font.Font, antialias: bool, color):
    text_render = font.render(text, antialias, color)
    screen_pos = world_to_screen(pos)
    gv.Screen.blit(text_render, (screen_pos.x, screen_pos.y))
    
def screen_text(text: str, pos: Vector2, font: pygame.font.Font, antialias: bool, color):
    text_render = font.render(text, antialias, color)
    gv.Screen.blit(text_render, (pos.x, pos.y))
