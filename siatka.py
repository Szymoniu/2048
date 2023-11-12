import pygame





def siatka(rows, cols, zawartosc_siatki, screen, okno):
    for row in range(rows):
        for col in range(cols):
            if zawartosc_siatki[row][col] == 2:
                color = ("#ADD8E6")  
            elif zawartosc_siatki[row][col] == 4:
                color = ("#4169E1")
            elif zawartosc_siatki[row][col] == 8:
                color = ("#4682B4")
            elif zawartosc_siatki[row][col] == 16:
                color = ("#7B68EE")
            elif zawartosc_siatki[row][col] == 32:
                color = ("#00FFFF")
            elif zawartosc_siatki[row][col] == 64:
                color = ("#7FFFD4")
            elif zawartosc_siatki[row][col] == 128:
                color = ("#40E0D0")
            elif zawartosc_siatki[row][col] == 256:
                color = ("#0000FF")
            elif zawartosc_siatki[row][col] == 512:
                color = ("#00008B")
            elif zawartosc_siatki[row][col] == 1024:
                color = ("#000080")
            elif zawartosc_siatki[row][col] == 2048:
                color = ("#191970")
            
            
            
            
            
            
            else:
                color = ("#E0FFFF")   

            pygame.draw.rect(screen, color, (col * okno, row * okno, okno, okno))
            pygame.draw.rect(screen, (0, 0, 0), (col * okno, row * okno, okno, okno), 2)