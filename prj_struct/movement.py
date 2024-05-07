import pygame

from prj_struct.map import lvl_4
from prj_struct.settings import PlayerSettings, GameSettings

vector_list = {
    'L': ['Left', ['L', 'R']],
    'U': ['Up', ['U', 'D']],
    'R': ['Right', ['L', 'R']],
    'D': ['Down', ['U', 'D']],
}


# def handle_movement(player_position):
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 player_position = (player_position[0] - 1, player_position[1])
#             elif event.key == pygame.K_RIGHT:
#                 player_position = (player_position[0] + 1, player_position[1])
#             elif event.key == pygame.K_UP:
#                 player_position = (player_position[0], player_position[1] - 1)
#             elif event.key == pygame.K_DOWN:
#                 player_position = (player_position[0], player_position[1] + 1)
#     return player_position


def handle_player_speed_with_stop(player: PlayerSettings, event):
    # print(player.speed_x, player.speed_y)
    # for event in pygame.event.get():
    # if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        player.speed_y = 0
        # print("LEFT")
        if player.speed_x <= 0:
            player.speed_x = -player.speed
        elif player.speed_x > 0:
            player.speed_x = 0
    elif event.key == pygame.K_RIGHT:
        player.speed_y = 0
        # print('RIGHT')
        if player.speed_x >= 0:
            player.speed_x = player.speed
        elif player.speed_x < 0:
            player.speed_x = 0
    elif event.key == pygame.K_UP:
        player.speed_x = 0
        # print('UP')
        if player.speed_y <= 0:
            player.speed_y = -player.speed
        elif player.speed_y > 0:
            player.speed_y = 0
    elif event.key == pygame.K_DOWN:
        player.speed_x = 0
        # print('DOWN')
        if player.speed_y >= 0:
            player.speed_y = player.speed
        elif player.speed_y < 0:
            player.speed_y = 0


def handle_player_speed_without_stop(player: PlayerSettings, event):
    if event.key == pygame.K_LEFT:
        player.speed_y = 0
        player.speed_x = -player.speed
    elif event.key == pygame.K_RIGHT:
        player.speed_y = 0
        player.speed_x = player.speed
    elif event.key == pygame.K_UP:
        player.speed_x = 0
        player.speed_y = -player.speed
    elif event.key == pygame.K_DOWN:
        player.speed_x = 0
        player.speed_y = player.speed


def get_rect_coords(x, y, tile_size):
    pos_x = x * tile_size
    pos_y = y * tile_size
    return [[pos_y, pos_x], [pos_y + tile_size, pos_x + tile_size]]


def get_save_areas(level, seve_tiles: list):
    correct_rect = []
    for x, row in enumerate(level):
        for y, tile in enumerate(row):
            if tile in seve_tiles:
                correct_rect.append(get_rect_coords(x, y, GameSettings.tile_size))
    return correct_rect


def check_collizion(player: PlayerSettings, save_areas):
    bot = [player.bot()[0] + player.speed_x, player.bot()[1] + player.speed_y]
    top = [player.top()[0] + player.speed_x, player.top()[1] + player.speed_y]
    left = [player.left()[0] + player.speed_x, player.left()[1] + player.speed_y]
    right = [player.right()[0] + player.speed_x, player.right()[1] + player.speed_y]

    b, t, l, r = False, False, False, False
    for rect in save_areas:
        if rect[0][0] <= bot[0] <= rect[1][0] and rect[0][1] <= bot[1] <= rect[1][1]:
            b = True
        if rect[0][0] <= top[0] <= rect[1][0] and rect[0][1] <= top[1] <= rect[1][1]:
            t = True
        if rect[0][0] <= left[0] <= rect[1][0] and rect[0][1] <= left[1] <= rect[1][1]:
            l = True
        if rect[0][0] <= right[0] <= rect[1][0] and rect[0][1] <= right[1] <= rect[1][1]:
            r = True
    if b and t and l and r:
        return True
    else:
        return False


def new_pos(player: PlayerSettings, level):
    if check_collizion(player, get_save_areas(level, [0, 2, 3])):
        return [player.player_position[0] + player.speed_x, player.player_position[1] + player.speed_y]
    else:
        return [player.player_position[0], player.player_position[1]]


