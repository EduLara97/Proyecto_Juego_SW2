import pygame


class EntityState(object):
    def __init__(self):
        self.current_sprite = None
        self.name = ""

    def get_sprite(self):
        return self.current_sprite

    def get_name(self):
        return self.name

    def get_width(self):
        return self.current_sprite.get_width()

    def get_height(self):
        return self.current_sprite.get_height()

    def update(self, dt):
        pass


class AnimatedState(EntityState):
    def __init__(self, images, number_of_sprites, speed, name):
        super(AnimatedState, self).__init__()

        self.images = images
        self.number_of_sprites = number_of_sprites
        self.speed = speed
        self.name = name
        self.current_sprite = self.images.subsurface(0, 0,
                                                     self.images.get_width() / self.number_of_sprites,
                                                     self.images.get_height())
        self.width = self.images.get_width()/ self.number_of_sprites
        self.height = self.images.get_height()
        self.is_loop = True
        self.current_delta = 0

    def update(self, dt):
        self.current_delta = self.current_delta + dt

        if self.current_delta > self.speed:
            if self.is_loop:
                self.current_delta = 0
            else:
                self.current_delta = self.current_delta - dt

        sprite_index = int((self.current_delta * self.number_of_sprites / self.speed))

        if sprite_index > self.number_of_sprites - 1:
            sprite_index = self.number_of_sprites - 1

        self.current_sprite = self.images.subsurface(sprite_index * self.width, 0,
                                                     self.width, self.height)


class StaticState(EntityState):
    def __init__(self, image, name):
        super(StaticState, self).__init__()
        self.current_sprite = image
        self.name = name
