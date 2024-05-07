import pygame

from tile_play.settings import PlayerSettings


def graviation(player: PlayerSettings, floor):
    next_pos_y = player.get_y() + player.speed_y  # + player.g_speed
    if next_pos_y + player.height >= floor:
        player.player_position[1] = floor - player.height
        player.speed_y = 0
    else:
        player.speed_y += player.g_speed
        player.player_position[1] = next_pos_y


def handle_player_y(player: PlayerSettings, event):
    # if event.key == pygame.K_LEFT:
    #     player.player_position[0] -= player.speed
    # elif event.key == pygame.K_RIGHT:
    #     player.player_position[0] += player.speed
    if event.key == pygame.K_UP:
        if player.speed_y == 0:
            player.double_jump = True
            player.speed_y = - player.jump_power
        elif player.double_jump:
            player.double_jump = False
            player.speed_y = - player.jump_power


def handle_player_x(player: PlayerSettings, keys):
    if keys[pygame.K_LEFT]:
        player.player_position[0] -= player.speed
        player.course = 'left'
    elif keys[pygame.K_RIGHT]:
        player.player_position[0] += player.speed
        player.course = 'right'
    else:
        player.course = 0
