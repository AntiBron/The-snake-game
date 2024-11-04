import pygame
import random
import sys

# Инициализация pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Функция для отображения текста на экране
def display_text(text, color, x, y, size=30):
    font = pygame.font.Font(None, size)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

# Основная функция игры
def game_loop():
    # Параметры змейки
    snake_pos = [(WIDTH // 2, HEIGHT // 2)]
    snake_dir = (0, -BLOCK_SIZE)
    snake_length = 1

    # Позиция пищи
    food_pos = (random.randrange(0, WIDTH, BLOCK_SIZE),
                random.randrange(0, HEIGHT, BLOCK_SIZE))

    clock = pygame.time.Clock()
    score = 0

    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dir != (0, BLOCK_SIZE):
                    snake_dir = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -BLOCK_SIZE):
                    snake_dir = (0, BLOCK_SIZE)
                elif event.key == pygame.K_LEFT and snake_dir != (BLOCK_SIZE, 0):
                    snake_dir = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-BLOCK_SIZE, 0):
                    snake_dir = (BLOCK_SIZE, 0)

        # Обновление позиции змейки
        new_head = (snake_pos[0][0] + snake_dir[0],
                    snake_pos[0][1] + snake_dir[1])
        snake_pos = [new_head] + snake_pos[:snake_length]

        # Проверка столкновений
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake_pos[1:]):
            break

        # Проверка поедания пищи
        if new_head == food_pos:
            score += 1
            snake_length += 1
            food_pos = (random.randrange(0, WIDTH, BLOCK_SIZE),
                        random.randrange(0, HEIGHT, BLOCK_SIZE))

        # Отображение графики
        screen.fill(BLACK)
        for segment in snake_pos:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, (*food_pos, BLOCK_SIZE, BLOCK_SIZE))
        display_text(f'Счёт: {score}', WHITE, 10, 10, 24)
        pygame.display.flip()
        clock.tick(10)

    # Конец игры
    screen.fill(BLACK)
    display_text("Игра окончена!", RED, WIDTH // 2 - 60, HEIGHT // 2 - 20, 50)
    display_text(f'Счёт: {score}', WHITE, WIDTH // 2 - 40, HEIGHT // 2 + 30, 30)
    pygame.display.flip()
    pygame.time.delay(2000)

# Запуск игры
if __name__ == "__main__":
    game_loop()
    pygame.quit()
