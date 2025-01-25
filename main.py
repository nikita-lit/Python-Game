import pygame
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, FPS
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
    gv.Player.set_size(Vector2(45,45))

    test_entity = Entity(Vector2(300, 300))

    while gv.Running:
        gv.Screen.fill((100,100,100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gv.Running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            gv.Camera.position.y -= 5
        if keys[pygame.K_DOWN]:
            gv.Camera.position.y += 5
        if keys[pygame.K_LEFT]:
            gv.Camera.position.x -= 5
        if keys[pygame.K_RIGHT]:
            gv.Camera.position.x += 5

        if keys[pygame.K_r]:
            gv.Player.position = Vector2()
            gv.Camera.position = Vector2()

        scene_screen_pos = world_to_screen(Vector2(-WORLD_WIDTH, -WORLD_HEIGHT), gv.Camera.position)
        pygame.draw.rect(gv.Screen, (45,45,45), pygame.Rect(scene_screen_pos.x, scene_screen_pos.y, (WORLD_WIDTH+WORLD_WIDTH), (WORLD_HEIGHT+WORLD_HEIGHT)))

        for ent in gv.Entities:
            world_pos = ent.position
            screen_pos = world_to_screen(world_pos, gv.Camera.position)

            pygame.draw.circle(gv.Screen, (255, 0, 0), (screen_pos.x, screen_pos.y), 10)
            ent_text = gv.Font.render(f"Pos: {world_pos}", True, (0,0,0))
            gv.Screen.blit(ent_text, (screen_pos.x, screen_pos.y))

        pos_text = gv.Font.render(f"Cam pos: {gv.Camera.position}", True, (0,0,0))
        gv.Screen.blit(pos_text, (10, 10))

        gv.Player.update()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

run()