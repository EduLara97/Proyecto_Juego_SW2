import pygame as pg
from pygame import *
# from Entities.Entities import Character, Platform, Roca
from Entities.Entities import *
from GeneralInformation import *
import random
from os import *

game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, "assets/images")
img_enemigos_folder = path.join(img_folder, "enemigos")
img_escenarios_folder = path.join(img_folder, "escenarios")
img_intro_folder = path.join(img_folder, "intro")
img_objetos_folder = path.join(img_folder, "objetos")
img_obstaculos_folder = path.join(img_folder, "obstaculos")
img_personajes_folder = path.join(img_folder, "personajes")

pg.init()
pg.mixer.init()
pg.display.set_caption(TITLE)
screen = pg.display.set_mode(SIZE)
reloj = pg.time.Clock()

display_ancho = 800
display_altura = 600
pequenafont = pg.font.SysFont("comicsansms", 25)
medianofont = pg.font.SysFont("comicsansms", 50)
largofont = pg.font.SysFont("comicsansms", 80)

"""---------------------------------------------------------------"""
"""------------------INTRO GENERAL IMG----------------------------"""
"""---------------------------------------------------------------"""
bg_intro = pg.image.load("assets/images/intro/escenario_fondo_v2.jpg").convert()
bg_intro = pg.transform.scale(bg_intro, SIZE)

titulo_img_sheet = pg.image.load("assets/images/intro/titulo_juego_sheet.png").convert_alpha()
width_img_sheet = titulo_img_sheet.get_width()
sprites_image_sheet = []
for i in range(int(width_img_sheet / 200)):
    sprites_image_sheet.append(titulo_img_sheet.subsurface(i * 200, 0, 200, 200))

"""---------------------------------------------------------------"""
"""------------------BACKGROUND IMAGES----------------------------"""
"""---------------------------------------------------------------"""
bg_moche = pg.image.load("assets/images/escenarios/escenario_mochica.png").convert()
bg_moche = pg.transform.scale(bg_moche, SIZE)
bg_paracas = pg.image.load("assets/images/escenarios/escenario_paracas.png").convert()
bg_paracas = pg.transform.scale(bg_paracas, SIZE)
bg_tiahua = pg.image.load("assets/images/escenarios/escenario_tiahua.png").convert()
bg_tiahua = pg.transform.scale(bg_tiahua, SIZE)
bg_wari = pg.image.load("assets/images/escenarios/escenario_chavin.png").convert()
bg_wari = pg.transform.scale(bg_wari, SIZE)

"""---------------------------------------------------------------"""
"""------------------INTRO MODO IMAGES----------------------------"""
"""---------------------------------------------------------------"""
mode_arcade = pg.image.load("assets/images/intro/modo_arcade.gif").convert()
mode_arcade = pg.transform.scale(mode_arcade, (300, 300))
mode_single = pg.image.load("assets/images/intro/modo_single.gif").convert()
mode_single = pg.transform.scale(mode_single, (300, 300))
title_arcade = pg.image.load("assets/images/intro/title_arcade.gif").convert()
title_arcade = pg.transform.scale(title_arcade, (300, 300))
title_single = pg.image.load("assets/images/intro/title_single.gif").convert()
title_single = pg.transform.scale(title_single, (300, 300))

mode_single_sheet = pg.image.load("assets/images/intro/mode_single_sheet.png").convert_alpha()
width_mode_single_sheet = mode_single_sheet.get_width()
sprites_mode_sigle_sheet = []
for i in range(int(width_mode_single_sheet / 200)):
    sprites_mode_sigle_sheet \
        .append(pg.transform.scale(mode_single_sheet.subsurface(i * 200, 0, 200, 200), (300, 300)))

mode_arcade_sheet = pg.image.load("assets/images/intro/mode_arcade_sheet.png").convert_alpha()
width_mode_arcade_sheet = mode_arcade_sheet.get_width()
sprites_mode_arcade_sheet = []
for i in range(int(width_mode_arcade_sheet / 200)):
    sprites_mode_arcade_sheet \
        .append(pg.transform.scale(mode_arcade_sheet.subsurface(i * 200, 0, 200, 200), (300, 300)))
"""---------------------------------------------------------------"""
"""------------------INTRO ESCENARIO IMAGES-----------------------"""
"""---------------------------------------------------------------"""
altEs = 100
anchEs = 200
escenario_moche = pg.image.load("assets/images/escenarios/escenario_mochica.png").convert()
escenario_moche = pg.transform.scale(escenario_moche, (anchEs, altEs))
escenario_tiahua = pg.image.load("assets/images/escenarios/escenario_tiahua.png").convert()
escenario_tiahua = pg.transform.scale(escenario_tiahua, (anchEs, altEs))
escenario_paracas = pg.image.load("assets/images/escenarios/escenario_paracas.png").convert()
escenario_paracas = pg.transform.scale(escenario_paracas, (anchEs, altEs))
escenario_wari = pg.image.load("assets/images/escenarios/escenario1.png").convert()
escenario_wari = pg.transform.scale(escenario_wari, (anchEs, altEs))

