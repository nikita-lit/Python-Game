import pygame
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, FPS
from global_vars import *
from player import *
from mathF.vector2 import *
from camera import *

pygame.init()

def run():
    g_Font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    g_Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame")

    g_Running = True

    g_Camera = Camera()
    g_Player = Player()
    g_Player.set_size(Vector2(45,45))

    while g_Running:
        g_Screen.fill((100,100,100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g_Running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            g_Camera.position.y -= 5
        if keys[pygame.K_DOWN]:
            g_Camera.position.y += 5
        if keys[pygame.K_LEFT]:
            g_Camera.position.x -= 5
        if keys[pygame.K_RIGHT]:
            g_Camera.position.x += 5

        for ent in g_Entities:
            world_pos = ent.position
            screen_pos = world_to_screen(world_pos, g_Camera.position)

            pygame.draw.circle(g_Screen, (255, 0, 0), (screen_pos.x, screen_pos.y), 10)
            ent_text = g_Font.render(f"Pos: {world_pos}", True, (0,0,0))
            g_Screen.blit(ent_text, (screen_pos.x, screen_pos.y))

        pos_text = g_Font.render(f"Cam pos: {g_Camera.position}", True, (0,0,0))
        g_Screen.blit(pos_text, (10, 10))

        g_Player.update()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

run()