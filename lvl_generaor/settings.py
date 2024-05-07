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
    def __init__(self, x=0, y=0, color=(0, 255, 0), radius=GameSettings.tile_size // 3, speed=2):
        self.color = color  # Цвет игрока
        self.radius = radius  # Радиус игрока
        self.speed = speed  # Скорость игрока
        self.player_position = [x, y]
        self.run = False
        self.speed_x = 0
        self.speed_y = 0

    def get_x(self):
        return self.player_position[0]  # Возвращает координату X

    def get_y(self):
        return self.player_position[1]  # Возвращает координату Y

    def top(self):
        return [self.player_position[0], self.player_position[1] - self.radius]  # Возвращает координату top

    def right(self):
        return [self.player_position[0] + self.radius, self.player_position[1]]  # Возвращает координату right

    def bot(self):
        return [self.player_position[0], self.player_position[1] + self.radius]  # Возвращает координату bot

    def left(self):
        return [self.player_position[0] - self.radius, self.player_position[1]]  # Возвращает координату left
