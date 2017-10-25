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

# Starting platforms
PLATFORM_GROUND = 0, HEIGHT - 40, WIDTH, 40
COINS_LIST = [(340, 100, 150, 150),
              (400, 0, 150, 150)]
PLATFORM_LIST = [(WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (445, 100, 50, 20)]

CARTEL_LIST = 600, HEIGHT - 80, 100, 40

LLAMA_LIST = 400, HEIGHT - 120, 100, 90

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20
