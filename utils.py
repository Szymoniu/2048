import pygame
def losuj_liczbe(rows, cols, mesh, screen, okno, flaga):
    
    font = pygame.font.Font(None, 36)

    for row in range(rows):
        for col in range(cols):
            # Rysowanie liczby tylko jeśli nie jest równa 0
            if mesh[row][col] != 0:
                text = font.render(str(mesh[row][col]), True, (255, 255, 255))  # Biały kolor tekstu
                text_rect = text.get_rect(center=(col * okno + okno // 2, row * okno + okno // 2))
                screen.blit(text, text_rect)