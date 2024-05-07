import pygame
from settings import GameSettings, Color, GameColors
from settings import PlayerSettings, Building, PlayerBuildings
import time
from game_functions import place_building, produce_resources, process_building_click, handle_building_click, \
    select_building_for_build

from strategy.draw_functions import draw_resources, draw_buildings, draw_grid, draw_select_build

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen = pygame.display.set_mode((GameSettings.screen_width, GameSettings.screen_height))
pygame.display.set_caption("Economic Strategy Game")


def main():
    pygame.init()

    screen = pygame.display.set_mode((GameSettings.screen_width, GameSettings.screen_height))
    pygame.display.set_caption("Economic Strategy Game")

    clock = pygame.time.Clock()
    player_settings = PlayerSettings()
    player_buildings = PlayerBuildings()

    # Установка здания "sawmill" на первой клетке
    # place_building(player_buildings, "sawmill", (0, 0))

    running = True
    while running:
        screen.fill(GameColors.white)
        draw_grid(screen)
        draw_buildings(screen, player_buildings, player_settings)
        produce_resources(player_buildings, player_settings)
        draw_resources(screen, player_settings,player_buildings)
        if player_settings.status == 'choise_build':
            # print('1')
            draw_select_build(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    # print('2')
                x, y = pygame.mouse.get_pos()

                cell_x = x // GameSettings.tile_size
                cell_y = y // GameSettings.tile_size

                    # Обрабатываем клик по клетке с зданием
                if not player_settings.status:
                    handle_building_click(player_buildings, player_settings, (cell_x, cell_y))
                elif player_settings.status == 'choise_build':
                    # print(x, y)
                    build = select_building_for_build(x, y, player_settings)
                    place_building(player_buildings, build, (player_settings.x_mouse, player_settings.y_mouse), player_settings)


            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Чит: увеличиваем количество всех ресурсов до 100000
                player_settings.money = 100000
                player_settings.wood = 100000
                player_settings.food = 100000
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                # Чит: увеличиваем количество всех ресурсов до 100000
                player_settings.money = 0
                player_settings.wood = 0
                player_settings.food = 0
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            #     # Выбор здания при нажатии клавиши Enter
            #     building_type = select_building()
            #     x, y = pygame.mouse.get_pos()
            #     cell_x = x // GameSettings.tile_size
            #     cell_y = y // GameSettings.tile_size
            #     place_building(player_buildings, building_type, (cell_x, cell_y))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
