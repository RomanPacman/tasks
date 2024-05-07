import pygame
from settings import GameSettings, GameColors, building_types


def draw_grid(screen):
    for x in range(0, GameSettings.screen_width, GameSettings.tile_size):
        pygame.draw.line(screen, GameColors.black, (x, 0), (x, GameSettings.screen_height))
    for y in range(0, GameSettings.screen_height, GameSettings.tile_size):
        pygame.draw.line(screen, GameColors.black, (0, y), (GameSettings.screen_width, y))


def draw_resources(screen, player_settings, player_buildings):
    font = pygame.font.SysFont(None, 12)

    # Рисуем черный прямоугольник для отображения ресурсов
    pygame.draw.rect(screen, GameColors.black, (GameSettings.screen_width - 90, 0, 70, 45))

    # Отображаем количество денег
    money_production = sum(
        building.level for building in player_buildings.buildings if building.building_type == "market")
    money_text = font.render(f"Money: {player_settings.money} ({money_production})", True, GameColors.white)
    screen.blit(money_text, (GameSettings.screen_width - 80, 10))

    # Отображаем количество дерева
    wood_production = sum(
        building.level for building in player_buildings.buildings if building.building_type == "sawmill")
    # player_settings.wood += wood_production  # Учитываем произведенные дерево
    wood_text = font.render(f"Wood: {player_settings.wood} ({wood_production})", True, GameColors.white)
    screen.blit(wood_text, (GameSettings.screen_width - 80, 20))

    # Отображаем количество еды
    food_production = sum(
        building.level for building in player_buildings.buildings if building.building_type == "farm")
    # player_settings.food += food_production  # Учитываем произведенную еду
    food_text = font.render(f"Food: {player_settings.food} ({food_production})", True, GameColors.white)
    screen.blit(food_text, (GameSettings.screen_width - 80, 30))


def check_upgrade_ability(player_settings, building):
    if player_settings.wood >= building.upgrade_cost:
        return GameColors.green  # Зеленый цвет, если хватает ресурсов
    else:
        return GameColors.red  # Красный цвет, если не хватает ресурсов


def draw_buildings(screen, player_buildings, player_settings):
    for building in player_buildings.buildings:
        rect = pygame.Rect(building.position[0] * GameSettings.tile_size, building.position[1] * GameSettings.tile_size,
                           GameSettings.tile_size, GameSettings.tile_size)
        pygame.draw.rect(screen, GameColors.black, rect, 2)

        # Определяем цвет квадратика в зависимости от типа здания
        if building.building_type == "farm":
            color = GameColors.green
        elif building.building_type == "sawmill":
            color = GameColors.brown
        elif building.building_type == "market":
            color = GameColors.yellow
        else:
            color = GameColors.white

        pygame.draw.rect(screen, color, rect.inflate(-4, -4))

        # Отображаем уровень здания
        font = pygame.font.SysFont(None, 20)
        text = font.render(str(building.level), True, GameColors.black)
        text_rect = text.get_rect(center=(rect.centerx, rect.centery - 20))
        screen.blit(text, text_rect)

        # Отображаем название здания
        building_name = font.render(building.building_type.capitalize(), True, GameColors.black)
        name_rect = building_name.get_rect(center=(rect.centerx, rect.centery + 20))
        screen.blit(building_name, name_rect)

        # Отображаем цену улучшения здания
        upgrade_cost = building_types[building.building_type].upgrade_cost
        upgrade_cost_str = f"w:{upgrade_cost.get('wood', 0)}, f:{upgrade_cost.get('food', 0)}, g:{upgrade_cost.get('gold', 0)}"
        upgrade_cost_color = (GameColors.red if player_settings.wood < upgrade_cost.get('wood', 0) else GameColors.black,
                              GameColors.red if player_settings.food < upgrade_cost.get('food', 0) else GameColors.black,
                              GameColors.red if player_settings.money < upgrade_cost.get('gold', 0) else GameColors.black)
        upgrade_cost_text = font.render(upgrade_cost_str, True, upgrade_cost_color)
        cost_rect = upgrade_cost_text.get_rect(center=(rect.centerx, rect.centery + 40))
        screen.blit(upgrade_cost_text, cost_rect)


def draw_select_build(screen):
    width_button = 170
    height_button = 80
    margin = 20
    start_pos_x = 105
    start_pos_y = 100

    pygame.draw.rect(screen, GameColors.black, [start_pos_x, start_pos_y, 590, 120], 0)
    pygame.draw.rect(screen, GameColors.green,
                     [start_pos_x + margin, start_pos_y + margin, width_button, height_button], 0)  # farm
    pygame.draw.rect(screen, GameColors.brown,
                     [start_pos_x + margin * 2 + width_button, start_pos_y + margin, width_button, height_button],
                     0)  # sawmill
    pygame.draw.rect(screen, GameColors.yellow,
                     [start_pos_x + margin * 3 + width_button * 2, start_pos_y + margin, width_button, height_button],
                     0)  # market

    font = pygame.font.SysFont(None, 16)

    # Отображаем стоимость постройки для каждого здания
    farm_cost_text = font.render("w:2,f:5", True, GameColors.black)
    screen.blit(farm_cost_text, (start_pos_x + margin + 10, start_pos_y + margin + 10))

    sawmill_cost_text = font.render("w:8,f:5,g:8", True, GameColors.black)
    screen.blit(sawmill_cost_text, (start_pos_x + margin * 2 + width_button + 10, start_pos_y + margin + 10))

    market_cost_text = font.render("w:10,f:15,g:5", True, GameColors.black)
    screen.blit(market_cost_text, (start_pos_x + margin * 3 + width_button * 2 + 10, start_pos_y + margin + 10))