"""---------------------------------------------------------------"""
"""------------------INTRO PERSONAJE IMAGES-----------------------"""
"""---------------------------------------------------------------"""
altPer = 150
anchPer = 150
perso_moche = pg.image.load("assets/images/intro/perso_moche.gif").convert()
perso_moche = pg.transform.scale(perso_moche, (anchPer, altPer))
perso_paracas = pg.image.load("assets/images/intro/perso_paracas.gif").convert()
perso_paracas = pg.transform.scale(perso_paracas, (anchPer, altPer))
perso_tiahua = pg.image.load("assets/images/intro/perso_tiahua.gif").convert()
perso_tiahua = pg.transform.scale(perso_tiahua, (anchPer, altPer))
perso_wari = pg.image.load("assets/images/intro/perso_wari.png").convert()
perso_wari = pg.transform.scale(perso_wari, (anchPer, altPer))

"""---------------------------------------------------------------"""
"""---------------------------------------------------------------"""
"""---------------------------------------------------------------"""

lista_perso = ["assets/images/personajes/inca_mochica.png",
               "assets/images/personajes/inca_paracas.png",
               "assets/images/personajes/inca_tiahuanaco.png",
               "assets/images/personajes/inca_wari.png"]

lista_escenarios = [bg_moche,
                    bg_paracas,
                    bg_tiahua,
                    bg_wari]


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
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    pausado = False
                """elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()"""
        screen.blit(bg_intro, (0, 0))
        message_to_screen("Pausado", ORANGE, -100, "mediano")
        message_to_screen("Presiona C para continuar", BLACK, 25, "pequena")
        pg.display.update()
        reloj.tick(5)


def pantalla_info():
    pausado = True
    while pausado:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    pausado = False
        screen.blit(bg_intro, (0, 0))
        message_to_screen("Información de la cultura", ORANGE, -100, "mediano")
        message_to_screen("Aqui se mostrara información acerca de la cultura", BLACK, 25, "pequena")
        message_to_screen("Presiona C para continuar", BLACK, 125, "pequena")
        pg.display.update()
        reloj.tick(5)


def intro_modo(intro):
    i2, i3, i4 = 0, 0, 0
    while intro:
        mx, my = pg.mouse.get_pos()
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                modo = seleccionarModo(mx, my)
                if modo > 0: return modo
        screen.blit(bg_intro, (0, 0))
        screen.blit(mode_arcade, (70, 250))
        screen.blit(mode_single, (450, 250))
        if 483 <= mx <= 659 and 275 <= my <= 537:
            screen.blit(sprites_mode_sigle_sheet[i3], (440, 80))
            i3 = (i3 + 1) % 4
            screen.blit(title_arcade, (70, 80))
        elif 164 <= mx <= 262 and 275 <= my <= 537:
            screen.blit(sprites_mode_arcade_sheet[i4], (70, 80))
            i4 = (i4 + 1) % 4
            screen.blit(title_single, (440, 80))
        else:
            screen.blit(title_single, (440, 80))
            screen.blit(title_arcade, (70, 80))
        screen.blit(sprites_image_sheet[i2], (300, -30))
        i2 = (i2 + 1) % 2
        message_to_screen("Escoger un modo de juego", BLACK, -160, "pequena")
        pg.display.update()
        reloj.tick(5)


def intro_escenario(intro):
    i2 = 0
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mx, my = pg.mouse.get_pos()
                escenario = seleccionarEscenario(mx, my)
                if escenario > 0: return escenario

        screen.blit(bg_intro, (0, 0))
        screen.blit(escenario_moche, (110, 220))
        screen.blit(escenario_tiahua, (490, 220))
        screen.blit(escenario_paracas, (110, 400))
        screen.blit(escenario_wari, (490, 400))
        screen.blit(sprites_image_sheet[i2], (300, -30))
        i2 = (i2 + 1) % 2
        message_to_screen("Escoger un escenario", BLACK, -160, "pequena")
        pg.display.update()
        reloj.tick(5)


def intro_personaje(intro):
    i2 = 0
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mx, my = pg.mouse.get_pos()
                personaje = seleccionarPersonaje(mx, my)
                if personaje > 0: return personaje

        screen.blit(bg_intro, (0, 0))
        screen.blit(perso_moche, (180, 200))
        screen.blit(perso_paracas, (490, 200))
        screen.blit(perso_tiahua, (180, 400))
        screen.blit(perso_wari, (490, 400))
        screen.blit(sprites_image_sheet[i2], (300, -30))
        i2 = (i2 + 1) % 2
        message_to_screen("Elegir un personaje", BLACK, -160, "pequena")
        pg.display.update()
        reloj.tick(5)


