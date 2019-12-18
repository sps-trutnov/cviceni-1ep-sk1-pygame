import pygame
import sys
import random

pygame.init()

rozmer_okna_x = 1600
rozmer_okna_y = 900
okno = pygame.display.set_mode((rozmer_okna_x, rozmer_okna_y))

cernobily_rezim = True
max_velikost_micku = 50
pocet_micku = 6000

x = []
y = []

w = []
h = []

dx = []
dy = []

rgb = []

for i in range(pocet_micku):
    w.append(random.randint(1, max_velikost_micku))
    h.append(w[i])
    
    x.append(random.randint(0, rozmer_okna_x - w[i]))
    y.append(random.randint(0, rozmer_okna_y - h[i]))
    
    dx.append(random.random())
    dy.append(random.random())
    
    if cernobily_rezim:
        odstin = random.randint(0, 254)
        rgb.append((odstin, odstin, odstin))
    else:
        rgb.append((random.randint(0, 254), random.randint(0, 254), random.randint(0, 254)))

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            sys.exit()
    
    okno.fill((255, 255, 255))
    
    for i in range(len(x)):
        x[i] = x[i] + dx[i]

    for i in range(len(y)):
        y[i] = y[i] + dy[i]
    
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
    
    for i in range(len(x)):
        pygame.draw.ellipse(okno, rgb[i], (x[i], y[i], w[i], h[i]))
    
    pygame.display.update()
