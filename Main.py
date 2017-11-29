import pygame as pg
from pygame import *
# from Entities.Entities import Character, Platform, Roca
import io
from Entities.Entities import *
from GeneralInformation import *
from urllib.request import urlopen
import random
import requests
from CBForm import *
from os import *

posturl="http://runinkarun.herokuapp.com/score/api"

URL_IMAGE = "http://res.cloudinary.com/dfktnvqxe/image/upload/v1511719844/escenario_fondo_v2_ikkq4e.jpg"
IMAGE_STR = urlopen(URL_IMAGE).read()
IMAGE_FILE = io.BytesIO(IMAGE_STR)

game_folder = path.dirname("")
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
microfont = pg.font.SysFont("comicsansms", 20)
pequenafont = pg.font.SysFont("comicsansms", 25)
medianofont = pg.font.SysFont("comicsansms", 50)
largofont = pg.font.SysFont("comicsansms", 80)

# Se realiza la carga del fondo (background) que tendran todas las pantallas de la intro
#bg_intro = pg.image.load("assets/images/intro/escenario_fondo_v2.jpg").convert()
bg_intro = pg.image.load(IMAGE_FILE).convert()
bg_intro = pg.transform.scale(bg_intro, SIZE)

# Se realiza la carga del titulo del juego, para la animación de este, se tiene un sprite sheet
# el cual sera pasado a un array para manejarlo de mejor manera
titulo_img_sheet = pg.image.load("assets/images/intro/titulo_juego_sheet.png").convert_alpha()
width_img_sheet = titulo_img_sheet.get_width()
sprites_image_sheet = []
for i in range(int(width_img_sheet / 200)):
    sprites_image_sheet.append(titulo_img_sheet.subsurface(i * 200, 0, 200, 200))

# En esta sección se realiza la carga de los escenarios (backgrounds) que
# tendra disponible el juego (imagenes unicas)
bg_moche = pg.image.load("assets/images/escenarios/escenario_mochica.png").convert()
bg_moche = pg.transform.scale(bg_moche, SIZE)
bg_paracas = pg.image.load("assets/images/escenarios/escenario_paracas.png").convert()
bg_paracas = pg.transform.scale(bg_paracas, SIZE)
bg_tiahua = pg.image.load("assets/images/escenarios/escenario_tiahua.png").convert()
bg_tiahua = pg.transform.scale(bg_tiahua, SIZE)
bg_wari = pg.image.load("assets/images/escenarios/escenario_chavin.png").convert()
bg_wari = pg.transform.scale(bg_wari, SIZE)

# En esta sección se realiza la carga de las imagenes que apareceran en la sección
# de intro de modo de juego. mode = imagen sobre la que se hara click, title = titulo que
# aparece encima de las imagenes de los modos de juego (son sprite sheets)
mode_arcade = pg.image.load("assets/images/intro/modo_arcade.gif").convert()
mode_arcade = pg.transform.scale(mode_arcade, (300, 300))
mode_single = pg.image.load("assets/images/intro/modo_single.gif").convert()
mode_single = pg.transform.scale(mode_single, (300, 300))
title_arcade = pg.image.load("assets/images/intro/title_arcade.gif").convert()
title_arcade = pg.transform.scale(title_arcade, (300, 300))
title_single = pg.image.load("assets/images/intro/title_single.gif").convert()
title_single = pg.transform.scale(title_single, (300, 300))
title_ranking = pg.image.load("assets/images/intro/ranking.gif").convert()
title_ranking = pg.transform.scale(title_ranking, (300, 300))


# el sprite sheet de las imagenes del modo single se pasan a un array de imagenes, donde
# se contiene cada una de las secciones que conformaban el sprite sheet
mode_single_sheet = pg.image.load("assets/images/intro/mode_single_sheet.png").convert_alpha()
width_mode_single_sheet = mode_single_sheet.get_width()
sprites_mode_sigle_sheet = []
for i in range(int(width_mode_single_sheet / 200)):
    sprites_mode_sigle_sheet \
        .append(pg.transform.scale(mode_single_sheet.subsurface(i * 200, 0, 200, 200), (300, 300)))

