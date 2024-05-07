import time

from settings import Building, GameColors, building_types, PlayerSettings


# def place_building(player_buildings, building_type, position):
#     # Проверяем, есть ли уже здание на этой клетке
#     for building in player_buildings.buildings:
#         if building.position == position:
#             return
#     new_building = Building(building_type, position=position)
#     player_buildings.add_building(new_building)

def place_building(player_buildings, building_type, position, player_settings):
    # Проверяем, есть ли уже здание на этой клетке
    for building in player_buildings.buildings:
        if building.position == position:
            return False

    # Получаем стоимость строительства здания
    build_cost = building_types[building_type].upgrade_cost

    # Проверяем, хватает ли ресурсов у игрока для строительства
    if player_settings.money >= build_cost['gold'] and \
            player_settings.wood >= build_cost['wood'] and \
            player_settings.food >= build_cost['food']:
        # Уменьшаем количество ресурсов у игрока
        player_settings.money -= build_cost['gold']
        player_settings.wood -= build_cost['wood']
        player_settings.food -= build_cost['food']

        # Строим здание
        new_building = Building(building_type, position)
        player_buildings.add_building(new_building)
        return True
    else:
        return False


def produce_resources(player_buildings, player_settings):
    for building in player_buildings.buildings:
        produced_resources = building.produce_resources()  # Получаем количество произведенных ресурсов
        if building.building_type == "sawmill":
            player_settings.wood += produced_resources
        elif building.building_type == "farm":
            player_settings.food += produced_resources
        elif building.building_type == "market":
            player_settings.money += produced_resources


def check_building_existence(player_buildings, position):
    for building in player_buildings:
        if building.position == position:
            return True
    return False


def handle_building_click(player_buildings, player_settings: PlayerSettings, position):
    if check_building_existence(player_buildings.buildings, position):
        process_building_click(player_buildings, player_settings, position)
    else:
        player_settings.x_mouse, player_settings.y_mouse = position
        player_settings.status = 'choise_build'


def process_building_click(player_buildings, player_settings, position):
    # Проверяем, есть ли здание на этой клетке
    if check_building_existence(player_buildings.buildings, position):
        # Если есть, то улучшаем его
        for building in player_buildings.buildings:
            if building.position == position:
                # Проверяем, хватает ли дерева для улучшения
                if player_settings.wood >= building.upgrade_cost:
                    player_settings.wood -= building.upgrade_cost  # Уменьшаем количество дерева у игрока
                    building.upgrade()  # Увеличиваем уровень здания
                    return True  # Успешно улучшили здание
                else:
                    return False  # Недостаточно дерева для улучшения


def select_building_for_build(x, y, player_settings: PlayerSettings):
    # print(player_settings.status)
    if 120 <= y <= 200:
        if 125 <= x <= 295:
            player_settings.status = None
            return 'farm'
        elif 315 <= x <= 485:
            player_settings.status = None
            return 'sawmill'
        elif 505 <= x <= 675:
            player_settings.status = None
            return 'market'
