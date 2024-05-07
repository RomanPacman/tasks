# Создаем поле из клеточек
import random

import pygame

width = 1500
height = 800
CELL_SIZE = 10

ROWS = int(height / CELL_SIZE)
COLS = int(width / CELL_SIZE)

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GREEN = [255, 255, 255]

grid = [[False for _ in range(COLS)] for _ in range(ROWS)]  # Инициализируем все клеточки как незакрашенные

def fill_random_cells():
    global grid
    for row in range(ROWS):
        for col in range(COLS):
            grid[row][col] = random.choice([True, False])

def update_grid():
    global grid
    new_grid = [[False for _ in range(COLS)] for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            neighbors = count_neighbors(row, col)
            # Правила "Жизнь"
            if grid[row][col]:
                if neighbors < 2 or neighbors > 3:
                    new_grid[row][col] = False
                else:
                    new_grid[row][col] = True
            else:
                if neighbors == 3:
                    new_grid[row][col] = True
    grid = new_grid


def count_neighbors(row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                if 0 <= row + i < ROWS and 0 <= col + j < COLS:
                    if grid[row + i][col + j]:
                        count += 1
    return count


# Функция для определения индексов клеточки по координатам мыши
def get_clicked_cell(pos):
    x, y = pos
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    return row, col


pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

# Основной цикл pygame
running = True
game_started = False
while running:
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # ЛКМ
                clicked_row, clicked_col = get_clicked_cell(event.pos)
                grid[clicked_row][clicked_col] = not grid[clicked_row][clicked_col]  # Инвертируем состояние клеточки
            elif event.button == 3:  # ПКМ
                fill_random_cells()
        elif event.type == pygame.KEYDOWN:
            game_started = not game_started if event.key == pygame.K_SPACE else game_started

    if game_started:
        update_grid()

    # Отрисовываем поле
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if grid[row][col] else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            # pygame.draw.rect(screen, GREEN, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    pygame.display.flip()
    clock.tick(160)