def intro_final(intro):
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYUP:
                intro = False
        screen.blit(bg_intro, (0, 0))
        message_to_screen(TITLE, ORANGE, -160, "mediano")
        message_to_screen(
            "Arrows to move, Space to jump", BLACK, -50, "pequena")
        message_to_screen(
            "Press a key to play", BLACK, 100, "pequena")
        pg.display.update()
        reloj.tick(5)


def into_juego():
    intro = True
    modo = intro_modo(intro)
    escenario = intro_escenario(intro)
    personaje = intro_personaje(intro)
    intro_final(intro)
    perso = lista_perso[personaje - 1]
    esce = lista_escenarios[escenario - 1]
    return esce, perso


def gameOver(score):
    intro = True
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    intro = False
        screen.blit(bg_intro, (0, 0))
        message_to_screen("GAME OVER", ORANGE, -100, "mediano")
        message_to_screen("Score: " + str(score), BLACK, -60, "pequena")
        message_to_screen(
            "Presiona C para volver a jugar", BLACK, 25, "pequena")
        pg.display.update()
        reloj.tick(5)


class Game:
    def __init__(self, escena):
        # initialize game window, etc
        self.dir = path.dirname(__file__)
        self.platforms = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.carteles = pg.sprite.Group()
        self.checkpoints = pg.sprite.Group()
        self.score = 0
        self.escenario = escena
        self.show_cartel = True
        self.posCheckpoint = (0, 0)
        self.confirmCheckpoint = False
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.img_dir = path.join(self.dir, "assets/images/personajes")
        self.sprites = Spritesheet(path.join(self.img_dir, SPRITESHEET))
        self.player = Player(self)
        self.load_data()

    def load_data(self):
        # load spritesheet image
        pass

    def new(self):
        # start a new game
        self.all_sprites.add(self.player)
        t = Terreno(*PLATFORM_GROUND)
        c = Cartel(*CARTEL_LIST)
        ch = Checkpoint(*LLAMA_LIST)
        self.all_sprites.add(t)
        self.platforms.add(t)
        self.all_sprites.add(c)
        self.carteles.add(c)
        self.all_sprites.add(ch)
        self.checkpoints.add(ch)
        for coin in COINS_LIST:
            m = Moneda(*coin)
            self.all_sprites.add(m)
            self.coins.add(m)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if folling

        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        hits_coin = pg.sprite.spritecollide(self.player, self.coins, False)
        if hits_coin:
            for coin in self.coins:
                if self.player.rect.right >= coin.rect.center[0]:
                    coin.kill()
                    pg.mixer.Sound.play(pg.mixer.Sound("assets/audio/coin_sound.wav"))
                    self.score += 10

        hits_cartel = pg.sprite.spritecollide(self.player, self.carteles, False)
        if hits_cartel:
            for cartel in self.carteles:
                if self.player.rect.center[0] >= cartel.rect.center[0] and self.show_cartel:
                    pantalla_info()
                    self.show_cartel = False

        hits_checkpoint = pg.sprite.spritecollide(self.player, self.checkpoints, False)
        if hits_checkpoint:
            self.posCheckpoint = (self.player.rect.x, self.player.rect.y)
            self.confirmCheckpoint = True

        # If player reaches top 1/4 of screen
        if self.player.rect.right >= WIDTH - (WIDTH / 4):
            self.player.pos.x -= abs(self.player.vel.x)
            for plat in self.platforms:
                plat.rect.x -= abs(self.player.vel.x)
                if plat.rect.right <= 0:
                    # Si ya no aparece en la pantalla la plataforma desaparece
                    plat.kill()
            for coin in self.coins:
                coin.rect.x -= abs(self.player.vel.x)
            for cartel in self.carteles:
                cartel.rect.x -= abs(self.player.vel.x)
            for llama in self.checkpoints:
                llama.rect.x -= abs(self.player.vel.x)
        if self.player.rect.top > HEIGHT:
            for plat in self.platforms:
                plat.kill()
            for coin in self.coins:
                coin.kill()
            for cartel in self.carteles:
                cartel.kill()
            for llama in self.checkpoints:
                llama.kill()
            self.player.pos = self.posCheckpoint
            self.show_cartel = True
            self.playing = False

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                if event.key == pg.K_p:
                    pausa()

    def draw(self):
        # Game Loop - draw
        self.screen.blit(self.escenario, (0, 0))
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, BLACK, WIDTH / 2, 15)
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(SKY_BLUE)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Arrows to move, Space to jump", 22, WHITE, WIDTH / 2,
                       HEIGHT / 2)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        pass

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


def main(escena):
    g = Game(escena)
    # g.show_start_screen()
    pg.mixer.music.load("assets/audio/bg_opcion2.wav")
    pg.mixer.music.set_volume(0.5)
    pg.mixer.music.play(-1)
    while g.running:
        g.new()
        g.show_go_screen()

    pg.quit()

if __name__ == "__main__":
    ese, perso = into_juego()
    main(ese)
