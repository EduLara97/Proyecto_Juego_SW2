import pygame as pg
pg.init()

def pausa(tecla, presionar):
    pausado = True
    while pausado:
        for event in range(5):
            if tecla == "q":
                return "salir juego"
            if presionar == "si":
                if tecla == "c":
                    pausado = False
                    return "continuar"
                if tecla == "x":
                    return "salir al menu"