# el sprite sheet de las imagenes del modo arcade se pasan a un array de imagenes, donde
# se contiene cada una de las secciones que conformaban el sprite sheet
mode_arcade_sheet = pg.image.load("assets/images/intro/mode_arcade_sheet.png").convert_alpha()
width_mode_arcade_sheet = mode_arcade_sheet.get_width()
sprites_mode_arcade_sheet = []
for i in range(int(width_mode_arcade_sheet / 200)):
    sprites_mode_arcade_sheet \
        .append(pg.transform.scale(mode_arcade_sheet.subsurface(i * 200, 0, 200, 200), (300, 300)))
        
# el sprite sheet de las imagenes del modo arcade se pasan a un array de imagenes, donde
# se contiene cada una de las secciones que conformaban el sprite sheet
mode_ranking_sheet = pg.image.load("assets/images/intro/ranking.png").convert_alpha()
width_mode_ranking_sheet = mode_ranking_sheet.get_width()
sprites_mode_ranking_sheet = []
for i in range(int(width_mode_ranking_sheet / 200)):
    sprites_mode_ranking_sheet \
        .append(pg.transform.scale(mode_ranking_sheet.subsurface(i * 200, 0, 200, 200), (300, 300)))       

# En esta sección se realiza la carga de los escenarios que podran estar incluidos en el juego,
# estas son imagenes unicas (no sprite sheets), ya que solo van a ir en la intro del modo soigle
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

# En esta sección se realiza la carga de los personajes (incas) que estaran disponibles en el juego,
# estas son imagenes unicas (no sprite sheets), ya que van a ir solo en la intro del modo single
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
perso_wari.set_colorkey(WHITE)

# lista de las imagenes de los incas (sprite sheets)
lista_perso = ["inca_mochica.png",
               "inca_paracas.png",
               "inca_tiahuanaco.png",
               "inca_wari.png"]

# lista de las plataformas que se podran apreciar por cada cultura (imagenes unicas)
lista_plataformas =["plataforma_mochica.png",
                    "plataforma_paracas.png",
                    "plataforma_tiahuanaco.png",
                    "plataforma_chavin.png"]

# lista de los escenarios de cada nivel (imagenes unicas), la carga de estas ya se realizo
# anteriormente en este programa
lista_escenarios = [bg_moche,
                    bg_paracas,
                    bg_tiahua,
                    bg_wari]


Boton1 = [300,250]
TamBoton = [200,80]
ColorBoton1 = [plomo, red]
Boton2 = [300,400]
ColorBoton2 = [plomo, blue]
Boton3 = [300, 500]
ColorBoton3 = [plomo, BLACK]

def seleccionarMenu(mx, my):
    if 300 <= mx <=500 and 250 <= my <= 330:
        return 1
    elif 300 <= mx <=500 and 400 <= my <=480:
        return 2
    elif 300 <= mx <=500 and 500 <= my <=580:
        return 3
    else:
        return 0


def msg_boton(msg, color, posx, posy, ancho, alto, tamano_letra="micro"):

    textSur, textRect = text_objetos(msg, color, tamano_letra)
    textRect.center = (posx + (ancho/2), posy + (alto/2))
    screen.blit(textSur, textRect)


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
    elif tamano_letra == "micro":
        textSuperficie = microfont.render(text, True, color)
    return textSuperficie, textSuperficie.get_rect()


def seleccionarModo(mx, my):
    if 483 <= mx <= 659 and 275 <= my <= 537:
        return 1
    elif 164 <= mx <= 262 and 275 <= my <= 537:
        return 2
    else:
        return 0


def seleccionarEscenario(mx, my, escenario):
    id_escenario = 0
    for escena in escenario:
        if 108 <= mx <= 313 and 219 <= my <= 321 and escena == "MOC":
            id_escenario = 1
        elif 478 <= mx <= 695 and 219 <= my <= 324 and escena == "TIA":
            id_escenario = 3
        elif 108 <= mx <= 313 and 397 <= my <= 505 and escena == "PAR":
            id_escenario = 2
        elif 478 <= mx <= 695 and 401 <= my <= 502 and escena == "WAR":
            id_escenario = 4
    return id_escenario


