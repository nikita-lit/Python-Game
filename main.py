import pygame
import camera
from camera import Camera
from consts import SCREEN_WIDTH, SCREEN_HEIGHT, WORLD_WIDTH, WORLD_HEIGHT, FPS
from player import Player
from mathF.vector2 import Vector2

pygame.init()

running = False
screen = None
player = None
camera = Camera()

objects = [(100, 100), (500, 500), (1500, 1500)]

game_objects = []

def run():
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame")

    running = True
    player = Player()
    player.set_size(Vector2(45,45))

    while running:
        screen.fill((100,100,100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            camera.position.y -= 5
        if keys[pygame.K_DOWN]:
            camera.position.y += 5
        if keys[pygame.K_LEFT]:
            camera.position.x -= 5
        if keys[pygame.K_RIGHT]:
            camera.position.x += 5

        #player.draw(screen)
        #player.update()

        pos_text = font.render(f"Pos: {camera.position}", True, (0,0,0))
        #velocity_text = font.render(f"Vel: {player.velocity}", True, (0,0,0))
        #acc_text = font.render(f"Acc: {player.acceleration}", True, (0,0,0))
        screen.blit(pos_text, (10, 10))
        #screen.blit(velocity_text, (10, 35))
        #screen.blit(acc_text, (10, 60))

        for obj in game_objects:
            world_pos = obj.position
            screen_x, screen_y = camera.world_to_screen(world_pos.x, world_pos.y, camera.position.x, camera.position.y)
            pygame.draw.circle(screen, (255, 0, 0), (int(screen_x), int(screen_y)), 10)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

run()