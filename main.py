import pygame
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, FPS, DELTA_TIME
import global_vars as gv
from player import *
from mathF.vector2 import *
from camera import *

pygame.init()

def run():
    gv.Font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    gv.Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame")

    gv.Running = True

    gv.Camera = Camera()
    gv.Player = Player()
    gv.Player.set_size(Vector2(35,35))

    test_entity = Entity(Vector2(300, 300))

    while gv.Running:
        gv.Screen.fill((100,100,100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gv.Running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            gv.Camera.position.y -= 700 * DELTA_TIME
        if keys[pygame.K_DOWN]:
            gv.Camera.position.y += 700 * DELTA_TIME
        if keys[pygame.K_LEFT]:
            gv.Camera.position.x -= 700 * DELTA_TIME
        if keys[pygame.K_RIGHT]:
            gv.Camera.position.x += 700 * DELTA_TIME

        if keys[pygame.K_r]:
            gv.Player.position = Vector2()
            gv.Camera.position = Vector2()

        draw.rect(gv.Screen, (45,45,45), pygame.Rect(-WORLD_WIDTH, -WORLD_HEIGHT, (WORLD_WIDTH*2), (WORLD_HEIGHT*2)) )

        gv.Entities.sort(key=lambda obj: obj.position.y)

        for ent in gv.Entities:
            ent.draw(gv.Screen)
            ent_text = gv.Font.render(f"Pos: {ent.position}", True, (0,0,0))

            screen_pos = world_to_screen(ent.position, gv.Camera.position)
            gv.Screen.blit(ent_text, (screen_pos.x, screen_pos.y))

        pos_text = gv.Font.render(f"Cam pos: {gv.Camera.position}", True, (0,0,0))
        gv.Screen.blit(pos_text, (10, 10))

        gv.Player.update()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

run()