import pygame
from Entities.Entities import Character
from GeneralInformation import SKY_BLUE, SIZE, WHITE, ORANGE, BLACK, ORANGE_LIGTH

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.mixer.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Platformer Example")

"""---------------------------------------------------------------"""
"""------------------INTRO GENERAL IMG----------------------------"""
"""---------------------------------------------------------------"""
bg_intro = pygame.image.load("assets/images/intro/escenario_fondo_v2.jpg").convert()
bg_intro = pygame.transform.scale(bg_intro, SIZE)

img_titulo = pygame.image.load("assets/images/intro/titulo_juego.gif").convert()
img_titulo = pygame.transform.scale(img_titulo, (300, 200))

"""---------------------------------------------------------------"""
"""------------------BACKGROUND IMAGES----------------------------"""
"""---------------------------------------------------------------"""
bg_moche = pygame.image.load("assets/images/escenarios/escenario_mochica.png").convert()
bg_moche = pygame.transform.scale(bg_moche, SIZE)
bg_paracas = pygame.image.load("assets/images/escenarios/escenario_paracas.png").convert()
bg_paracas = pygame.transform.scale(bg_paracas, SIZE)
bg_tiahua = pygame.image.load("assets/images/escenarios/escenario_tiahua.png").convert()
bg_tiahua = pygame.transform.scale(bg_tiahua, SIZE)
bg_wari = pygame.image.load("assets/images/escenarios/escenario_chavin.png").convert()
bg_wari = pygame.transform.scale(bg_wari, SIZE)


"""---------------------------------------------------------------"""
"""------------------INTRO MODO IMAGES----------------------------"""
"""---------------------------------------------------------------"""
mode_arcade = pygame.image.load("assets/images/intro/modo_arcade.gif").convert()
mode_arcade = pygame.transform.scale(mode_arcade, (300, 300))
mode_single = pygame.image.load("assets/images/intro/modo_single.gif").convert()
mode_single = pygame.transform.scale(mode_single, (300, 300))
title_arcade = pygame.image.load("assets/images/intro/title_arcade.png").convert()
title_arcade = pygame.transform.scale(title_arcade, (300, 100))
title_single = pygame.image.load("assets/images/intro/title_single.png").convert()
title_single = pygame.transform.scale(title_single, (300, 100))

"""---------------------------------------------------------------"""
"""------------------INTRO ESCENARIO IMAGES-----------------------"""
"""---------------------------------------------------------------"""
altEs = 100
anchEs = 200
escenario_moche = pygame.image.load("assets/images/escenarios/escenario_mochica.png").convert()
escenario_moche = pygame.transform.scale(escenario_moche, (anchEs, altEs))
escenario_tiahua = pygame.image.load("assets/images/escenarios/escenario_tiahua.png").convert()
escenario_tiahua = pygame.transform.scale(escenario_tiahua, (anchEs, altEs))
escenario_paracas = pygame.image.load("assets/images/escenarios/escenario_paracas.png").convert()
escenario_paracas = pygame.transform.scale(escenario_paracas, (anchEs, altEs))
escenario_wari = pygame.image.load("assets/images/escenarios/escenario1.png").convert()
escenario_wari = pygame.transform.scale(escenario_wari, (anchEs, altEs))

"""---------------------------------------------------------------"""
"""------------------INTRO PERSONAJE IMAGES-----------------------"""
"""---------------------------------------------------------------"""
altPer = 150
anchPer = 150
perso_moche = pygame.image.load("assets/images/intro/perso_moche.gif").convert()
perso_moche = pygame.transform.scale(perso_moche, (anchPer, altPer))
perso_paracas = pygame.image.load("assets/images/intro/perso_paracas.gif").convert()
perso_paracas = pygame.transform.scale(perso_paracas, (anchPer, altPer))
perso_tiahua = pygame.image.load("assets/images/intro/perso_tiahua.gif").convert()
perso_tiahua = pygame.transform.scale(perso_tiahua, (anchPer, altPer))
perso_wari = pygame.image.load("assets/images/intro/perso_wari.png").convert()
perso_wari = pygame.transform.scale(perso_wari, (anchPer, altPer))

"""---------------------------------------------------------------"""
"""---------------------------------------------------------------"""
"""---------------------------------------------------------------"""

lista_perso= ["assets/images/personajes/inca_mochica.png",
              "assets/images/personajes/inca_paracas.png",
              "assets/images/personajes/inca_tiahuanaco.png",
              "assets/images/personajes/inca_wari.png"]

lista_escenarios = [bg_moche,
                    bg_paracas,
                    bg_tiahua,
                    bg_wari]

reloj = pygame.time.Clock()
display_ancho = 800
display_altura = 600
pequenafont = pygame.font.SysFont("comicsansms", 25)
medianofont = pygame.font.SysFont("comicsansms", 50)
largofont = pygame.font.SysFont("comicsansms", 80)


