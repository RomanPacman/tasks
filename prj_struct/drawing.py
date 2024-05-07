import pygame
from settings import GameSettings, GameColors, PlayerSettings


def draw_level(level, screen):
    tile_size = GameSettings.tile_size
    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            color = GameColors.white  # По умолчанию белый цвет для пустых клеток
            if tile == 1:
                color = GameColors.blue

            pygame.draw.rect(screen, color, (x * tile_size, y * tile_size, tile_size, tile_size))


def draw_player(screen, player: PlayerSettings):
    x, y = player.player_position[0], player.player_position[1]
    player_color = GameColors.green
    pygame.draw.circle(screen, player_color, (x, y), player.radius)


def draw_exit(screen, exit_position):
    tile_size = GameSettings.tile_size
    x, y = exit_position
    x_scale, y_scale = x * tile_size, y * tile_size
    tile_2, tile_4 = tile_size / 2, tile_size / 4
    exit_color = GameColors.orange
    rect_width = pygame.Rect(x_scale, y_scale + tile_4, tile_size, tile_2)
    rect_height = pygame.Rect(x_scale + tile_4, y_scale, tile_2, tile_size)
    pygame.draw.rect(screen, exit_color, rect_width)
    pygame.draw.rect(screen, exit_color, rect_height)

    pygame.draw.circle(screen, exit_color, [x_scale + tile_4, y_scale + tile_4], tile_4)
    pygame.draw.circle(screen, exit_color, [x_scale + tile_4 + tile_2, y_scale + tile_4], tile_4)
    pygame.draw.circle(screen, exit_color, [x_scale + tile_4, y_scale + tile_4 + tile_2], tile_4)
    pygame.draw.circle(screen, exit_color, [x_scale + tile_4 + tile_2, y_scale + tile_4 + tile_2], tile_4)


def draw_fps(screen, clock):
    fps = int(clock.get_fps())
    font = pygame.font.SysFont(None, 24)
    fps_text = font.render(f"FPS: {fps}", True, GameColors.white)
    screen.blit(fps_text, (GameSettings.screen_width - 80, 20))
