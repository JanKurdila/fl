import pygame
from Config import config
import sys
import random


# Inicializácia Pygame a nastavenia okna
pygame.init()
window = pygame.display.set_mode(config.ROZLISENIE)
pygame.display.set_caption("Flappy Bird")

# Načítanie pozadia a vtáka
pozadie = config.POZADIE
vtak = config.VTAK
vtak_rect = vtak.get_rect()
vtak_rect.x = config.ROZLISENIE[0] // 10
vtak_rect.y = config.ROZLISENIE[1] // 2

# Nastavenie hodín
clock = pygame.time.Clock()

# Rýchlosť vtáka a gravitácia
rychlost_vtaka = config.VTAK_RYCHLOST
gravitacia = config.GRAVITACIA

# Prekážky
sirka_prekazky = config.SIRKA_PREKAZKY
farba_prekazky = config.FARBA_PREKAZKY
zmena_xovej_suradnice_prekazky = config.ZMENA_XOVEJ_SURADNICE_PREKAZKY
pociatocna_suradnica_prekazky = config.ROZLISENIE[0]

# Funkcia na vykreslenie prekážok
def display_obstacle(obstacle_x, height):
    pygame.draw.rect(window, farba_prekazky, (obstacle_x, 0, sirka_prekazky, height))
    bottom_obstacle_height = config.ROZLISENIE[1] - height - 150
    pygame.draw.rect(window, farba_prekazky, (obstacle_x, config.ROZLISENIE[1], sirka_prekazky, -bottom_obstacle_height))

# Generovanie počiatočnej prekážky
vyska_prekazky = random.randint(150, 450)

# Herná slučka
while True:
    # Spracovanie udalostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rychlost_vtaka = config.STEP

    # Aplikácia gravitácie
    rychlost_vtaka += gravitacia
    vtak_rect.y += rychlost_vtaka

    # Pohyb prekážky
    pociatocna_suradnica_prekazky += zmena_xovej_suradnice_prekazky
    if pociatocna_suradnica_prekazky < -sirka_prekazky:
        pociatocna_suradnica_prekazky = config.ROZLISENIE[0]
        vyska_prekazky = random.randint(150, 450)

    # Vymazanie obrazovky a vykreslenie pozadia, vtáka a prekážok
    window.blit(pozadie, (0, 0))
    window.blit(vtak, vtak_rect)
    display_obstacle(pociatocna_suradnica_prekazky, vyska_prekazky)

    # Aktualizácia displeja
    pygame.display.update()

    # Spomalenie cyklu
    clock.tick(config.FPS)
