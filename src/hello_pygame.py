# Jdu programovat aplikaci s real-time grafikou...

# 1) pridam do ni knihovnu pygame
import pygame
import sys
import random
# 2) nastartuju knihovnu
pygame.init()
# 3) nastavim okno pro vykreslovani
rozmer_okna_x = 1600
rozmer_okna_y = 900
okno = pygame.display.set_mode((rozmer_okna_x, rozmer_okna_y))

cernobily_rezim = True
max_velikost_micku = 50
pocet_micku = 6000

# 4) uvodni nastaveni moji aplikace
x = []
y = []

w = []
h = []

dx = []
dy = []

rgb = []

for i in range(pocet_micku):
    # rozmery micku
    w.append(random.randint(1, max_velikost_micku))
    h.append(w[i])
    # pozice micku (omezene velikosti okna)
    x.append(random.randint(0, rozmer_okna_x - w[i]))
    y.append(random.randint(0, rozmer_okna_y - h[i]))
    # rychlosti micku (0 az 1 pixel za frame)
    dx.append(random.random())
    dy.append(random.random())
    # barvy micku (odstiny sede)
    if cernobily_rezim:
        odstin = random.randint(0, 254)
        rgb.append((odstin, odstin, odstin))
    else:
        rgb.append((random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))

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
    for i in range(len(x)):
        x[i] = x[i] + dx[i]

    for i in range(len(y)):
        y[i] = y[i] + dy[i]
    
    # pravidla pro odrazy
    for i in range(len(y)):
        if y[i] < 0:
            y[i] = 0
            dy[i] *= -1
        if y[i] > rozmer_okna_y - h[i]:
            y[i] = rozmer_okna_y - h[i]
            dy[i] *= -1
        
    for i in range(len(x)):
        if x[i] < 0:
            x[i] = 0
            dx[i] *= -1
        if x[i] > rozmer_okna_x - w[i]:
            x[i] = rozmer_okna_x - w[i]
            dx[i] *= -1
    
    # vykresleni tvaru
    for i in range(len(x)):
        pygame.draw.ellipse(okno, rgb[i], (x[i], y[i], w[i], h[i]))
    
    # prekresleni okna
    pygame.display.update()