def message_to_screen(msg, color, y_displace=0, tamano_letra="pequena"):
    textSur, textRect = text_objetos(msg, color, tamano_letra)
    textRect.center = (display_ancho / 2), (display_altura / 2) + y_displace
    screen.blit(textSur, textRect)


def text_objetos(text, color, tamano_letra):
    if tamano_letra == "pequena":
        textSuperficie = pequenafont.render(text, True, color)
    elif tamano_letra == "mediano":
        textSuperficie = medianofont.render(text, True, color)
    elif tamano_letra == "largo":
        textSuperficie = largofont.render(text, True, color)
    return textSuperficie, textSuperficie.get_rect()


def seleccionarModo(mx, my):
    if 483 <= mx <= 659 and 275 <= my <= 537:
        return 2
    elif 164 <= mx <= 262 and 275 <= my <= 537:
        return 0
    else:
        return 0


def seleccionarEscenario(mx, my):
    if 110 <= mx <= 310 and 219 <= my <= 322:
        return 1
    elif 489 <= mx <= 690 and 219 <= my <= 322:
        return 2
    elif 110 <= mx <= 310 and 399 <= my <= 500:
        return 3
    elif 489 <= mx <= 690 and 399 <= my <= 500:
        return 4
    else:
        return 0


def seleccionarPersonaje(mx, my):
    if 211 <= mx <= 292 and 202 <= my <= 344:
        return 1
    elif 512 <= mx <= 615 and 202 <= my <= 344:
        return 2
    elif 211 <= mx <= 292 and 413 <= my <= 546:
        return 3
    elif 512 <= mx <= 615 and 413 <= my <= 546:
        return 4
    else:
        return 0

def pausa():
    pausado = True
    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False
                """elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()"""
        screen.blit(bg_intro, (0, 0))
        message_to_screen("Pausado", ORANGE, -100, "mediano")
        message_to_screen("Presiona C para continuar",BLACK, 25, "pequena")
        pygame.display.update()
        reloj.tick(5)


def intro_modo(intro):
    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                modo = seleccionarModo(mx, my)
                if modo > 0: return modo
        screen.blit(bg_intro, (0, 0))
        screen.blit(mode_arcade, (70, 250))
        screen.blit(mode_single, (450, 250))
        screen.blit(title_arcade, (70, 170))
        screen.blit(title_single, (450, 170))
        screen.blit(img_titulo, (250, -30))
        message_to_screen("Escoger un modo de juego", BLACK, -160, "pequena")
        pygame.display.update()
        reloj.tick(5)


def intro_escenario(intro):
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                escenario = seleccionarEscenario(mx, my)
                if escenario > 0: return escenario

        screen.blit(bg_intro, (0, 0))
        screen.blit(escenario_moche, (110, 220))
        screen.blit(escenario_tiahua, (490, 220))
        screen.blit(escenario_paracas, (110, 400))
        screen.blit(escenario_wari, (490, 400))
        screen.blit(img_titulo, (250, -30))
        message_to_screen("Escoger un escenario", BLACK, -160, "pequena")
        pygame.display.update()
        reloj.tick(5)


def intro_personaje(intro):
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                personaje = seleccionarPersonaje(mx, my)
                if personaje > 0: return personaje

        screen.blit(bg_intro, (0, 0))
        screen.blit(perso_moche, (180, 200))
        screen.blit(perso_paracas, (490, 200))
        screen.blit(perso_tiahua, (180, 400))
        screen.blit(perso_wari, (490, 400))
        screen.blit(img_titulo, (250, -30))
        message_to_screen("Elegir un personaje", BLACK, -160, "pequena")
        pygame.display.update()
        reloj.tick(5)


def into_juego():
    intro = True
    modo = intro_modo(intro)
    escenario = intro_escenario(intro)
    personaje = intro_personaje(intro)
    perso = lista_perso[personaje-1]
    esce = lista_escenarios[escenario-1]
    return esce, perso


class Main(object):
    def __init__(self, esce, perso):
        self.runing = True
        self.clock = pygame.time.Clock()
        self.drawable_sprites = pygame.sprite.Group()
        self.character = Character(screen, SIZE[0] / 2, 0, perso)
        self.drawable_sprites.add(self.character)
        self.escenario = esce

    def keydown(self, event_key):
        """Cada vez que se oprime una tecla"""
        self.character.key_down(event_key)

    def keyup(self, event_key):
        """Cada vez que se deja de oprimir"""
        self.character.key_up(event_key)

    def main(self):
        pygame.mixer.music.load("assets/audio/bg_opcion2.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        x = 0
        while self.runing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        x = - 4
                    elif event.key == pygame.K_p:
                        pausa()
                    self.keydown(event.key)

                if event.type == pygame.KEYUP:
                    x = 0
                    self.keyup(event.key)

            screen.fill(SKY_BLUE)
            screen.blit(self.escenario, (0, 0))
            dt = self.clock.tick(60)
            self.character.update(dt)
            self.drawable_sprites.draw(screen)
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    ese, perso = into_juego()
    m = Main(ese, perso)
    m.main()
