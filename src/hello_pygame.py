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
    
    # vykresleni tvaru (obdelniku)
    pygame.draw.rect(okno, (0, 0, 0), (100, 200, 50, 40))
    # vykresleni tvaru (elipsy)
    pygame.draw.ellipse(okno, (0, 0, 0), (300, 200, 40, 60))
    # vykresleni tvaru (ctverce)
    pygame.draw.rect(okno, (0, 0, 0), (400, 250, 50, 50))
    # vykresleni tvaru (kruhu)
    pygame.draw.ellipse(okno, (0, 0, 0), (400, 350, 40, 40))
    
    # prekresleni okna
    pygame.display.update()
