import math

import pygame
import pygame.gfxdraw
import time

from settings import GameSettings, PlayerSettings
from tile_play.drawing import draw_player, change_color, draw, draw_all, draw_texture_player_idle, \
    draw_texture_player_walk, draw_attack_1
from tile_play.movement import graviation, handle_player_y, handle_player_x

pygame.init()

screen = pygame.display.set_mode((GameSettings.screen_width, GameSettings.screen_height))
pygame.display.set_caption("My Game")


def main():
    clock = pygame.time.Clock()
    game_timer = 0

    jump = 0
    attack = 0

    player = PlayerSettings(GameSettings.screen_width / 2, GameSettings.screen_height / 2)
    running = True
    while running:
        game_timer += 1
        # print(game_timer)
        keys = pygame.key.get_pressed()
        if keys:
            handle_player_x(player, keys)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    handle_player_y(player, event)
                if event.key == pygame.K_q:
                    attack = 1
                    attack_timer = 0
            elif event.type == pygame.QUIT:
                running = False

        graviation(player, 650)

        for x_pos in range((GameSettings.screen_width // GameSettings.tile_size) * 2):
            draw(screen, [x_pos * 100, 540])

        if player.course != 0:
            draw_texture_player_walk(screen, player, game_timer // 10)
        elif attack != 0:
            attack_timer += 1
            if attack_timer//6 != 0:
                attack = attack_timer//6
            if attack == 6:
                attack = 0

            # print(attack)

            draw_attack_1(screen, player, attack)
        else:
            draw_texture_player_idle(screen, player, 0)
            # draw_attack_1(screen, player, 0)

        pygame.display.flip()
        clock.tick(5)

    pygame.quit()


if __name__ == "__main__":
    main()
