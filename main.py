import pygame
from Config import config
import sys

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

# Rýchlosť vtáka
rychlost_vtaka = config.VTAK_RYCHLOST
gravitacia = config.GRAVITACIA

while True:
    # Spracovanie udalostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rychlost_vtaka = -10

    # Aplikácia gravitácie
    rychlost_vtaka += gravitacia
    vtak_rect.y += rychlost_vtaka

    # Vymazanie obrazovky a vykreslenie pozadia a vtáka
    window.blit(pozadie, (0, 0))
    window.blit(vtak, vtak_rect)

    # Aktualizácia displeja
    pygame.display.update()

    # Spomalenie cyklu
    clock.tick(config.FPS)
