import pygame
import random

ROZLISENIE = (500, 700)


FPS = 20


POZADIE = pygame.image.load('Obrázky/po.jpg')
VTAK = pygame.image.load('Obrázky/bird1.png')

VTAK_RYCHLOST = 0
GRAVITACIA = 0.5

# Parametre prekážok
SIRKA_PREKAZKY = 70
FARBA_PREKAZKY = pygame.Color(211, 253, 117)
ZMENA_XOVEJ_SURADNICE_PREKAZKY = -4

STEP = -10
DIERA = 130