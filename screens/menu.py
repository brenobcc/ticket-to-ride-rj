import pygame, sys
from config import *
from screens.game import game_loop

def main_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ticket to Ride - Rio de Janeiro")

    font = pygame.font.Font(None, 50)
    button_rect = pygame.Rect((SCREEN_WIDTH - 200)/2, (SCREEN_HEIGHT - 70)*0.8, 200, 70)
    text = font.render('Jogar', True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)

    try:
        background_image = pygame.image.load("assets/background.png").convert()
        background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except pygame.error as e:
        print(f"Erro ao carregar a imagem de fundo: {e}")
        
        background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        background_image.fill(BLACK)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(background_image, (0, 0))

        color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(screen, color, button_rect, border_radius=10)

        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(mouse_pos):
                game_loop()

        pygame.display.update() 