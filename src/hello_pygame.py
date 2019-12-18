# pouzite knihovny
import pygame
import sys
import random

# nastaveni aplikace
rozmer_okna_x = 1600
rozmer_okna_y = 900

cernobily_rezim = False
max_velikost_micku = 50

pocet_micku = 6000

# logika aplikace
pygame.init()

okno = pygame.display.set_mode((rozmer_okna_x, rozmer_okna_y))
pygame.display.set_caption("Míčkyyy!")

micky = []

for i in range(pocet_micku):
    micek = dict()
    
    micek['w'] = random.randint(1, max_velikost_micku)
    micek['h'] = micek['w']
    
    micek['x']= random.randint(0, rozmer_okna_x - micek['w'])
    micek['y'] = random.randint(0, rozmer_okna_y - micek['h'])
    
    micek['dx'] = random.random() * random.choice([-1, 1])
    micek['dy'] = random.random() * random.choice([-1, 1])
    
    if cernobily_rezim:
        odstin = random.randint(1, 254)
        micek['rgb'] = (odstin, odstin, odstin)
    else:
        micek['rgb'] = (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))
    
    micky.append(micek)

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.KEYDOWN and udalost.key == pygame.K_ESCAPE:
            sys.exit()
        if udalost.type == pygame.QUIT:
            sys.exit()
    
    okno.fill((255, 255, 255))
    
    for micek in micky:
        micek['x'] = micek['x'] + micek['dx']
        micek['y'] = micek['y'] + micek['dy']
        
        if micek['y'] < 0:
            micek['y'] = 0
            micek['dy'] *= -1
        if micek['y'] > rozmer_okna_y - micek['h']:
            micek['y'] = rozmer_okna_y - micek['h']
            micek['dy'] *= -1
        if micek['x'] < 0:
            micek['x'] = 0
            micek['dx'] *= -1
        if micek['x'] > rozmer_okna_x - micek['w']:
            micek['x'] = rozmer_okna_x - micek['w']
            micek['dx'] *= -1
    
        pygame.draw.ellipse(okno, micek['rgb'], (micek['x'], micek['y'], micek['w'], micek['h']))
    
    pygame.display.update()
