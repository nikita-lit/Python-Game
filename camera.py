import pygame
from pygame.math import clamp
import global_vars as gv
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, DELTA_TIME
from mathF.vector2 import Vector2

class Camera():
    position = Vector2(0, 0)
    zoom = 1.0;

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.position.y -= screen_scale(400) * DELTA_TIME
        if keys[pygame.K_DOWN]:
            self.position.y += screen_scale(400) * DELTA_TIME
        if keys[pygame.K_LEFT]:
            self.position.x -= screen_scale(400) * DELTA_TIME
        if keys[pygame.K_RIGHT]:
            self.position.x += screen_scale(400) * DELTA_TIME

        if keys[pygame.K_PLUS]:
            self.zoom += 0.5 * DELTA_TIME
        if keys[pygame.K_MINUS]:
            self.zoom -= 0.5 * DELTA_TIME

        self.zoom = clamp(self.zoom, 0.3, 2)

    def adjust_position_for_zoom(self):
        camera_center = self.position + Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.position = camera_center - Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) * self.zoom

def clamp_camera(camera_pos: Vector2):
    camera_pos.x = max(0, min(camera_pos.x, WORLD_WIDTH - SCREEN_WIDTH))
    camera_pos.y = max(0, min(camera_pos.y, WORLD_HEIGHT - WORLD_HEIGHT))
    return camera_pos

def world_to_screen(world_pos: Vector2):
    relative_pos = world_pos - gv.Camera.position
    screen_pos = relative_pos * gv.Camera.zoom
    screen_pos.x += SCREEN_WIDTH / 2
    screen_pos.y += SCREEN_HEIGHT / 2
    return screen_pos

def screen_to_world(screen_pos: Vector2):
    relative_pos = screen_pos - Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    world_pos = relative_pos / gv.Camera.zoom
    world_pos += gv.Camera.position
    return world_pos

def get_mouse_world_pos():
    mouse_pos = pygame.mouse.get_pos()
    return screen_to_world(Vector2(mouse_pos[0], mouse_pos[1]))

def screen_scale(scale: float):
    return scale * gv.Camera.zoom