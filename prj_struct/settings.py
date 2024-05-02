class GameSettings:
    screen_height = 600
    screen_width = 800
    tile_size = 100

class Color:
    def __init__(self, id_color, name, rgb):
        self.id_color = id_color
        self.name = name
        self.rgb = rgb


class GameColors:
    def __init__(self):
        self.colors = {}

    def add_color(self, color_id, name, rgb):
        self.colors[color_id] = Color(color_id, name, rgb)

    def get_color(self, color_id):
        return self.colors.get(color_id)

game_colors = GameColors()
game_colors.add_color(1, "Red", (255, 0, 0))
game_colors.add_color(2, "Green", (0, 255, 0))
game_colors.add_color(3, "Blue", (0, 0, 255))