def seleccionarPersonaje(mx, my, persons):
    id_personaje = 0
    for personaje in persons:
        if 211 <= mx <= 292 and 202 <= my <= 344 and personaje == "inmoc":
            id_personaje = 1
        elif 512 <= mx <= 615 and 202 <= my <= 344 and personaje == "intia":
            id_personaje = 3
        elif 211 <= mx <= 292 and 413 <= my <= 546 and personaje == "inpar":
            id_personaje = 2
        elif 512 <= mx <= 615 and 413 <= my <= 546 and personaje == "inwar":
            id_personaje = 4
    return id_personaje


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
                    return event.key
                if event.key == pg.K_x:
                    return event.key
                """elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()"""
        screen.blit(bg_intro, (0, 0))
        message_to_screen("Pausado", ORANGE, -100, "mediano")
        message_to_screen("Presiona C para continuar y X para salir", BLACK, 25, "pequena")
        pg.display.update()
        reloj.tick(60)


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
        archivo = open()
        message_to_screen("Información de la cultura", ORANGE, -100, "mediano")
        message_to_screen("Aqui se mostrara información acerca de la cultura", BLACK, 25, "pequena")
        message_to_screen("Presiona C para continuar", BLACK, 125, "pequena")
        pg.display.update()
        reloj.tick(5)
        
def botones(texto, superficie, estado, pos, tam, ided= None):    
    cursor = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    
    if pos[0] + tam[0] > cursor[0] > tam[0] and pos[1] + tam[1] > cursor[1] > tam[1] and pos[1] + tam[1] < cursor[1] + tam[1]:
        if click[0] == 1:
            if ided == "intro_modo":
                intro_modo(transformarApiToArray(modo_juego))
            elif ided == "intro_ranking":
                intro_ranking()
            elif ided == "salir":
                quit()
        boton = pg.draw.rect(superficie, estado[1], (pos[0], pos[1], tam[0], tam[1]))
    else:
        boton = pg.draw.rect(superficie, estado[0], (pos[0], pos[1], tam[0], tam[1]))

    msg_boton(texto, WHITE, pos[0], pos[1], tam[0], tam[1])    
    return boton

def intro_menu():
    intro = True
    i2, i3, i4, i5 = 0, 0, 0, 0
    while intro:
        mx, my = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                modo = seleccionarMenu(mx, my)
                if modo > 0: return modo
        screen.blit(bg_intro, (0, 0))
        screen.blit(sprites_image_sheet[i2], (300, -30))
        i2 = (i2 + 1) % 2

        botones("nuevo", screen, ColorBoton1, Boton1, TamBoton, ided="intro_modo")
        botones("ranking", screen, ColorBoton2, Boton2, TamBoton, ided="intro_ranking")
        botones("salir", screen, ColorBoton3, Boton3, TamBoton, ided="salir")
        
        pg.display.update()
        reloj.tick(5)


def intro_modo(modo_juego):
    intro = True
    i2, i3, i4, i5 = 0, 0, 0, 0
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

        for mod in modo_juego:
            if mod == "single":
                screen.blit(mode_single, (450, 250))
            if mod == "arcade":
                screen.blit(mode_arcade, (70, 250))
        for mod in modo_juego:
            if 483 <= mx <= 659 and 275 <= my <= 537 and mod == "single":
                screen.blit(sprites_mode_sigle_sheet[i3], (440, 80))
                i3 = (i3 + 1) % 4
                if len(modo_juego) > 1:
                    screen.blit(title_arcade, (70, 80))
                break
            elif 164 <= mx <= 262 and 275 <= my <= 537 and mod == "arcade":
                screen.blit(sprites_mode_arcade_sheet[i4], (70, 80))
                i4 = (i4 + 1) % 4
                if len(modo_juego) > 1:
                    screen.blit(title_single, (440, 80))
                break
            elif 323 <= mx <= 460 and 540 <= my <= 600:
                screen.blit(sprites_mode_ranking_sheet[i5], (260, 400))
                i5 = (i5 + 1) % 4
            else:
                if mod == "single":
                    screen.blit(title_single, (440, 80))
                elif mod == "arcade":
                    screen.blit(title_arcade, (70, 80))


        screen.blit(sprites_image_sheet[i2], (300, -30))
        i2 = (i2 + 1) % 2
        message_to_screen("Escoger un modo de juego", BLACK, -160, "pequena")
        pg.display.update()
        reloj.tick(5)


