# pouzite knihovny
import pygame
import sys
import random

# nastaveni aplikace
rozmer_okna_x = 1600
rozmer_okna_y = 900

cernobily_rezim = False
max_velikost_micku = 50

# logika aplikace
pygame.init()

okno = pygame.display.set_mode((rozmer_okna_x, rozmer_okna_y))
pygame.display.set_caption("Míčeeek!")

micek = dict()

micek_w = random.randint(1, max_velikost_micku)
micek_h = micek_w

micek_x= random.randint(0, rozmer_okna_x - micek_w)
micek_y = random.randint(0, rozmer_okna_y - micek_h)

micek_dx = random.random() * random.choice([-1, 1])
micek_dy = random.random() * random.choice([-1, 1])

if cernobily_rezim:
    odstin = random.randint(0, 254)
    micek_rgb = (odstin, odstin, odstin)
else:
    micek_rgb = (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254))

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            sys.exit()
    
    okno.fill((255, 255, 255))
    
    micek_x = micek_x + micek_dx
    micek_y = micek_y + micek_dy
    
    if micek_y < 0:
        micek_y = 0
        micek_dy *= -1
    if micek_y > rozmer_okna_y - micek_h:
        micek_y = rozmer_okna_y - micek_h
        micek_dy *= -1
    if micek_x < 0:
        micek_x = 0
        micek_dx *= -1
    if micek_x > rozmer_okna_x - micek_w:
        micek_x = rozmer_okna_x - micek_w
        micek_dx *= -1
    
    pygame.draw.ellipse(okno, micek_rgb, (micek_x, micek_y, micek_w, micek_h))
    
    pygame.display.update()
