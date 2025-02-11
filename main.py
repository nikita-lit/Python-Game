import pygame
import random
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, FPS, DELTA_TIME
import global_vars as gv
from player import *
from mathF.vector2 import *
from camera import *

pygame.init()

def run():
    gv.Font = pygame.font.Font(None, 36)
    gv.Font2 = pygame.font.Font(None, 22)
    clock = pygame.time.Clock()

    gv.Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Python Game")

    gv.Running = True

    gv.Camera = Camera()
    gv.Player = Player()
    gv.Player.set_size(Vector2(35,35))

    for i in range(5):
        x = random.randint(-WORLD_WIDTH, WORLD_WIDTH)
        y = random.randint(-WORLD_HEIGHT, WORLD_HEIGHT)
        test_entity = Entity(Vector2(x, y))
        test_entity.set_size(Vector2(15, 15))

    while gv.Running:
        gv.Screen.fill((100,100,100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gv.Running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            gv.Player.position = Vector2()
            gv.Camera.position = Vector2()

        draw.rect((45,45,45), pygame.Rect(-WORLD_WIDTH, -WORLD_HEIGHT, (WORLD_WIDTH+WORLD_WIDTH), (WORLD_HEIGHT+WORLD_HEIGHT)), 5)

        gv.Entities.sort(key=lambda ent:ent.position.y)

        for ent in gv.Entities:
            ent.draw()
            if not isinstance(ent, Player):
                ent.set_position( Vector2.move_towards(ent.position, gv.Player.position, 100 * DELTA_TIME) )

            draw.world_text(f"Pos: {ent.position}", ent.position, gv.Font2, True, (0,0,0))

        draw.screen_text(f"Cam pos: {gv.Camera.position}", Vector2(10,10), gv.Font, True, (0,0,0))
        draw.screen_text(f"FPS: {int(clock.get_fps())}", Vector2(10,50), gv.Font, True, (0,0,0))

        gv.Camera.update()
        gv.Player.update()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

run()