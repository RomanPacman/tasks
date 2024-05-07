import pygame

from tile_play.settings import GameColors, PlayerSettings


def change_color(item, trend):
    if item == 0:
        # print('trend +')
        trend = True
    elif item == 255:
        # print('trend -')
        trend = False

    if trend:
        print(item)
        item += 1
    else:
        item -= 1


# textures
lvl_textures = pygame.image.load(r"C:\Users\User\Desktop\assets\Platform.png")
player_textures = pygame.image.load(r"C:\Users\User\Desktop\assets\player_1.png")
walk_textures_right = player_textures
walk_textures_left = pygame.transform.flip(walk_textures_right, True, False)
player_textures.set_colorkey([155, 155, 155])
walk_textures_left.set_colorkey([155, 155, 155])


def draw_player(screen, player: PlayerSettings):
    player_color = GameColors.green
    player_box = pygame.Rect(player.get_rect())
    pygame.draw.rect(screen, player_color, player_box, 5, 20, 20, 20, 20)


def draw_texture_player_idle(screen, player: PlayerSettings, tact):
    # player_box = pygame.Rect(player.get_rect())
    player_box = pygame.Rect(266, 70, player.width - 5, player.height)
    hitbox_surface = player_textures.subsurface(player_box)
    screen.blit(hitbox_surface, [player.get_x(), player.get_y() - 90])


def draw_texture_player_walk(screen, player: PlayerSettings, tact):
    walk_textures = walk_textures_right
    step = tact % 7  # // 1

    if player.course == 'left':
        walk_textures = walk_textures_left
    # player_box = pygame.Rect(266, 280, player.width - 5, player.height)
    x_pos_texture = 266 + step * 193

    # print(f'{player.course}  {x_pos_texture}')
    player_box = pygame.Rect(x_pos_texture, 280, player.width - 5, player.height)

    hitbox_surface = walk_textures.subsurface(player_box)
    screen.blit(hitbox_surface, [player.get_x(), player.get_y() - 90])


def draw(screen, tile_coords: list):
    # screen.blit(player_image, (100, 100))  # Изображение игрока
    floor_rect = pygame.Rect(30, 0, 100, 50)
    hitbox_surface = lvl_textures.subsurface(floor_rect)
    screen.blit(hitbox_surface, tile_coords)


def draw_all(screen, tile_coords: list, asset_coords: list):
    # rect_coords = [(x * 64, x * 64) for x in asset_coords]
    # rect_coords.append(64)
    # rect_coords.append(64)
    rect_coords = [asset_coords[0] * 64, asset_coords[1] * 64, 64, 64]
    floor_rect = pygame.Rect(rect_coords)
    hitbox_surface = lvl_textures.subsurface(floor_rect)
    screen.blit(hitbox_surface, tile_coords)


def draw_attack_1(screen, player: PlayerSettings, tact):
    # print('q')
    x_pos_texture = 220 + tact * 200

    rect_dict = {
        0: [256, 920, 170, 220], #[256, 920, 170, 220],
        1: [442, 920, 170, 220],
        2: [620, 920, 210, 220],
        3: [820, 920, 250, 220],
        4: [1020, 920, 130, 220],
        5: [1230, 920, 150, 220],
        6: [1400, 920, 160, 220]
    }

    # player_box = pygame.Rect(x_pos_texture, 948, player.width + 80, player.height)
    # player_box = pygame.Rect(x_pos_texture, 900, 200, 183)
    player_box = rect_dict[tact]
    hitbox_surface = player_textures.subsurface(player_box)
    screen.blit(hitbox_surface, [player.get_x(), player.get_y() - 110])
