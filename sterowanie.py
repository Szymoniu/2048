import pygame
import random


def dodaj_nowe_liczby(rows, zawartosc_siatki, cols):
    
    empty_cells = [(i, j) for i in range(rows) for j in range(cols) if zawartosc_siatki[i][j] == 0]

    # Dodawanie dwóch nowych wartości "2"
    for _ in range(1):
        if move and empty_cells:
            row, col = random.choice(empty_cells)
            zawartosc_siatki[row][col] = 2
            empty_cells.remove((row, col))
    


def przesun_w_lewo(rows, zawartosc_siatki, cols, flaga):
    global move 
    move = False
    global score
    score = 0
    for row in range(rows):
        for col in range(cols - 1, 0, -1):
            if zawartosc_siatki[row][col] !=0:
                for k in range(col - 1, -1, -1):
                    if zawartosc_siatki[row][k] == 0:
                        zawartosc_siatki[row][k] = zawartosc_siatki[row][col]
                        zawartosc_siatki[row][col] = 0
                        move = True
                        break
                    elif zawartosc_siatki[row][k] == zawartosc_siatki[row][col] and not flaga[row][k]:
                        zawartosc_siatki[row][k] *= 2
                        zawartosc_siatki[row][col] = 0
                        flaga[row][k] = True
                        move = True
                        score += zawartosc_siatki[row][k]
                        break
                    else:
                        break 
                    
                
def przesun_w_prawo(rows, zawartosc_siatki, cols, flaga):
    global move
    move = False
    global score
    score = 0
    for row in range(rows):
        for col in range(cols - 1):
            if zawartosc_siatki[row][col] != 0:
                for k in range(col + 1, cols):
                    if zawartosc_siatki[row][k] == 0:
                        zawartosc_siatki[row][k] = zawartosc_siatki[row][col]
                        zawartosc_siatki[row][col] = 0
                        move = True
                        break
                    elif zawartosc_siatki[row][k] == zawartosc_siatki[row][col] and not flaga[row][k]:
                        zawartosc_siatki[row][k] *= 2
                        zawartosc_siatki[row][col] = 0
                        flaga[row][k] = True
                        move = True
                        score += zawartosc_siatki[row][k]
                        break
                    else:
                        break 

def przesun_w_dół(rows, zawartosc_siatki, cols, flaga):
    global move 
    move = False
    global score
    score = 0
    for col in range(cols):
        for row in range(rows - 1):
            if zawartosc_siatki[row][col] != 0:
                for k in range(row + 1, rows):
                    if zawartosc_siatki[k][col] == 0:
                        zawartosc_siatki[k][col] = zawartosc_siatki[row][col]
                        zawartosc_siatki[row][col] = 0
                        move = True
                        break
                    elif zawartosc_siatki[k][col] == zawartosc_siatki[row][col] and not flaga[k][col]:
                        zawartosc_siatki[k][col] *= 2
                        zawartosc_siatki[row][col] = 0
                        flaga[row][k] = True
                        move = True
                        score += zawartosc_siatki[k][col]
                        break
                    else:
                        break 




def przesun_w_górę(rows, zawartosc_siatki, cols, flaga):
    global move
    move = False
    global score
    score = 0
    for col in range(cols):
        for row in range(rows - 1, 0, -1):
            if zawartosc_siatki[row][col] != 0:
                for k in range(row -1, -1, -1):
                    if zawartosc_siatki[k][col] == 0:
                        zawartosc_siatki[k][col] = zawartosc_siatki[row][col]
                        zawartosc_siatki[row][col] = 0
                        move = True
                        break
                    elif zawartosc_siatki[k][col] == zawartosc_siatki[row][col] and not flaga[k][col]:
                        zawartosc_siatki[k][col] *= 2
                        zawartosc_siatki[row][col] = 0
                        flaga[row][k] = True
                        move = True
                        score += zawartosc_siatki[k][col]
                    else:
                        break 


def resetuj_flagi(flaga, rows, cols):
    for row in range(rows):
        for col in range(cols):
            flaga[row][col] = False