def intro_ranking():
    intro = True
    nombre = []
    score = []
    response = requests.get(posturl)
    if response.status_code == 200:
        data = response.json()
        print(data)
        for i in range(2):
            nombre.append(data[i]['playerName'])
            score.append(data[i]['acumScore'])
        while intro:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        intro = False
            screen.blit(bg_intro, (0, 0))
            message_to_screen("TOP 10", ORANGE, -160, "mediano")
            message_to_screen("Jugador    Puntaje", BLACK, -60, "pequena")
            for i in range(2):
                message_to_screen(nombre[i] + " : " + str(score[i]), BLACK, -20*-(i+1), "pequena")
            pg.display.update()
            reloj.tick(5)



def intro_escenario(intro, escenarios):
    i2 = 0
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mx, my = pg.mouse.get_pos()
                escenario = seleccionarEscenario(mx, my, escenarios)
                if escenario > 0: return escenario

        screen.blit(bg_intro, (0, 0))
        for escena in escenarios:
            if escena == "MOC":
                screen.blit(escenario_moche, (110, 220))
            elif escena == "PAR":
                screen.blit(escenario_paracas, (110, 400))
            elif escena == "TIA":
                screen.blit(escenario_tiahua, (490, 220))
            elif escena == "WAR":
                screen.blit(escenario_wari, (490, 400))

        screen.blit(sprites_image_sheet[i2], (300, -30))
        i2 = (i2 + 1) % 2
        message_to_screen("Escoger un escenario", WHITE, -160, "pequena")
        pg.display.update()
        reloj.tick(5)


def intro_personaje(intro, persons):
    i2 = 0
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mx, my = pg.mouse.get_pos()
                personaje = seleccionarPersonaje(mx, my, persons)
                if personaje > 0: return personaje

        screen.blit(bg_intro, (0, 0))
        for personaje in persons:
            if personaje == "inmoc":
                screen.blit(perso_moche, (180, 200))
            elif personaje == "inpar":
                screen.blit(perso_paracas, (180, 400))
            elif personaje == "intia":
                screen.blit(perso_tiahua, (490, 200))
            elif personaje == "inwar":
                screen.blit(perso_wari, (490, 400))

        screen.blit(sprites_image_sheet[i2], (300, -30))
        i2 = (i2 + 1) % 2
        message_to_screen("Elegir un personaje", yellow, -160, "pequena")
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
            "Flechas para mover, Espacio para saltar", WHITE, -50, "pequena")
        message_to_screen(
            "Presionar cualquier tecla para empezar", WHITE, 100, "pequena")
        pg.display.update()
        reloj.tick(5)


def into_juego(escenario, persons):
    intro = True
    # modo = intro_modo(intro, modo_juego)
    # ranking = intro_ranking(intro)
    escenario = intro_escenario(intro, escenario)
    personaje = intro_personaje(intro, persons)
    intro_final(intro)
    perso = personaje - 1
    esce = escenario - 1
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
                    propiedades = Propiedades.get_instance()
                    propiedades.puntaje = propiedades.puntaje + score
                    intro = False
        screen.blit(bg_intro, (0, 0))
        message_to_screen("VICTORIA", ORANGE, -100, "mediano")
        message_to_screen("Tu puntaje de este nivel fue: " + str(score), BLACK, -40, "pequena")
        message_to_screen(
            "Presiona C para continuar", BLACK, 25, "pequena")
        pg.display.update()
        reloj.tick(5)


def gameOverFinal():
    intro = True
    form = Form(pg.display.set_mode(SIZE))
    edit_text = EditText(250, 400, 320, 35, 2, 'Anonimo', False, 20)
    form.add_child(edit_text)
    propiedades = Propiedades.get_instance()
    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_position = pg.mouse.get_pos()
                edit_text.collidepoint(mouse_position)
            if event.type == pg.KEYDOWN:
                edit_text.update(event)
                if event.key == pg.K_RETURN:
                    intro = False
        screen.blit(bg_intro, (0, 0))
        message_to_screen("FELICIDADES", ORANGE, -100, "mediano")
        message_to_screen("ACABASTE EL JUEGO", ORANGE, -40, "mediano")
        message_to_screen("Tu puntaje Final fue: " + str(propiedades.puntaje), BLACK, 30, "pequena")
        message_to_screen(
            "Presiona enter para guardar y salir al menú", ORANGE, 200, "pequena")
        form.draw()
        pg.display.update()
        reloj.tick(5)
    payload = {"playerName": edit_text.value, "acumScore": str(propiedades.puntaje)}
    # data = json.dumps({'playerName':'Bot', 'acumScore':str(score)})
    r = requests.post(posturl, data=payload)


