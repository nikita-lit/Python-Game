import pygame
import camera as cam
import global_vars as gv
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, FPS
from player import Player
from mathF.vector2 import Vector2
from camera import Camera

pygame.init()

def run():
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    gv.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame")

    gv.running = True

    gv.camera = Camera()
    gv.player = Player()
    gv.player.set_size(Vector2(45,45))

    while gv.running:
        gv.screen.fill((100,100,100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gv.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            gv.camera.position.y -= 5
        if keys[pygame.K_DOWN]:
            gv.camera.position.y += 5
        if keys[pygame.K_LEFT]:
            gv.camera.position.x -= 5
        if keys[pygame.K_RIGHT]:
            gv.camera.position.x += 5

        #player.draw(screen)
        #player.update()

        pos_text = font.render(f"Pos: {gv.camera.position}", True, (0,0,0))
        #velocity_text = font.render(f"Vel: {player.velocity}", True, (0,0,0))
        #acc_text = font.render(f"Acc: {player.acceleration}", True, (0,0,0))
        gv.screen.blit(pos_text, (10, 10))
        #screen.blit(velocity_text, (10, 35))
        #screen.blit(acc_text, (10, 60))

        for obj in gv.game_objects:
            world_pos = obj.position
            screen_pos = cam.world_to_screen(world_pos, gv.camera.position)
            pygame.draw.circle(gv.screen, (255, 0, 0), (screen_pos.x, screen_pos.y), 10)
            obj_text = font.render(f"Pos: {world_pos}", True, (0,0,0))
            gv.screen.blit(obj_text, (screen_pos.x, screen_pos.y))

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

run()