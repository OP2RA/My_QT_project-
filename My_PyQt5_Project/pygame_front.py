
import PIL
import pygame, random

pygame.init()


bg = pygame.image.load('marsi.png')
WINDOW_WIDTH = bg.get_size()[0]
WINDOW_HEIGHT = bg.get_size()[1]
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Puzzle Game')

FPS = 10
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CRIMSON = (220, 20, 60)
ORANGE = (255, 127, 0)

bg_rect = bg.get_rect()
bg_rect.topleft = (0, 0)

font_title = pygame.font.Font('20780.ttf', 64)
font_content = pygame.font.Font('20686.ttf', 40)

title_text = font_title.render('Puzzle Game', True, CRIMSON)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 80)

choose_text = font_content.render('Choose your difficulty', True, CRIMSON)
choose_rect = choose_text.get_rect()
choose_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20)

easy_text = font_content.render("Press 'E' - Easy (3x3)", True, ORANGE)
easy_rect = easy_text.get_rect()
easy_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 40)

medium_text = font_content.render("Press 'M' - Medium (4x4)", True, ORANGE)
medium_rect = medium_text.get_rect()
medium_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 90)

hard_text = font_content.render("Press 'H' - Hard (5x5)", True, ORANGE)
hard_rect = hard_text.get_rect()
hard_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 140)

# end screen
play_again_text = font_title.render('Play Again?', True, WHITE)
play_again_rect = play_again_text.get_rect()
play_again_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font_content.render('Yes(Y)', True, WHITE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2 - 125, WINDOW_HEIGHT // 2 + 100)

end_text = font_content.render('No(N)', True, WHITE)
end_rect = end_text.get_rect()
end_rect.center = (WINDOW_WIDTH // 2 + 125, WINDOW_HEIGHT // 2 + 100)

selected_img = None
is_game_over = False
show_start_screen = True

cell_width = None
cell_height = None

cells = []

def start_game(mode):
    global cells, cell_width, cell_height, show_start_screen
    rows = mode
    cols = mode

    num_cells = rows * cols

    cell_width = WINDOW_WIDTH // rows
    cell_height = WINDOW_HEIGHT // cols

    cell = []
    rand_indexes = list(range(0, num_cells))

    for i in range(num_cells):
        x = (i % rows) * cell_width
        y = (i // cols) * cell_height
        rect = pygame.Rect(x, y, cell_width, cell_height)
        rand_pos = random.choice(rand_indexes)
        rand_indexes.remove(rand_pos)
        cells.append({'rect': rect, 'border': WHITE, 'order': i, 'pos': rand_pos})

    show_start_screen = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if show_start_screen:
        screen.fill(BLACK)
        screen.blit(title_text, title_rect)
        screen.blit(choose_text, choose_rect)
        screen.blit(easy_text, easy_rect)
        screen.blit(medium_text, medium_rect)
        screen.blit(hard_text, hard_rect)
    else:

        screen.fill(WHITE)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
