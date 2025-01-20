import pygame
import draw
from consts import WIDTH
from consts import HEIGHT
from consts import FPS
from player import Player
from mathF.vector2 import Vector2

pygame.init()

running = False
screen = None
player = None

print(draw.ss(5))

def run():
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame")

    running = True
    player = Player()
    player.set_size(Vector2(draw.ss(25),draw.ss(25)))

    while running:
        screen.fill((100,100,100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.draw(screen)
        player.update()

        pos_text = font.render(f"Pos: {player.position}", True, (0,0,0))
        velocity_text = font.render(f"Vel: {player.velocity}", True, (0,0,0))
        acc_text = font.render(f"Acc: {player.acceleration}", True, (0,0,0))
        screen.blit(pos_text, (10, 10))
        screen.blit(velocity_text, (10, 35))
        screen.blit(acc_text, (10, 60))

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

run()