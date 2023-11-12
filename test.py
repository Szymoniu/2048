import pygame
import sys
import random
import pygame.time
from utils import losuj_liczbe
from sterowanie import przesun_w_prawo, przesun_w_lewo, przesun_w_górę, przesun_w_dół, dodaj_nowe_liczby, resetuj_flagi
from siatka import siatka
from wynik import wynik
pygame.init()


font = pygame.font.Font(None, 36)
width, height = 600, 700
screen_size = (width, height)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("2048")

rows, cols = 4, 4
okno = width // cols
border = (0, 0, 0)
move = False
score = 0
addscore = False

background_color = ("white")

zawartosc_siatki = [[0 for _ in range(cols)] for _ in range(rows)]
flaga = [[False for _ in range(cols)] for _ in range(rows)]


for _ in range(2):
    empty_cells = [(i, j) for i in range(rows) for j in range(cols) if zawartosc_siatki[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        zawartosc_siatki[row][col] = 2
        
def obsluga_klawiszy():
    global score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                przesun_w_lewo(rows, zawartosc_siatki, cols, flaga)
                dodaj_nowe_liczby(rows, zawartosc_siatki, cols)
                resetuj_flagi(flaga, rows, cols)
                
            elif event.key == pygame.K_RIGHT:
                przesun_w_prawo(rows, zawartosc_siatki, cols, flaga)
                dodaj_nowe_liczby(rows, zawartosc_siatki, cols)
                resetuj_flagi(flaga, rows, cols)
                
            elif event. key == pygame.K_UP:
                przesun_w_górę(rows, zawartosc_siatki, cols, flaga)
                dodaj_nowe_liczby(rows, zawartosc_siatki, cols)
                resetuj_flagi(flaga, rows, cols)
                
            elif event.key == pygame.K_DOWN:
                przesun_w_dół(rows, zawartosc_siatki, cols, flaga)
                dodaj_nowe_liczby(rows, zawartosc_siatki, cols)
                resetuj_flagi(flaga, rows, cols)
                


    





def main():
    global move
    global score
    
    while True:
        obsluga_klawiszy()
        screen.fill(background_color)
        siatka(rows, cols, zawartosc_siatki, screen, okno)
        losuj_liczbe(rows, cols, zawartosc_siatki, screen, okno, flaga)
        wynik(screen, score, width, height)
        pygame.display.flip()

if __name__ == "__main__":
    main()
