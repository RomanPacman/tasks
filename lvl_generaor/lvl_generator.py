import random
import msvcrt

width = 8
height = 6

my_dict = {f'{i}': [' '] * (height - 1) + [111] for i in range(width)}


def draw_lvl(lvl_dict):
    for row in range(height):
        lvl_row = []
        for value in lvl_dict.values():
            lvl_row.append(value[row])
        print(lvl_row)


# print(my_dict[str(len(my_dict)-1)])


def generate_col(previous_column):
    new_column = []
    for i in range(len(previous_column)):
        if previous_column[i] == 0 and previous_column[i - 1:i + 2].count(0) < 3 and previous_column[i - 1:i + 2].count(
                1) < 2:
            new_column.append(0)
        else:
            new_column.append(1)
    return new_column


def gener_col(height_lvl):
    new_column = []
    for step in range(height_lvl):
        if random.randint(0, 1) == 1:
            new_column.append(' ')
        else:
            new_column.append(111)
    if 111 not in new_column:
        gener_col(height_lvl)
    else:
        return new_column



for step in range(10):
    last_col = (len(my_dict) - 1)
    # my_dict[str(int(last_col) + 1)] = generate_col(my_dict[last_col])
    my_dict[str(last_col + 1)] = gener_col(height)
    draw_lvl(my_dict)
    print('')

# draw_lvl(my_dict)