def transformarApiToArray(str):
    str1 = str.replace("[", "")
    str2 = str1.replace("]", "")
    str3 = str2.replace("'", "")
    str4 = str3.replace(" ", "")
    str5 = str4.split(",")
    return str5


class Game:
    def __init__(self, escena, perso):
        # initialize game window, etc
        self.dir = path.dirname("")
        self.platforms = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.carteles = pg.sprite.Group()
        self.serpientes = pg.sprite.Group()
        self.checkpoints = pg.sprite.Group()
        self.rocones = pg.sprite.Group()
        self.soldados = pg.sprite.Group()
        self.bosses = pg.sprite.Group()
        self.lanza = pg.sprite.Group()
        self.score = 0
        self.escenario = escena
        self.show_cartel = True
        self.posCheckpoint = (0, 0)
        self.confirmCheckpoint = False
        self.llama_pibot = 0
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.img_dir = path.join(self.dir, "assets/images/personajes")
        self.sprites = Spritesheet(path.join(self.img_dir, lista_perso[perso]))
        self.img_dir_enemigos = path.join(self.dir, "assets/images/enemigos")
        self.sprites_serpientes = Spritesheet(path.join(self.img_dir_enemigos, "serpiente.png"))
        self.sprites_soldado = Spritesheet(path.join(self.img_dir_enemigos, "espanol_normal.png"))
        self.sprites_boss = Spritesheet(path.join(self.img_dir_enemigos, "espanol_boss.png"))
        self.sprites_lanza = Spritesheet(path.join(img_objetos_folder, "lanza.png"))
        self.level = LEVELS[escena]

    def new(self):
        # Se incia un nuevo juego
        if self.posCheckpoint == (0, 0):
            self.score = 0

        # Se construye el escenario, las plataformas, objetos y personajes
        # según el mapa que fue pasado
        x = y = 0
        for row in self.level:
            for col in row:
                self.construir(x, y, col)
                x += 32
            y += 72
            x = 0

        # Camara que seguira el personaje durante el juego
        self.camera= Camera(0, 0)
        self.run()

    def run(self):
        # Loop del juego, aqui se realizaran todos los updates de los eventos que ocurren durante el juego
        # además de dibujar a los personajes, este Loop terminara si la variable self.playing es setada
        # como False por algún evento ocurrido
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
    #Lanzar proyectil del boss
    def proyectil(self):
        out=False
        way=True
        if self.player.pos.x < self.boss.pos.x:
            posx=self.boss.pos.x-3
        else:
            posx=self.boss.pos.x+3
            way=False
              
        posy=self.boss.pos.y*2/3
        self.screen.blit(self.sprites_lanza, (posx, posy))
        
        
    def update(self):
        # Esta es la sección donde se defininen todos los accionares dentro del juego, por ejemplo
        # si el personaje choca contra una roca, este se detiene y no puede seguir avanzando

        self.all_sprites.update()
        self.camera.update(self.player)

        # Aqui se determina si es que el personaje salta encima de una plataforma,
        # este queda por encima de ella
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        # Se determina el accionar cuando se salta encima de la serpiente, en este caso
        # la serpiente morira
        hits_saltar_serpiente = pg.sprite.spritecollide(self.player, self.serpientes, False)
        if self.player.vel.y > 0:
            if hits_saltar_serpiente:
                if self.player.rect.bottom >= hits_saltar_serpiente[0].rect.top:
                    pg.mixer.Sound.play(pg.mixer.Sound("assets/audio/matarObstaculo.wav"))
                    hits_saltar_serpiente[0].kill()
                    self.score += 20

        # Se determina el accionar cada vez que la serpiente choque de costado con el inca
        # cada golpe disminuira cierta cantidad de vida al personaje, cuando la vida llegue a
        # 0, el personaje morira y el juego terminara
        hits_serpiente = pg.sprite.spritecollide(self.player, self.serpientes, False)
        if hits_serpiente:
            if self.player.vel.x >= 0 \
                    and self.player.rect.right >= hits_serpiente[0].rect.left:
                self.player.vel.x = -15
                self.player.vel.y = -12
                vida = self.player.disminuirVida(SERPIENTE_FUERZA)
                if vida <= 0:
                    self.player.vida = 0
                    self.kill_all()
                    self.playing = False
                    
        # Accion cada que una lanza golpea al personaje
        hits_lanza= pg.sprite.spritecollide(self.player, self.lanza, False)
        if hits_lanza:
            if self.player.vel.x >= 0 \
                    and self.player.rect.right >= hits_lanza[0].rect.left:
                self.player.vel.x = -15
                self.player.vel.y = -12
                vida = self.player.disminuirVida(LANZA_DMG)
                hits_lanza[0].kill()
                if vida <= 0:
                    self.player.vida = 0
                    self.kill_all()
                    self.playing = False
                    
        # Se determina que las serpientes siempre se posicionaran encima de las plataformas
        for serpiente in self.serpientes:
            if serpiente.vel.y > 0:
                hits = pg.sprite.spritecollide(serpiente, self.platforms, False)
                if hits:
                    serpiente.pos.y = hits[0].rect.top
                    serpiente.vel.y = 0

        # Si la serpinete llega a impactar contra una roca, la dirección a la cual se dirige
        # cambia, y esta sale con una acceleracion determinada
        for serpiente in self.serpientes:
            hit_serpiente_roca = pg.sprite.spritecollide(serpiente, self.rocones, False)
            if hit_serpiente_roca:
                if serpiente.vel.x > 0 and serpiente.rect.right >= hit_serpiente_roca[0].rect.left:
                    serpiente.pos.x += abs(serpiente.vel.x)
                    serpiente.vel.x = -3
                elif serpiente.vel.x < 0 and serpiente.rect.left <= hit_serpiente_roca[0].rect.right:
                    serpiente.pos.x -= abs(serpiente.vel.x)
                    serpiente.vel.x = 3
                serpiente.cambiarMovimiento()

        # Se determina que los soldados se mantendran encima de las plataformas
        for soldado in self.soldados:
            if soldado.vel.y > 0:
                hits = pg.sprite.spritecollide(soldado, self.platforms, False)
                if hits:
                    soldado.pos.y = hits[0].rect.top
                    soldado.vel.y = 0

        # Al igual que con las serpientes, los soldados cambiaran la dirección si chocan contra una roca
        for soldado in self.soldados:
            hit_soldado_roca = pg.sprite.spritecollide(soldado, self.rocones, False)
            if hit_soldado_roca:
                if soldado.vel.x > 0 and soldado.rect.right >= hit_soldado_roca[0].rect.left:
                    soldado.pos.x += abs(soldado.vel.x)
                    soldado.vel.x = -5
                elif soldado.vel.x < 0 and soldado.rect.left <= hit_soldado_roca[0].rect.right:
                    soldado.pos.x -= abs(soldado.vel.x)
                    soldado.vel.x = 5
                soldado.cambiarMovimiento()

        # Se determina que cuando el personaje salte sobre algun soldado, este soldado morira
        # y además seran sumados 20 puntos al score del jugador
        hits_saltar_soldado = pg.sprite.spritecollide(self.player, self.soldados, False)
        if self.player.vel.y > 0:
            if hits_saltar_soldado:
                if self.player.rect.bottom >= hits_saltar_soldado[0].rect.top:
                    pg.mixer.Sound.play(pg.mixer.Sound("assets/audio/matarObstaculo.wav"))
                    hits_saltar_soldado[0].kill()
                    self.score += 20

        # Se determina que cuando
        hits_soldado = pg.sprite.spritecollide(self.player, self.soldados, False)
        if hits_soldado:
            if self.player.vel.x >= 0 \
                    and self.player.rect.right >= hits_soldado[0].rect.left:
                self.player.vel.x = -15
                self.player.vel.y = -12
                vida = self.player.disminuirVida(SOLDADO_FUERZA)
                if vida <= 0:
                    self.player.vida = 0
                    self.kill_all()
                    self.playing = False

        if self.boss.vel.y > 0:
            hits = pg.sprite.spritecollide(self.boss, self.platforms, False)
            if hits:
                self.boss.pos.y = hits[0].rect.top
                self.boss.vel.y = 0

        hit_boss_roca = pg.sprite.spritecollide(self.boss, self.rocones, False)
        if hit_boss_roca:
            if self.boss.vel.x > 0 and self.boss.rect.right >= hit_boss_roca[0].rect.left:
                self.boss.pos.x += abs(self.boss.vel.x)
                self.boss.vel.x = -5
            elif self.boss.vel.x < 0 and self.boss.rect.left <= hit_boss_roca[0].rect.right:
                self.boss.pos.x -= abs(self.boss.vel.x)
                self.boss.vel.x = 5
            self.boss.cambiarMovimiento()

        hits_saltar_boss = pg.sprite.spritecollide(self.player, self.bosses, False)
        if self.player.vel.y > 0:
            if hits_saltar_boss:
                if self.player.rect.bottom >= hits_saltar_boss[0].rect.top:
                    pg.mixer.Sound.play(pg.mixer.Sound("assets/audio/matarObstaculo.wav"))
                    self.player.vel.y = -12
                    vida_boss = self.boss.disminuirVida()
                    print(vida_boss)
                    if vida_boss <= 0:
                        hits_saltar_boss[0].kill()
                        self.score += 40
                        gameOver(self.score)
                        self.playing = False
                        self.running = False

        hits_boss = pg.sprite.spritecollide(self.player, self.bosses, False)
        if hits_boss:
            if self.player.vel.x >= 0 \
                    and self.player.rect.right >= hits_boss[0].rect.left \
                    and self.player.rect.bottom >= hits_boss[0].rect.bottom:
                self.player.vel.x = -15
                self.player.vel.y = -12
                vida = self.player.disminuirVida(BOSS_FUERZA)
                if vida <= 0:
                    self.player.vida = 0
                    self.kill_all()
                    self.playing = False

        # Cuando choque de costado con el personaje pasara esto
        hit_roca = pg.sprite.spritecollide(self.player, self.rocones, False)
        if hit_roca:
            if self.player.vel.x > 0:
                if self.player.rect.right >= hit_roca[0].rect.left:
                    #print("CHOCA DERECHA")
                    self.player.pos.x -= abs(self.player.vel.x)
            elif self.player.vel.x < 0:
                if self.player.rect.left <= hit_roca[0].rect.right:
                    #print("CHOCA IZQUIERDA")
                    self.player.pos.x += abs(self.player.vel.x)

        hits_coin = pg.sprite.spritecollide(self.player, self.coins, False)
        if hits_coin:
            if self.player.rect.right >= hits_coin[0].rect.center[0]:
                hits_coin[0].kill()
                pg.mixer.Sound.play(pg.mixer.Sound("assets/audio/coin_sound.wav"))
                self.score += 10

        hits_cartel = pg.sprite.spritecollide(self.player, self.carteles, False)
        if hits_cartel:
            if self.player.rect.center[0] >= hits_cartel[0].rect.center[0] and self.show_cartel:
                pantalla_info()
                self.show_cartel = False

        hits_checkpoint = pg.sprite.spritecollide(self.player, self.checkpoints, False)
        if hits_checkpoint:
            self.posCheckpoint = (self.player.rect.x, self.player.rect.y)
            self.confirmCheckpoint = True

        # If player reaches top 1/4 of screen
        if self.player.rect.left <= 0:
            self.player.pos.x += abs(self.player.vel.x)


        if self.player.rect.top > HEIGHT:
            self.kill_all()
            self.show_cartel = True
            self.playing = False

        for serp in self.serpientes:
            if serp.rect.top > HEIGHT:
                serp.kill()

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                if event.key == pg.K_p:
                    e = pausa()
                    if e == pg.K_x:
                        self.playing = False
                        self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.blit(lista_escenarios[self.escenario], (0, 0))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.draw_text(str(self.score), 22, BLACK, WIDTH / 2, 15)
        self.draw_text("Corazones: " + str(self.player.vida), 22, BLACK, 200, 15)
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(SKY_BLUE)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Flechas para mover, Espacio para Saltar", 22, WHITE, WIDTH / 2,
                       HEIGHT / 2)
        self.draw_text("Presione cualquier tecla para empezar", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

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
        font = pg.font.SysFont("comicsansms", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def construir(self, x, y, col):
        if col == "P":
            p = Platform( lista_plataformas[self.escenario], x, y, 50, 50)
            self.platforms.add(p)
            self.all_sprites.add(p)
        elif col == "F":
            if self.posCheckpoint == (0, 0):
                self.player = Player(self, x, y)
                self.all_sprites.add(self.player)
            else:
                self.player = Player(self, self.posCheckpoint[0], self.posCheckpoint[1])
                self.all_sprites.add(self.player)
        elif col == "L":
            l = Checkpoint(x, y)
            self.checkpoints.add(l)
            self.all_sprites.add(l)
        elif col == "S":
            s = Serpiente(self, x, y)
            self.serpientes.add(s)
            self.all_sprites.add(s)
        elif col == "E":
            e = Soldado(self, x, y)
            self.soldados.add(e)
            self.all_sprites.add(e)
        elif col == "R":
            r = Rocon(x, y)
            self.rocones.add(r)
            self.all_sprites.add(r)
        elif col == "M":
            m = Moneda(x, y)
            self.coins.add(m)
            self.all_sprites.add(m)
        elif col == "C":
            c = Cartel(x, y)
            self.carteles.add(c)
            self.all_sprites.add(c)
        elif col == "B":
            self.boss = Boss(self, x, y)
            self.bosses.add(self.boss)
            self.all_sprites.add(self.boss)

    def kill_all(self):
        for plat in self.platforms:
            plat.kill()
        for coin in self.coins:
            coin.kill()
        for cartel in self.carteles:
            cartel.kill()
        for serp in self.serpientes:
            serp.kill()
        for llama in self.checkpoints:
            llama.kill()
        for roca in self.rocones:
            roca.kill()
        for espanol in self.soldados:
            espanol.kill()
        self.boss.kill()
        self.player.kill()


def mainArcade():
    pg.mixer.music.load("assets/audio/bg_opcion2.wav")
    pg.mixer.music.set_volume(0.5)
    pg.mixer.music.play(-1)
    g = Game(0, 0)
    g1 = Game(1, 0)
    g2 = Game(2, 0)
    g3 = Game(3, 0)

    while g.running:
        g.new()
    while g1.running:
        g1.new()
    while g2.running:
        g2.new()
    while g3.running:
        g3.new()
    gameOverFinal()
    propiedades = Propiedades.get_instance()
    print(str(propiedades.puntaje))
    pg.mixer.quit()


def mainSingle(escena, perso):
    g = Game(escena, perso)
    # Carga de la musica que sonara de fondo cuando comienze el juego
    pg.mixer.music.load("assets/audio/bg_opcion2.wav")
    pg.mixer.music.set_volume(0.5)
    pg.mixer.music.play(-1)
    while g.running:
        g.new()
    pg.mixer.quit()

if __name__ == "__main__":
    url = "http://runinkarun.herokuapp.com/api"
    response = requests.get(url)

    if response.status_code == 200:
        results = response.json()[len(response.json())-1]
        print(results)
        escenario = results['escenario']
        personajes = results['personaje']
        modo_juego = results['modo_juego']
        dificultad = results['dificultad']
        intro_background = results['intro_background']
        speed_player = results['speed_player']
        life = results['life']
        #game_time = results['game_time']
        musica = results['musica']

    while True:
        propiedades = Propiedades.get_instance()
        propiedades.propiedades_personaje(life, speed_player)
        num = intro_menu()
        print(str(num))
        if num == 1:
            modo = intro_modo(transformarApiToArray(modo_juego))
            print(str(modo))
            if modo == 1:
                ese, perso = into_juego(transformarApiToArray(escenario),
                                        transformarApiToArray(personajes))
                mainSingle(ese, perso)
            elif modo == 2:
                mainArcade()
        elif num == 2:
            intro_ranking()
