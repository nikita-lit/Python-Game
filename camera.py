from mathF.vector2 import Vector2

class Camera():
    position = Vector2(0, 0)

    @staticmethod
    def clamp_camera(camera_x, camera_y, world_width, world_height, screen_width, screen_height):
        camera_x = max(0, min(camera_x, world_width - screen_width))
        camera_y = max(0, min(camera_y, world_height - screen_height))
        return camera_x, camera_y

    @staticmethod
    def world_to_screen(world_x, world_y, camera_x, camera_y):
        screen_x = world_x - camera_x
        screen_y = world_y - camera_y
        return screen_x, screen_y