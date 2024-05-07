import time

import pygame


class GameSettings:
    screen_height = 600
    screen_width = 800
    tile_size = 100


class Color:
    def __init__(self, id_color, name, rgb):
        self.id_color = id_color
        self.name = name
        self.rgb = rgb


class ColorDescriptor:
    def __init__(self, color):
        self.color = color

    def __get__(self, instance, owner):
        return self.color.rgb


class GameColors:
    red = ColorDescriptor(Color(1, "Red", (255, 0, 0)))
    green = ColorDescriptor(Color(2, "Green", (0, 255, 0)))
    blue = ColorDescriptor(Color(3, "Blue", (0, 0, 255)))
    yellow = ColorDescriptor(Color(4, "Yellow", (255, 255, 0)))
    orange = ColorDescriptor(Color(5, "Orange", (255, 165, 0)))
    purple = ColorDescriptor(Color(6, "Purple", (128, 0, 128)))
    cyan = ColorDescriptor(Color(7, "Cyan", (0, 255, 255)))
    magenta = ColorDescriptor(Color(8, "Magenta", (255, 0, 255)))
    pink = ColorDescriptor(Color(9, "Pink", (255, 192, 203)))
    brown = ColorDescriptor(Color(10, "Brown", (165, 42, 42)))
    lime = ColorDescriptor(Color(11, "Lime", (0, 255, 0)))
    teal = ColorDescriptor(Color(12, "Teal", (0, 128, 128)))
    lavender = ColorDescriptor(Color(13, "Lavender", (230, 230, 250)))
    maroon = ColorDescriptor(Color(14, "Maroon", (128, 0, 0)))
    navy = ColorDescriptor(Color(15, "Navy", (0, 0, 128)))
    olive = ColorDescriptor(Color(16, "Olive", (128, 128, 0)))
    sky_blue = ColorDescriptor(Color(17, "Sky Blue", (135, 206, 235)))
    indigo = ColorDescriptor(Color(18, "Indigo", (75, 0, 130)))
    peach = ColorDescriptor(Color(19, "Peach", (255, 218, 185)))
    gold = ColorDescriptor(Color(20, "Gold", (255, 215, 0)))
    white = ColorDescriptor(Color(20, "White", (255, 255, 255)))
    black = ColorDescriptor(Color(15, "Black", (0, 0, 0)))


class PlayerSettings:
    def __init__(self):
        self.money = 30
        self.exp = 0
        self.food = 30
        self.wood = 30
        self.status = None
        self.x_mouse = 0
        self.y_mouse = 0

    def deduct_building_cost(self, money_cost, wood_cost, food_cost):
        self.money -= money_cost
        self.wood -= wood_cost
        self.food -= food_cost if hasattr(self, 'food') else 0


class Building:
    def __init__(self, building_type, position=(0, 0), level=1, base_production=1):
        self.building_type = building_type  # Тип здания (например, "sawmill")
        self.position = position  # Позиция здания на поле (координаты x, y)
        self.level = level
        self.last_produced = 0  # Время последнего произведенного ресурса
        self.base_production = base_production
        self.upgrade_cost = self.calculate_upgrade_cost()

    def produce_resources(self):
        # Логика производства ресурсов для каждого типа здания
        if self.building_type == "sawmill" and time.time() - self.last_produced >= 5:
            self.last_produced = time.time()
            return self.base_production * self.level
        elif self.building_type == "farm" and time.time() - self.last_produced >= 5:
            self.last_produced = time.time()
            return self.base_production * self.level
        elif self.building_type == "market" and time.time() - self.last_produced >= 5:
            self.last_produced = time.time()
            return self.base_production * self.level
        else:
            return 0  # В случае, если здание не производит ресурсы в данный момент

    def draw(self, screen):
        x = self.position[0] * GameSettings.tile_size
        y = self.position[1] * GameSettings.tile_size
        pygame.draw.rect(screen, GameColors.red, (x, y, GameSettings.tile_size, GameSettings.tile_size))

        font = pygame.font.SysFont(None, 20)
        text = font.render(str(self.level), True, GameColors.black)
        text_rect = text.get_rect(center=(x + GameSettings.tile_size // 2, y + GameSettings.tile_size // 2))
        screen.blit(text, text_rect)

    def calculate_upgrade_cost(self):
        if self.building_type == "farm":
            money_cost = 2 * self.level
            wood_cost = 5 * 2 * self.level
            return money_cost, wood_cost
        elif self.building_type == "sawmill":
            money_cost = 8 * 2 * self.level
            wood_cost = 5 * self.level
            food_cost = 2 ** 2 * self.level
            return money_cost, wood_cost, food_cost
        elif self.building_type == "market":
            money_cost = 5 * 2 ** 2 * self.level
            wood_cost = 10 * self.level
            food_cost = 5 * self.level
            return money_cost, wood_cost, food_cost
        else:
            return 0

    def upgrade(self):
        self.level += 1
        self.upgrade_cost = self.calculate_upgrade_cost()


class PlayerBuildings:
    def __init__(self):
        self.buildings = []  # Список зданий игрока

    def add_building(self, building):
        self.buildings.append(building)

    def get_building(self, name):
        for building in self.buildings:
            if building.name == name:
                return building
        return None


class BuildingType:
    def __init__(self, name, production_resource, base_production, upgrade_cost):
        self.name = name
        self.production_resource = production_resource
        self.base_production = base_production
        self.upgrade_cost = upgrade_cost

building_types = {
    "farm": BuildingType("Farm", "food", 1, {"wood": 5, "food": 2, "gold": 2}),
    "sawmill": BuildingType("Sawmill", "wood", 1, {"wood": 5, "food": 8}),
    "market": BuildingType("Market", "money", 1, {"wood": 15, "food": 5, "gold": 10})
}
