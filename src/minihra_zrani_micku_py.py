# pouzite knihovny
import pygame
import sys
import math
import random

def udrzet_v_okne(obrazec):
    if obrazec["y"] < 0:
        obrazec["y"] = 0
    if obrazec["y"] > rozmer_okna_y - obrazec["h"]:
        obrazec["y"] = rozmer_okna_y - obrazec["h"]
    if obrazec["x"] < 0:
        obrazec["x"] = 0
    if obrazec["x"] > rozmer_okna_x - obrazec["w"]:
        obrazec["x"] = rozmer_okna_x - obrazec["w"]

def odrazit_od_kraje(obrazec):
    if obrazec["y"] < 0:
        obrazec["dy"] *= -1
    if obrazec["y"] > rozmer_okna_y - obrazec["h"]:
        obrazec["dy"] *= -1
    if obrazec["x"] < 0:
        obrazec["dx"] *= -1
    if obrazec["x"] > rozmer_okna_x - obrazec["w"]:
        obrazec["dx"] *= -1    

def ovladat_hrace(hrac):
    stisknuto = pygame.key.get_pressed()
    
    vektor_hrace = {"x": 0, "y": 0}
    
    if stisknuto[pygame.K_RIGHT]:
        vektor_hrace["x"] += 1
    if stisknuto[pygame.K_LEFT]:
        vektor_hrace["x"] -= 1
    if stisknuto[pygame.K_DOWN]:
        vektor_hrace["y"] += 1
    if stisknuto[pygame.K_UP]:
        vektor_hrace["y"] -= 1
    
    korekce = math.sqrt(vektor_hrace["x"] ** 2 + vektor_hrace["y"] ** 2)
    
    if korekce > 0:
        vektor_hrace["x"] /= korekce
        vektor_hrace["y"] /= korekce
    
    hrac["x"] += vektor_hrace["x"] * hrac["v"]
    hrac["y"] += vektor_hrace["y"] * hrac["v"]

def sezrat_okolni_micky(hrac, micky):
    for micek in micky:
        soucet_polomeru = (micek["w"] + hrac["w"]) / 2
        
        x1 = hrac["x"] + hrac["w"] / 2
        x2 = micek["x"] + micek["w"] / 2
        y1 = hrac["y"] + hrac["h"] / 2
        y2 = micek["y"] + micek["h"] / 2
        
        vzdalenost_stredu = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
        if vzdalenost_stredu < soucet_polomeru:
            micek["sezrany"] = True

def obnovit_po_sezrani_vsech(micky):
    for micek in micky:
        if not micek["sezrany"]:
            return
    
    for micek in micky:
        micek["sezrany"] = False

# nastaveni aplikace
rozmer_okna_x = 800
rozmer_okna_y = 600

cernobily_rezim = False
max_velikost_micku = 50

# logika aplikace
pygame.init()

okno = pygame.display.set_mode((rozmer_okna_x, rozmer_okna_y))
pygame.display.set_caption("Míčkyyy!")

rychlost_hrace = 2
pocet_micku = 1000
vsechny_micky = []

for i in range(pocet_micku):
    micek = dict()

    micek["w"] = random.randint(1, max_velikost_micku)
    micek["h"] = micek["w"]

    micek["x"] = random.randint(0, rozmer_okna_x - micek["w"])
    micek["y"] = random.randint(0, rozmer_okna_y - micek["h"])

    micek["dx"] = random.random() * random.choice([-1, 1])
    micek["dy"] = random.random() * random.choice([-1, 1])

    micek["sezrany"] = False

    if cernobily_rezim:
        odstin = random.randint(0, 254)
        micek["rgb"] = (odstin, odstin, odstin)
    else:
        micek["rgb"] = (random.randint(0, 254), random.randint(0, 254), random.randint(0, 254))
    
    vsechny_micky.append(micek)

hrac = dict()

hrac["w"] = 50
hrac["h"] = hrac["w"]

hrac["x"] = (rozmer_okna_x - hrac["w"]) / 2
hrac["y"] = (rozmer_okna_y - hrac["h"]) / 2

hrac["v"] = rychlost_hrace

hrac["rgb"] = (0, 0, 0)

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.KEYDOWN and udalost.key == pygame.K_ESCAPE:
            sys.exit()
        if udalost.type == pygame.QUIT:
            sys.exit()
    
    okno.fill((255, 255, 255))

    for micek in vsechny_micky:
        micek["x"] = micek["x"] + micek["dx"]
        micek["y"] = micek["y"] + micek["dy"]
        
        odrazit_od_kraje(micek)
        udrzet_v_okne(micek)
        
        if not micek["sezrany"]:
            pygame.draw.ellipse(okno, micek["rgb"], (micek["x"], micek["y"], micek["w"], micek["h"]))
    
    ovladat_hrace(hrac)
    udrzet_v_okne(hrac)
    
    sezrat_okolni_micky(hrac, vsechny_micky)
    obnovit_po_sezrani_vsech(vsechny_micky)
    
    pygame.draw.ellipse(okno, hrac["rgb"], (hrac["x"], hrac["y"], hrac["w"], hrac["h"]))
    
    pygame.display.update()
