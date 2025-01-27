import pygame
import global_vars as gv
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, DELTA_TIME
from mathF.vector2 import Vector2

class Camera():
    position = Vector2(0, 0)
    zoom = 0.0;

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            gv.Camera.position.y -= 400 * DELTA_TIME
        if keys[pygame.K_DOWN]:
            gv.Camera.position.y += 400 * DELTA_TIME
        if keys[pygame.K_LEFT]:
            gv.Camera.position.x -= 400 * DELTA_TIME
        if keys[pygame.K_RIGHT]:
            gv.Camera.position.x += 400 * DELTA_TIME

def clamp_camera(camera_pos):
    camera_pos.x = max(0, min(camera_pos.x, WORLD_WIDTH - SCREEN_WIDTH))
    camera_pos.y = max(0, min(camera_pos.y, WORLD_HEIGHT - WORLD_HEIGHT))
    return camera_pos

def world_to_screen(world_pos):
    screen_pos = world_pos - (gv.Camera.position + Vector2(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2))
    return screen_pos