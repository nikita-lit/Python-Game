import pygame
import global_vars as gv
from consts import SCREEN_WIDTH, SCREEN_HEIGHT
from mathF.vector2 import *
from camera import *

def rect(rect: pygame.Rect, width: int = 1, color = (255, 255, 255)):
    screen_pos = world_to_screen(Vector2(rect.x, rect.y))
    rect.width = screen_scale(rect.width)
    rect.height = screen_scale(rect.height)
    rect.x = screen_pos.x
    rect.y = screen_pos.y
    pygame.draw.rect(gv.Screen, color, rect, width)

def circle(pos: Vector2, radius: float = 5, color = (255, 255, 255), width: int = 0):
    screen_pos = world_to_screen(pos)
    pygame.draw.circle(gv.Screen, color, (screen_pos.x, screen_pos.y), screen_scale(radius), int(screen_scale(width)))

def line(start_pos: Vector2, end_pos: Vector2, width: int = 1, color = (255, 255, 255)):
    screen_start_pos = world_to_screen(start_pos)
    screen_end_pos = world_to_screen(end_pos)
    pygame.draw.line(gv.Screen, (255, 255, 0), (screen_start_pos.x, screen_start_pos.y), (screen_end_pos.x, screen_end_pos.y), int(screen_scale(width)))

def world_text(text: str, pos: Vector2, font: pygame.font.Font, antialias: bool, color):
    text_render = font.render(text, antialias, color)
    screen_pos = world_to_screen(pos)
    gv.Screen.blit(text_render, (screen_pos.x, screen_pos.y))
    
def screen_text(text: str, pos: Vector2, font: pygame.font.Font, antialias: bool, color):
    text_render = font.render(text, antialias, color)
    gv.Screen.blit(text_render, (pos.x, pos.y))
