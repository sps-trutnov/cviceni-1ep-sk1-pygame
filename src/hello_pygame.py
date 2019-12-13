# Jdu programovat aplikaci s real-time grafikou...

# 1) pridam do ni knihovnu pygame
import pygame
import sys
# 2) nastartuju knihovnu
pygame.init()
# 3) nastavim okno pro vykreslovani
rozmer_okna_x = 800
rozmer_okna_y = 600
okno = pygame.display.set_mode((rozmer_okna_x, rozmer_okna_y))

# 4) uvodni nastaveni moji aplikace
x = 200
y = 200
w = h = 50

dx = 0.1
dy = -0.05

# 5) nekonecna vykreslovaci smycka
while True:
    # z udalosti, ktere nastaly...
    for udalost in pygame.event.get():
        # nastala udalost VYPNUTI ?
        if udalost.type == pygame.QUIT:
            # vypnu aplikaci
            sys.exit()
    
    # premazani okna barvou pozadi
    okno.fill((255, 255, 255))
    
    # rovnice pohybu
    x = x + dx
    y = y + dy
    
    # pravidla pro odrazy
    if y < 0:
        y = 0
        dy *= -1
    if y > rozmer_okna_y - h:
        y = rozmer_okna_y - h
        dy *= -1
        
    if x < 0:
        x = 0
        dx *= -1
    if x > rozmer_okna_x - w:
        x = rozmer_okna_x - w
        dx *= -1
    
    # vykresleni tvaru
    pygame.draw.ellipse(okno, (0, 0, 0), (x, y, w, h))
    pygame.draw.ellipse(okno, (0, 0, 0), (x, y, w, h))
    
    # prekresleni okna
    pygame.display.update()
