import pygame
from Config import config
import sys
import random

# Funkcia na vykreslenie prekážok
def display_obstacles(obstacle_x, height):
    pygame.draw.rect(window, farba_prekazky, (obstacle_x, 0, sirka_prekazky, height))
    bottom_obstacle_height = config.ROZLISENIE[1] - height - diera
    pygame.draw.rect(window, farba_prekazky, (obstacle_x, config.ROZLISENIE[1] - bottom_obstacle_height, sirka_prekazky, bottom_obstacle_height))

# Funkcia pre koniec hry
def game_over():
    font = config.FONT
    text = font.render("Game Over", True, (255, 0, 0))
    text_rect = text.get_rect(center=(config.ROZLISENIE[0] / 2, config.ROZLISENIE[1] / 2))
    window.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)  # Čaká 2 sekundy
    pygame.quit()
    sys.exit()

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
rychlost_vtaka = 0
gravitacia = config.GRAVITACIA

# Prekážky
sirka_prekazky = config.SIRKA_PREKAZKY
farba_prekazky = config.FARBA_PREKAZKY
zmena_xovej_suradnice_prekazky = config.ZMENA_XOVEJ_SURADNICE_PREKAZKY
pociatocna_suradnica_prekazky = config.ROZLISENIE[0]

# Konštantná diera medzi prekážkami
diera = config.DIERA

# Generovanie počiatočnej výšky prekážky
vyska_prekazky = random.randint(150, config.ROZLISENIE[1] - diera - 150)


# Skóre
skore = 0
font = config.FONT

# Premenná na sledovanie, či vták preletel prekážku
prekazka_preletena = False

# Herná slučka
while True:
    # Spracovanie udalostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Ovládanie vtáka smerom nahor pomocou medzerníka
                rychlost_vtaka = config.STEP

    # Aplikácia gravitácie
    rychlost_vtaka += gravitacia
    vtak_rect.y += rychlost_vtaka

    # Kontrola, aby vták neprešiel cez hornú alebo spodnú hranu obrazovky
    if vtak_rect.y < 0:
        vtak_rect.y = 0
        rychlost_vtaka = 0
    elif vtak_rect.y > config.ROZLISENIE[1] - vtak_rect.height:
        vtak_rect.y = config.ROZLISENIE[1] - vtak_rect.height
        rychlost_vtaka = 0

    # Zvýšenie skóre, ak vták preletí bez kolízie prekážky
    if pociatocna_suradnica_prekazky + sirka_prekazky < vtak_rect.x and not prekazka_preletena:
        skore += 1
        prekazka_preletena = True
    elif pociatocna_suradnica_prekazky + sirka_prekazky >= vtak_rect.x:
        prekazka_preletena = False

    # Pohyb prekážky
    pociatocna_suradnica_prekazky += zmena_xovej_suradnice_prekazky
    if pociatocna_suradnica_prekazky < -sirka_prekazky:
        pociatocna_suradnica_prekazky = config.ROZLISENIE[0]
        vyska_prekazky = random.randint(150, config.ROZLISENIE[1] - diera - 150)

    if pociatocna_suradnica_prekazky < -sirka_prekazky:
        pociatocna_suradnica_prekazky = config.ROZLISENIE[0]
        vyska_prekazky = random.randint(150, config.ROZLISENIE[1] - diera - 150)
           


    # Kontrola kolízie vtáka s prekážkami
    if vtak_rect.colliderect(pygame.Rect(pociatocna_suradnica_prekazky, 0, sirka_prekazky, vyska_prekazky)) or vtak_rect.colliderect(pygame.Rect(pociatocna_suradnica_prekazky, config.ROZLISENIE[1] - (config.ROZLISENIE[1] - vyska_prekazky - diera), sirka_prekazky, config.ROZLISENIE[1] - vyska_prekazky - diera)):
        game_over()

    # Vymazanie obrazovky a vykreslenie pozadia, vtáka a prekážok
    window.fill((0, 0, 0))  # Vymazanie obrazovky čiernou farbou
    window.blit(pozadie, (0, 0))
    window.blit(vtak, vtak_rect)
    display_obstacles(pociatocna_suradnica_prekazky, vyska_prekazky)

    # Zobrazenie skóre
    text = font.render("Score: " + str(skore), True, (255, 255, 255))
    window.blit(text, (10, 10))

    # Aktualizácia displeja
    pygame.display.update()

    # Spomalenie cyklu
    clock.tick(config.FPS)

