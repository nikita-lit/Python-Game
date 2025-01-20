from mathF.vector2 import Vector2
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT

class Camera():
    position = Vector2(0, 0)

def clamp_camera(camera_pos):
    camera_pos.x = max(0, min(camera_pos.x, WORLD_WIDTH - SCREEN_WIDTH))
    camera_pos.y = max(0, min(camera_pos.y, WORLD_HEIGHT - WORLD_HEIGHT))
    return camera_pos

def world_to_screen(world_pos, camera_pos):
    screen_pos = world_pos - camera_pos
    return screen_pos