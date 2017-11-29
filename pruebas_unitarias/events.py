import pygame as pg
import pausa



def events(tecla, presionar):
    playing = True
    running = True
    for event in range(5):
        if tecla == "q":
            if playing:
                playing = False
            running = False
            return "salir del juego"
        if presionar == "si":
            if tecla == "barra_espaciadora":
                return "saltar"
            if tecla == "p":
                return "juego pausado"
                e = pausa.pausa("c", presionar)
                if e == "salir al menu":
                    playing = False
                    running = False
                    return "salir al menu"
