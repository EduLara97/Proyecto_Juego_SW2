# define colors
WHITE = 255, 255, 255
SKY_BLUE = 7, 242, 212
ORANGE = 239, 127, 26
BLACK = 0, 0, 0
ORANGE_LIGTH = 255, 183, 87

# game options/settings
TITLE = "RUN INKA RUN GAME"
SIZE = 800, 600
WIDTH = 800
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
SPRITESHEET = "inca_mochica.png"

LEVEL_PRUEBA=[
        "                                                                                                                             ",
        "                                                                                                                             ",
        "                    MM        PP                   MM                                                                        ",
        "                   PPPP                  L       PPPPPP                     MMMMMM        MMMMMM                             ",
        "                                      PPPPPP                             PPPPPPPPPPPPPPPPPPPPPPPPPPPP                        ",
        "                P                        MM                                             MMM                                  ",
        "            P                           PPPP                                   PPPPPPPPPPPPPPPPPPPPPP                        ",
        " F  R    S  C  R                                                                                                             ",
        "PPPPPPPPPPPPPPPPPPP          PPPPPPPPPPPPPPPPPPPPPPPPPP        P      PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP        PPPPPPPPPPPPPPPP"]

# Starting platforms
PLATFORM_GROUND = [(0, HEIGHT - 40, 2000, 80),
                   (2150, HEIGHT - 40, 2000, 80)]
COINS_LIST = [(880, 160, 30, 30),
              (950, 60, 30, 30),
              (920, 160, 30, 30),
              (990, 60, 30, 30),
              (1380, 160, 30, 30),
              (1450, 60, 30, 30),
              (1410, 160, 30, 30),
              (1490, 60, 30, 30),
              (1810, 160, 30, 30),
              (1950, 60, 30, 30)]
PLATFORM_LIST = [(WIDTH / 2 - 50 + 500, HEIGHT * 3 / 4, 100, 20),
                 (625, 350, 100, 20),
                 (850, 200, 100, 20),
                 (945, 100, 50, 20),
                 (1125, HEIGHT - 350, 100, 20),
                 (1350, 200, 100, 20),
                 (1445, 100, 50, 20)]

CARTEL_LIST = 600, HEIGHT - 80, 100, 40

LLAMA_LIST = 3400, HEIGHT - 120, 100, 90

# Player properties
PLAYER_ACC = 0.5
SERP_ACC = 0.2
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 15
VIDA_PERSONAJE = 5

# Coins properties
COINS_PROP = (30, 30)

# Cartel properties
CARTEL_PROP = (100, 80)

# Enemies properties
SERPIENTE_PROP = (40, 40)
SERPIENTE_FUERZA = 1
