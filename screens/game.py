import pygame
import sys
from config import *

def select_objective_cards(screen, max_selection=2):
    """Modal de seleção de cartas de objetivo (com tema marrom do tabuleiro)"""
    font = pygame.font.Font(None, 26)
    small_font = pygame.font.Font(None, 24)

    objective_cards = [
        {"name": "Rio de Janeiro - São Gonçalo", "selected": False},
        {"name": "Maricá - Magé", "selected": False},
        {"name": "Nova Iguaçu - Rio Bonito", "selected": False},
        {"name": "Petrópolis - Cachoeiras de Macacu", "selected": False},
    ]

    table_color = (139, 69, 19)
    modal_color = (181, 101, 29)
    modal_border = (110, 58, 15)
    card_unselected = (205, 133, 63)
    card_selected = (237, 201, 175)
    text_color = (40, 20, 0)
    btn_color_enabled = (120, 70, 20)
    btn_color_disabled = (90, 60, 40)

    card_width = 300
    card_height = 70
    card_margin = 20
    cards_rects = []

    modal_width = card_width + 60
    modal_height = len(objective_cards) * (card_height + card_margin) + 150
    modal_x = SCREEN_WIDTH / 2 - modal_width / 2
    modal_y = SCREEN_HEIGHT / 2 - modal_height / 2

    for i, card in enumerate(objective_cards):
        rect = pygame.Rect(
            modal_x + 30,
            modal_y + 60 + i * (card_height + card_margin),
            card_width,
            card_height
        )
        cards_rects.append(rect)

    confirm_rect = pygame.Rect(
        modal_x + modal_width / 2 - 75,
        modal_y + modal_height - 70,
        150,
        45
    )

    selected_count = 0
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(cards_rects):
                    card = objective_cards[i]
                    if rect.collidepoint(mouse_pos):
                        if not card["selected"] and selected_count < max_selection:
                            card["selected"] = True
                            selected_count += 1
                        elif card["selected"]:
                            card["selected"] = False
                            selected_count -= 1

                if confirm_rect.collidepoint(mouse_pos) and selected_count > 0:
                    return [c["name"] for c in objective_cards if c["selected"]]

        screen.fill(table_color)

        modal_rect = pygame.Rect(modal_x, modal_y, modal_width, modal_height)
        pygame.draw.rect(screen, modal_color, modal_rect, border_radius=12)
        pygame.draw.rect(screen, modal_border, modal_rect, 4, border_radius=12)

        title = font.render("Selecione suas cartas de objetivo", True, text_color)
        screen.blit(title, (modal_x + modal_width / 2 - title.get_width() / 2, modal_y + 15))

        for i, rect in enumerate(cards_rects):
            card = objective_cards[i]
            color = card_selected if card["selected"] else card_unselected
            pygame.draw.rect(screen, color, rect, border_radius=10)
            pygame.draw.rect(screen, modal_border, rect, 2, border_radius=10)

            text = font.render(card["name"], True, text_color)
            screen.blit(text, (rect.x + 10, rect.y + rect.height / 2 - text.get_height() / 2))

        btn_color = btn_color_enabled if selected_count > 0 else btn_color_disabled
        pygame.draw.rect(screen, btn_color, confirm_rect, border_radius=8)
        confirm_text = small_font.render("Confirmar", True, WHITE)
        screen.blit(
            confirm_text,
            (
                confirm_rect.x + confirm_rect.width / 2 - confirm_text.get_width() / 2,
                confirm_rect.y + confirm_rect.height / 2 - confirm_text.get_height() / 2
            )
        )

        pygame.display.update()

def game_loop():
    """Loop principal do jogo"""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ticket to Ride - Jogo")
    clock = pygame.time.Clock()

    table_color = (139, 69, 19)

    try:
        board_image = pygame.image.load("assets/board.png").convert_alpha()
        board_width = int(SCREEN_WIDTH * 0.85)
        board_height = int(SCREEN_HEIGHT * 0.85)
        board_image = pygame.transform.smoothscale(board_image, (board_width, board_height))
    except:
        board_image = pygame.Surface((int(SCREEN_WIDTH * 0.85), int(SCREEN_HEIGHT * 0.85)))
        board_image.fill((200, 220, 255))

    board_x = (SCREEN_WIDTH - board_image.get_width()) // 2
    board_y = (SCREEN_HEIGHT - board_image.get_height()) // 2

    selected_cards = select_objective_cards(screen)
    print("Cartas selecionadas:", selected_cards)

    participants = [
        {"name": "Breno", "color": (255, 0, 0), "pos": (30, 80)},
        {"name": "João", "color": (0, 255, 0), "pos": (SCREEN_WIDTH - 30, 80)},
        {"name": "Luisa", "color": (0, 0, 255), "pos": (30, SCREEN_HEIGHT - 100)},
        {"name": "Leo", "color": (255, 255, 0), "pos": (SCREEN_WIDTH - 30, SCREEN_HEIGHT - 100)},
    ]

    font = pygame.font.Font(None, 30)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(table_color)

        shadow_rect = pygame.Rect(board_x + 5, board_y + 5, board_image.get_width(), board_image.get_height())
        pygame.draw.rect(screen, (60, 30, 10), shadow_rect, border_radius=10)

        screen.blit(board_image, (board_x, board_y))

        for p in participants:
            pygame.draw.circle(screen, p["color"], p["pos"], 20)
            name_text = font.render(p["name"], True, WHITE)
            screen.blit(name_text, (p["pos"][0] - name_text.get_width()/2, p["pos"][1] + 40))

        pygame.display.update()
        clock.tick(60)
