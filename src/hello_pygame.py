# Jdu programovat aplikaci s real-time grafikou...

# 1) pridam do ni knihovnu pygame
import pygame
# 2) nastartuju knihovnu
pygame.init()
# 3) nastavim okno pro vykreslovani
okno = pygame.display.set_mode((640, 480))

# 4) uvodni nastaveni moji aplikace
# ...

# 5) nekonecna vykreslovaci smycka
while True:
    # premazani okna barvou pozadi
    okno.fill((255, 255, 255))
    
    # prekresleni okna
    pygame.display.update()
