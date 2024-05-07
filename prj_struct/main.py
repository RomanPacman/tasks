import pygame
import time

from prj_struct.drawing import draw_level, draw_player, draw_exit, draw_fps
from prj_struct.movement import handle_player_speed_with_stop, new_pos, handle_player_speed_without_stop, \
    check_collizion, get_save_areas
from settings import GameSettings, PlayerSettings
from map import map_dict, get_player_start_pos, get_tile_pos

# Инициализация Pygame
pygame.init()

# Создание окна игры
screen = pygame.display.set_mode((GameSettings.screen_width, GameSettings.screen_height))
pygame.display.set_caption("My Game")


# Основной цикл игры
def main():
    # Загрузка уровня
    current_level = '1'
    level = map_dict[current_level]
    player_settings = PlayerSettings()
    player_settings.player_position = get_player_start_pos(level)
    total_time_start = time.time()
    total_time_spent = 0
    exit_position = get_tile_pos(level, 3)

    clock = pygame.time.Clock()
    running = True
    while running:
        start_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                handle_player_speed_without_stop(player_settings, event)

            elif event.type == pygame.QUIT:
                running = False

        player_settings.player_position = new_pos(player_settings, level)

        if check_collizion(player_settings, get_save_areas(level, [3])):
            # Проверяем, достиг ли игрок выхода на текущем уровне
            print('Finish level', current_level)
            # Переходим к следующему уровню
            current_level = str(int(current_level) + 1)
            if current_level in map_dict:
                level = map_dict[current_level]
                exit_position = get_tile_pos(level, 3)
                player_settings.player_position = get_player_start_pos(level)
                print('Next level', current_level)
            else:
                print('Game finished')
                total_time_spent += time.time() - start_time
                print(total_time_spent)
                running = False

        draw_level(level, screen)
        draw_exit(screen, exit_position)
        draw_player(screen, player_settings)

        draw_fps(screen, clock)
        pygame.display.flip()
        clock.tick(160)
    total_time_end = time.time()  # Время завершения игры
    total_time_spent += total_time_end - total_time_start  # Добавляем время игры к общему времени
    print("Total time:", int(total_time_spent), "seconds")

    pygame.quit()


if __name__ == "__main__":
    main()
