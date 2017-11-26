from random import randrange

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
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.propiedades = Propiedades.get_instance()
        self.vida = self.propiedades.vida_personaje
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def load_images(self):
        self.standing_frames = [self.game.sprites.get_image(0, 0, 200, 200)]
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
            self.acc.x = - self.propiedades.player_acc
        if keys[pg.K_RIGHT]:
            self.acc.x = self.propiedades.player_acc

        # APPLY FRICTION
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
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

    def disminuirVida(self, disminucion):
        self.vida -= disminucion
        return self.vida


class Serpiente(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.movimiento = True

    def load_images(self):
        self.standing_frames = [pg.transform.scale(self.game.sprites_serpientes.get_image(0, 0, 165, 90.5), SERPIENTE_PROP)]
        for frame in self.standing_frames:
            frame.set_colorkey(WHITE)
        self.walk_frames_r = [pg.transform.scale(self.game.sprites_serpientes.get_image(165, 0, 165, 90.5), SERPIENTE_PROP),
                              pg.transform.scale(self.game.sprites_serpientes.get_image(330, 0, 165, 90.5), SERPIENTE_PROP),
                              pg.transform.scale(self.game.sprites_serpientes.get_image(495, 0, 165, 90.5), SERPIENTE_PROP)]

        self.walk_frames_l = []

        for frame in self.walk_frames_r:
            frame.set_colorkey(WHITE)
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))

    def cambiarMovimiento(self):
        self.movimiento = not self.movimiento
        # return self.movimiento

    def update(self):
        self.animate()
        self.acc = vec(0, PLAYER_GRAV)
        if self.movimiento:
            self.acc.x = -SERP_ACC
        else:
            self.acc.x = SERP_ACC
        # APPLY FRICTION
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
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


class Soldado(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.movimiento = True

    def load_images(self):
        self.standing_frames = [pg.transform.scale(self.game.sprites_soldado.get_image(0, 0, 200, 200), SOLDADO_PROP)]
        for frame in self.standing_frames:
            frame.set_colorkey(BLACK)
        self.walk_frames_r = [pg.transform.scale(self.game.sprites_soldado.get_image(200, 0, 200, 200), SOLDADO_PROP),
                              pg.transform.scale(self.game.sprites_soldado.get_image(400, 0, 200, 200), SOLDADO_PROP),
                              pg.transform.scale(self.game.sprites_soldado.get_image(600, 0, 200, 200), SOLDADO_PROP)]

        self.walk_frames_l = []

        for frame in self.walk_frames_r:
            frame.set_colorkey(BLACK)
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))

    def update(self):
        self.animate()
        self.acc = vec(0, PLAYER_GRAV)
        if self.movimiento:
            self.acc.x = -SERP_ACC
        else:
            self.acc.x = SERP_ACC
        # APPLY FRICTION
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

    def cambiarMovimiento(self):
        self.movimiento = not self.movimiento

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


class Boss(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.movimiento = True

    def load_images(self):
        self.standing_frames = [pg.transform.scale(self.game.sprites_boss.get_image(0, 0, 200, 200), SOLDADO_PROP)]
        for frame in self.standing_frames:
            frame.set_colorkey(BLACK)
        self.walk_frames_r = [pg.transform.scale(self.game.sprites_boss.get_image(200, 0, 200, 200), SOLDADO_PROP),
                              pg.transform.scale(self.game.sprites_boss.get_image(400, 0, 200, 200), SOLDADO_PROP),
                              pg.transform.scale(self.game.sprites_boss.get_image(600, 0, 200, 200), SOLDADO_PROP)]

        self.walk_frames_l = []

        for frame in self.walk_frames_r:
            frame.set_colorkey(BLACK)
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))

    def update(self):
        self.animate()
        self.acc = vec(0, PLAYER_GRAV)
        if self.movimiento:
            self.acc.x = -SERP_ACC
        else:
            self.acc.x = SERP_ACC
        # APPLY FRICTION
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

    def cambiarMovimiento(self):
        self.movimiento = not self.movimiento

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
    def __init__(self, esce, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/images/terrenos/" + esce).convert()
        self.image = pg.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Moneda(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/images/objetos/moneda.gif").convert()
        self.image = pg.transform.scale(self.image, COINS_PROP)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Terreno(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/images/terrenos/terreno.png").convert()
        self.image = pg.transform.scale(self.image, (w, self.image.get_height()+h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Cartel(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/images/objetos/cartel1.png").convert()
        self.image = pg.transform.scale(self.image, CARTEL_PROP)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Checkpoint(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/images/objetos/llama_1.gif").convert()
        self.image = pg.transform.scale(self.image, (100, 80))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    """def update(self):
        self.animate()
    
    def animate(self):
        now = pg.time.get_ticks()
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
                self.rect.bottom = bottom"""


class Rocon(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("assets/images/obstaculos/rocon.png").convert()
        self.image = pg.transform.scale(self.image, (50, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + 490

        # limit scrolling to map size
        x = min(0, x) # left
        y = min(0, y) # right
        self.camera = pg.Rect(x, y, self.width, self.height)