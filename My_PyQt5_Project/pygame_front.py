import pygame
import random
import os

if __name__ != '__main__':
    directory = 'C:/PyCharm/Notes/Puzzle/data'
    pictures = os.listdir(directory)
    random_pic = os.path.join('data', random.choice(pictures))
    pygame.init()
    bg = pygame.image.load(random_pic)
    WINDOW_WIDTH = bg.get_size()[0]
    WINDOW_HEIGHT = bg.get_size()[1]
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Puzzle')

    # FPS = 10
    # clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    DARKRED = (220, 20, 60)
    ORANGE = (255, 127, 0)

    bg_rect = bg.get_rect()
    bg_rect.topleft = (0, 0)

    font_title = pygame.font.Font('20780.ttf', 64)
    font_content = pygame.font.Font('20686.ttf', 40)

    title_text = font_title.render('Puzzle Game', True, DARKRED)
    title_rect = title_text.get_rect()
    title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 80)

    choose_text = font_content.render('Choose your difficulty', True, DARKRED)
    choose_rect = choose_text.get_rect()
    choose_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20)

    easy_text = font_content.render("Press 'E' - Easy (4x4)", True, ORANGE)
    easy_rect = easy_text.get_rect()
    easy_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 40)

    medium_text = font_content.render("Press 'M' - Medium (5x5)", True, ORANGE)
    medium_rect = medium_text.get_rect()
    medium_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 90)

    hard_text = font_content.render("Press 'H' - Hard (6x6)", True, ORANGE)
    hard_rect = hard_text.get_rect()
    hard_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 140)

    # end screen
    play_again1 = font_title.render('Play Again?', True, WHITE)
    play_again2 = play_again1.get_rect()
    play_again2.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    continue_text = font_content.render('Yes(Y)', True, WHITE)
    continue_rect = continue_text.get_rect()
    continue_rect.center = (WINDOW_WIDTH // 2 - 125, WINDOW_HEIGHT // 2 + 100)

    end_text = font_content.render('No(N)', True, WHITE)
    end_rect = end_text.get_rect()
    end_rect.center = (WINDOW_WIDTH // 2 + 125, WINDOW_HEIGHT // 2 + 100)

    selected_img = None
    game_over = False
    show_start_screen = True

    cell_width = None
    cell_height = None

    cells = []


    def start_game(mode):
        global cells, cell_width, cell_height, show_start_screen
        rows = mode
        cols = mode

        num_cells = rows * cols

        cell_width = WINDOW_WIDTH // rows  # ??????-???? ???????????????? ?? ??????????
        cell_height = WINDOW_HEIGHT // cols

        cell = []
        rand_indexes = list(range(0, num_cells))

        for i in range(num_cells):  # ?????????????????? ?????????? ?? ?????????????????????? ??????????????????????????????, ?? ?????? ?????????????? ??????????
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if game_over:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_y]:
                        game_over = False
                        show_start_screen = True
                    if keys[pygame.K_n]:
                        pygame.quit()

                if show_start_screen:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_e]:
                        start_game(4)
                    elif keys[pygame.K_m]:
                        start_game(5)
                    elif keys[pygame.K_h]:
                        start_game(6)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                mouse_pos = pygame.mouse.get_pos()

                for cell in cells:
                    rect = cell['rect']
                    order = cell['order']

                    if rect.collidepoint(mouse_pos):  # ???????????????? ?????????????? ???????????? ?????????????????? ??????????
                        if not selected_img:
                            selected_img = cell
                            cell['border'] = RED
                        else:
                            current_img = cell
                            # ???????????????????? ??????????????
                            if current_img['order'] != selected_img['order']:
                                temp = selected_img['pos']
                                cells[selected_img['order']]['pos'] = cells[current_img['order']]['pos']
                                cells[current_img['order']]['pos'] = temp
                                cells[selected_img['order']]['border'] = WHITE
                                selected_img = None

                                # ???????????? ???? ??????????
                                game_over = True
                                for cell in cells:
                                    if cell['order'] != cell['pos']:
                                        game_over = False

        if show_start_screen:
            screen.fill(BLACK)
            screen.blit(title_text, title_rect)
            screen.blit(choose_text, choose_rect)
            screen.blit(easy_text, easy_rect)
            screen.blit(medium_text, medium_rect)
            screen.blit(hard_text, hard_rect)
        else:

            screen.fill(WHITE)

            if not game_over:
                for i, val in enumerate(cells):
                    pos = cells[i]['pos']
                    img_area = pygame.Rect(cells[pos]['rect'].x, cells[pos]['rect'].y, cell_width, cell_height)
                    screen.blit(bg, cells[i]['rect'], img_area)
                    pygame.draw.rect(screen, cells[i]['border'], cells[i]['rect'], 1)
            else:
                screen.blit(bg, bg_rect)
                screen.blit(play_again1, play_again2)
                screen.blit(continue_text, continue_rect)
                screen.blit(end_text, end_rect)

        pygame.display.update()
        # clock.tick(FPS)

    pygame.quit()
