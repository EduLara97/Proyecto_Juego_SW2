# define colors
WHITE = 255, 255, 255
SKY_BLUE = 7, 242, 212
ORANGE = 239, 127, 26
BLACK = 0, 0, 0
ORANGE_LIGTH = 255, 183, 87
blue = (0, 0, 255)
plomo = (232, 224, 224)
red = 255, 0, 0


# game options/settings
TITLE = "RUN INKA RUN GAME"
SIZE = 800, 600
WIDTH = 800
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
SPRITESHEET = "inca_mochica.png"

LEVELS = [[
        "                                                                                                                             ",
        "                                                                                                                             ",
        "                    MM        PP                   MM                                                                        ",
        "                   PPPP                  L       PPPPPP                     MMMMMM        MMMMMM   S                         ",
        "                                      PPPPPP                             PPPPPPPPPPPPPPPPPPPPPPPPPPPP                        ",
        "                P                        MM                                             MMM        S      P                  ",
        "            P                           PPPP                                   PPPPPPPPPPPPPPPPPPPPPP                        ",
        "F   R    S  C  E R                                                                                 S         R            B R",
        "PPPPPPPPPPPPPPPPPPP          PPPPPPPPPPPPPPPPPPPPPPPPPP       PPP     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP        PPPPPPPPPPPPPPPP"],
        [
        "                                                                                                                                  ",
        "                                                                                                                                  ",
        "                                                                                           PP                                     ",
        "                                                       L                             PP                                           ",
        "                                       C               P                       PP                                                 ",
        "                             M         PP          P                       P                                                      ",
        "        M       M        M   P     P          P                      PP                                         P                 ",
        "F       M       M        M           R  SR        RM    EMR                R S R     R  E R       MMMMMMMMM          R         B R",
        "PPPP   PPP     PP       PP           PPPPP        PPPPPPPPP    PPPP     PPPPPPPP     PPPPPP      PPPPPPPPPP          PPPPPPPPPPPPP"],
        [
        "                                                                                                                                                     ",
        "                                                                          SSSMM         L                                                            ",
        "                                                                         PPPPPP        PPPM                                   P                      ",
        "                                                                                                                         P                           ",
        "                  MMM                                                 M                                              P                               ",
        "                                                                     PPP                    M        MM   MM    P                                    ",
        "             M   PMPMP                                                                                                                               ",
        "  F                S     R C S    R  S     R   ES    RMCMMM               R E   R              S S                SR               R          B     R",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP   PPPPPPPPPPPPPPPPPPP      PPPPPPPPPPPPPPPPPPPPPPPPPPPP               PPPPPPPPPPPPPPPPPP"],
        [
        "                                                                                                                                   ",
        "                                                                                MMM                                                ",
        "                                                                           MMM                                                     ",
        "                                                                           PPP                                                     ",
        "F      M                                  MMMM                                                        MMMMMMMMM                    ",
        "PP    PP   PPP                  MM            C                          M                           PPPPPPPPPPPP                  ",
        "                               PPP       P     P                        PP                                                         ",
        "R SSS      R        MMMMMM      SR      PR SS  RP                    L              R E     R  MMMMMMMMMM S R      R            B R",
        "PPPPPPPPPPPP       PPPPPPPPPPPPPPP     P PPPPPPP PPPPPP   P  MM  P  PPPPP          PPPPPPPPPPPPPPPPPPPPPPPPPP      PPPPPPPPPPPPPPPP"],
        [
        "                                                      MMMMMM                                                        ",
        "                                                     PPPPPPPP                                       MMM             ",
        "                                                                                         M        PPPPP             ",
        "F                           M     M   M         MMMM  RS      R                         M MM     P                  ",
        "PP                      M   M     M    M       PPPPPPPPPPPPPPPP              M     PPPP        P                    ",
        "PPP                     M   P     P    P    P                           L    P                                      ",
        "PPPP                    P                                               PP                                          ",
        "MMMMM     MMMM R S   R S  S  R    E    R                        MMM M                    C              R         BR",
        "PPPPP     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP                       PPPPPP             PPPPPPPPPPPPPP       PPPPPPPPPPPP"]]

# Player properties

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 15
VIDA_PERSONAJE = 5


class Propiedades:
        instancia = None


        @classmethod
        def get_instance(cls):
                if cls.instancia == None:
                        cls.instancia = Propiedades()
                return cls.instancia


        def __init__(self):
                self.player_acc = 1
                self.player_friction = -0.12
                self.player_grav = 0.8
                self.player_jump = 15
                self.vida_personaje = 5
                self.puntaje = 0

        def propiedades_personaje(self, vida, velocidad):
                self.vida_personaje = vida
                if velocidad == 1:
                        self.player_acc = 0.5
                elif velocidad == 2:
                        self.player_acc = 0.55
                elif velocidad == 3:
                        self.player_acc == 0.6
                elif velocidad == 4:
                        self.player_acc == 0.65
                elif velocidad == 5:
                        self.player_acc == 0.7
# Coins properties
COINS_PROP = (30, 30)

# Cartel properties
CARTEL_PROP = (100, 80)

# Enemies properties
SERPIENTE_PROP = (40, 40)
SERPIENTE_FUERZA = 1
SERP_ACC = 0.1
SOLDADO_PROP = (60, 80)
SOLDADO_FUERZA = 2
BOSS_FUERZA = 3
BOOS_VIDA = 5
LANZA_DMG = 2
