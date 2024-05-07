from prj_struct.settings import GameSettings

lvl_clear = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

lvl_1 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

lvl_2 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

lvl_3 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

lvl_4 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 2, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 3, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

map_dict = {
    '1': lvl_1,
    '2': lvl_2,
    '3': lvl_3,
    '4': lvl_4,
}

tile_size = GameSettings.tile_size


def get_player_start_pos(lvl):
    for y, row in enumerate(lvl):
        for x, tile in enumerate(row):
            if tile == 2:
                return (x + 0.5) * tile_size, (y + 0.5) * tile_size


def get_tile_pos(lvl, tile):
    for y, row in enumerate(lvl):
        for x, ckeck_tile in enumerate(row):
            if ckeck_tile == tile:
                return x, y
