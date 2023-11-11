import pygame
import sys
import random
from utils import losuj_liczbe
from sterowanie import przesun_w_prawo, przesun_w_lewo, przesun_w_górę, przesun_w_dół, dodaj_nowe_liczby

pygame.init()

width, height = 600, 600
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("2048")

rows, cols = 4, 4
okno = width // cols
border = (0, 0, 0)

background_color = ("lightblue")

zawartosc_siatki = [[0 for _ in range(cols)] for _ in range(rows)]

for _ in range(2):
        empty_cells = [(i, j) for i in range(rows) for j in range(cols) if zawartosc_siatki[i][j] == 0]
if empty_cells:
        row, col = random.choice(empty_cells)
        zawartosc_siatki[row][col] = 2



def siatka():
    for row in range(rows):
        for col in range(cols):
            if zawartosc_siatki[row][col] == 2:
                color = ("blue")  
            else:
                color = ("lightblue")   

            pygame.draw.rect(screen, color, (col * okno, row * okno, okno, okno))
            pygame.draw.rect(screen, (0, 0, 0), (col * okno, row * okno, okno, okno), 2)

def obsluga_klawiszy():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                przesun_w_lewo(rows, zawartosc_siatki, cols)
            elif event.key == pygame.K_RIGHT:
                przesun_w_prawo(rows, zawartosc_siatki, cols)
            elif event. key == pygame.K_UP:
                przesun_w_górę(rows, zawartosc_siatki, cols)
            elif event.key == pygame.K_DOWN:
                przesun_w_dół(rows, zawartosc_siatki, cols)

# Reszta kodu bez zmian

            

def main():
    while True:
        obsluga_klawiszy()

        screen.fill(background_color)
        siatka()
        losuj_liczbe(rows, cols, zawartosc_siatki, screen, okno)

        pygame.display.flip()

if __name__ == "__main__":
    main()
