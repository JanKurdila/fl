# Flappy Bird  - Skákajúci vtak medzi pohybujúcimi sa prekážkami

![alt text](Obrázky/hra.jpg)

# KONFIGURÁCIA
Nastavenia hry sú spravované prostredníctvom konfiguračného súboru (config.py). 


## Vysvetlenie kódu

### Hlavné funkcie
    display_obstacles(obstacle_x, height)
    '''Kreslí prekážky na obrazovke.'''

    game_over()
    '''Zobrazí správu "Game Over" a ukončí hru.'''
## Hlavná herná slučka
    1) Inicializuje Pygame a nastaví herné okno.
    2) Načíta obrázky pozadia a vtáka.
    3) Nastaví počiatočné herné premenné (rýchlosť vtáka, gravitácia, vlastnosti prekážok, skóre atď.).
    4) Obsahuje hlavnú hernú slučku, ktorá:
    - Spracováva užívateľský vstup (medzerník na pohyb vtáka nahor).
    - Aplikuje gravitáciu na vtáka.
    - Aktualizuje pozíciu vtáka a kontroluje zrážky s okrajmi obrazovky a prekážkami.
    - Pohybuje prekážky a kontroluje skórovanie.
    - Vykresľuje herné prvky (pozadie, vták, prekážky, skóre).
    - Riadi počet snímok za sekundu.

## Ovládanie hry
Medzerník: Pohyb vtáka nahor.

## Podrobnejší popis
Prečítajte si jednotlivé commity od 0 smerom nahor. Sú výstižne pomenované, aby sme vedeli čo sme v nich riešili.