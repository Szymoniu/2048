import pygame
def wynik(screen, score, width, height):
    font = pygame.font.Font(None, 36)
    text = font.render("Twój wynik:", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height - 50))
    screen.blit(text, text_rect)

    
    score_text = font.render(str(score), True, (0, 0, 0))
    score_rect = score_text.get_rect(center=(width // 2, height - 20))
    screen.blit(score_text, score_rect)
    