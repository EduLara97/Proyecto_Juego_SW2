import pygame as pg
from pygame import *
from utils.States import AnimatedState, StaticState
from GeneralInformation import *

vec = pg.math.Vector2


class Spritesheet:
    # utility class for loading and parsing spritesheets
    def __init__(self, filename):
        self.sspritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        # grab an image out of a larger spritesheet
        image = pg.Surface((width, height))
        image.blit(self.sspritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (60, 80))
        return image


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(20, 0)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def load_images(self):
        self.standing_frames =[self.game.sprites.get_image(0, 0, 200, 200)]
        for frame in self.standing_frames:
            frame.set_colorkey(BLACK)
        self.walk_frames_r = [self.game.sprites.get_image(200, 0, 200, 200),
                              self.game.sprites.get_image(400, 0, 200, 200),
                              self.game.sprites.get_image(600, 0, 200, 200)]

        """self.game.sprites.get_image(200, 0, 200, 200),
                              self.game.sprites.get_image(200, 200, 200, 200),
                              self.game.sprites.get_image(200, 400, 200, 200),
                              self.game.sprites.get_image(200, 600, 200, 200)"""
        self.walk_frames_l = []

        for frame in self.walk_frames_r:
            frame.set_colorkey(BLACK)
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))



    def jump(self):
        # jump only if standing on a platform
        pg.mixer.Sound.play(pg.mixer.Sound("assets/audio/jump.wav"))
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP

    def update(self):
        self.animate()
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # APPLY FRICTION
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

        # show walk animation
        if self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % \
                                     len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]

                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        # show idle animation
        if not self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                bottom = self.rect.bottom
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/images/terrenos/plataforma1.png").convert()
        self.image = pg.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Moneda(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/images/objetos/moneda.gif").convert()
        self.image = pg.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Terreno(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/images/terrenos/terreno_1.png").convert()
        self.image = pg.transform.scale(self.image, (1000, self.image.get_height()))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Cartel(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/images/objetos/cartel1.jpg").convert()
        self.image = pg.transform.scale(self.image, (w, h))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Checkpoint(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/images/objetos/llama_1.gif").convert()
        self.image = pg.transform.scale(self.image, (w, h))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# class GameEntity(pygame.sprite.Sprite):
#     def __init__(self, display):
#         super(GameEntity, self).__init__()
#
#         self.display = display
#         self.states_dict = {}
#         self.current_state = None
#         self.dx = 0
#         self.dy = 0
#         self.image = None
#         self.jumping = False
#
#     def set_current_state(self, key):
#         self.current_state = self.states_dict[key]
#
#     def impulse(self, dx, dy):
#         self.dx = dx
#         self.dy = dy
#
#     def update(self, dt):
#         """raise: Sirve para levantar errores"""
#         raise NotImplementedError("The update method must be called in any child class")
#
#
# class Character(GameEntity):
#     def __init__(self, display, px, py, perso):
#         super(Character, self).__init__(display)
#         self.cho = True
#         self.speed = 3.5
#         self.walking_images = pygame.image.load(perso)
#         self.walking_images = pygame.transform.scale(self.walking_images, (300, 250))
#         self.number_of_sprites = 4
#
#         self.walking_right_state = AnimatedState(self.walking_images.subsurface(0, 0,
#                                                                                 self.walking_images.get_width(),
#                                                                                 self.walking_images.get_height() / 2),
#                                                  self.number_of_sprites, 400, "walking_right")
#
#         self.walking_left_state = AnimatedState(self.walking_images.subsurface(0, self.walking_images.get_height() / 2,
#                                                                                self.walking_images.get_width(),
#                                                                                self.walking_images.get_height() / 2),
#                                                 self.number_of_sprites, 400, "walking_left")
#
#         self.resting_right_state = StaticState(self.walking_images.
#                                                subsurface(0, 0,
#                                                           self.walking_images.get_width() / self.number_of_sprites,
#                                                           self.walking_images.get_height() / 2), "resting_right")
#
#         self.resting_left_state = StaticState(self.walking_images.
#                                               subsurface(self.walking_images.get_width() * 3 / 4,
#                                                          self.walking_images.get_height() / 2,
#                                                          self.walking_images.get_width() / self.number_of_sprites,
#                                                          self.walking_images.get_height() / 2), "resting_left")
#
#         self.states_dict[self.walking_right_state.get_name()] = self.walking_right_state
#         self.states_dict[self.walking_left_state.get_name()] = self.walking_left_state
#         self.states_dict[self.resting_right_state.get_name()] = self.resting_right_state
#         self.states_dict[self.resting_left_state.get_name()] = self.resting_left_state
#
#         self.set_current_state(self.resting_right_state.get_name())
#         self.image = self.current_state.get_sprite()
#         self.rect = self.image.get_rect()
#         self.rect.x = px
#         self.rect.y = py
#
#     def calculate_gravity(self):
#         self.dy = self.dy + 0.35
#
#     def jump(self, jump_force):
#         self.impulse(self.dx, -jump_force)
#
#     def key_down(self, key):
#         if key == pygame.K_UP:
#             if not self.jumping:
#                 pygame.mixer.Sound.play(pygame.mixer.Sound("assets/audio/jump.wav"))
#                 self.jump(10)
#                 self.jumping = True
#         if key == pygame.K_DOWN:
#             pass
#         if self.cho:
#             if key == pygame.K_RIGHT:
#                 self.dx = self.speed
#                 self.set_current_state(self.walking_right_state.get_name())
#         else:
#             print("no paso")
#         if key == pygame.K_LEFT:
#             self.dx = -self.speed
#             self.set_current_state(self.walking_left_state.get_name())
#
#     def key_up(self, key):
#         if key == pygame.K_UP:
#             pass
#         if key == pygame.K_DOWN:
#             pass
#         if key == pygame.K_RIGHT:
#             if self.dx > 0:
#                 self.dx = 0
#                 self.set_current_state(self.resting_right_state.get_name())
#         if key == pygame.K_LEFT:
#             if self.dx < 0:
#                 self.dx = 0
#                 self.set_current_state(self.resting_left_state.get_name())
#
#     def update(self, dt, platforms):
#         self.calculate_gravity()
#         self.rect.x = self.rect.x + self.dx
#         self.rect.y = self.rect.y + self.dy
#         """if self.rect.y + self.rect.height > self.display.get_height() - 62:
#             self.rect.y = self.display.get_height() - 62 - self.rect.height
#             self.jumping = False
#             self.dy = 0"""
#         self.current_state.update(dt)
#         self.image = self.current_state.get_sprite()
#         self.collide(self.dx, self.dy, platforms)
#
#     def collide(self, xvel, yvel, platforms):
#         for p in platforms:
#             if pygame.sprite.collide_rect(self, p):
#                 if xvel > 0:
#                     self.rect.right = p.rect.left
#                     print("collide right")
#                 if xvel < 0:
#                     self.rect.left = p.rect.right
#                     print("collide left")
#                 if yvel > 0:
#                     print(str(yvel))
#                     self.rect.bottom = p.rect.top
#                     #self.onGround = True
#                     print("collide bottom")
#                     self.dy = 0
#                 if yvel < 0:
#                     self.rect.top = p.rect.bottom
#                     print("collide top")
#                 """if xvel > 0 & self.rect.right == p.rect.right:
#                     self.rect.right = p.rect.right
#                 elif xvel > 0 & self.rect.right == p.rect.left:
#                     self.rect.right = p.rect.left
#                 if xvel < 0 & self.rect.left == p.rect.right:
#                     self.rect.left = p.rect.left
#                 elif xvel < 0 & self.rect.left == p.rect.right:
#                     self.rect.left = p.rect.rigt
#                 if yvel > 0:
#                     self.rect.bottom = p.rect.top
#                 if yvel < 0:
#                     self.rect.top = p.rect.bottom"""
#
#
# class Entity(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#
#
# class Platform(Entity):
#     def __init__(self, x, y):
#         Entity.__init__(self)
#         self.image = Surface((32, 32))
#         self.image.convert()
#         self.image.fill(Color("#DDDDDD"))
#         self.rect = Rect(x, y, 32, 32)
#
#     def update(self):
#         pass
#
#
# class ExitBlock(Platform):
#     def __init__(self, x, y):
#         Platform.__init__(self, x, y)
#         self.image.fill(Color("#0033FF"))
#
#
# class Roca(Entity):
#     def __init__(self, x, y):
#         Entity.__init__(self)
#         self.image = pygame.image.load("assets/images/obstaculos/rocon.png").convert()
#         self.image = pygame.transform.scale(self.image, (50, 200))
#         self.rect = Rect(x, y, self.image.get_width(), self.image.get_height())
#
#     """def rock_draw(self, surface):
#         surface.blit(self.image, (440, 80))
#
#     def checkCollision(self, spriteGroup):
#         if  pygame.sprite.spritecollide(self, spriteGroup, False):
#             print("CHOCAROOOOOOOOOONNNNNNNNNNNNNN")"""
#
