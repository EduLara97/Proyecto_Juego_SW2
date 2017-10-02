import pygame

from utils.States import AnimatedState, StaticState



class GameEntity(pygame.sprite.Sprite):
    def __init__(self, display):
        super(GameEntity, self).__init__()

        self.display = display
        self.states_dict = {}
        self.current_state = None
        self.dx = 0
        self.dy = 0
        self.image = None
        self.jumping = False

    def set_current_state(self, key):
        self.current_state = self.states_dict[key]

    def impulse(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def update(self, dt):
        """raise: Sirve para levantar errores"""
        raise NotImplementedError("The update method must be called in any child class")


class Character(GameEntity):
    def __init__(self, display, px, py, perso):
        super(Character, self).__init__(display)
        print(perso)
        self.speed = 3.5
        self.walking_images = pygame.image.load(perso)
        self.walking_images = pygame.transform.scale(self.walking_images, (300, 250))
        self.number_of_sprites = 4

        self.walking_right_state = AnimatedState(self.walking_images.subsurface(0, 0,
                                                                                self.walking_images.get_width(),
                                                                                self.walking_images.get_height() / 2),
                                                 self.number_of_sprites, 400, "walking_right")

        self.walking_left_state = AnimatedState(self.walking_images.subsurface(0, self.walking_images.get_height() / 2,
                                                                               self.walking_images.get_width(),
                                                                               self.walking_images.get_height() / 2),
                                                self.number_of_sprites, 400, "walking_left")

        self.resting_right_state = StaticState(self.walking_images.
                                               subsurface(0, 0,
                                                          self.walking_images.get_width() / self.number_of_sprites,
                                                          self.walking_images.get_height() / 2), "resting_right")

        self.resting_left_state = StaticState(self.walking_images.
                                              subsurface(self.walking_images.get_width() * 3 / 4,
                                                         self.walking_images.get_height() / 2,
                                                         self.walking_images.get_width() / self.number_of_sprites,
                                                         self.walking_images.get_height() / 2), "resting_left")

        self.states_dict[self.walking_right_state.get_name()] = self.walking_right_state
        self.states_dict[self.walking_left_state.get_name()] = self.walking_left_state
        self.states_dict[self.resting_right_state.get_name()] = self.resting_right_state
        self.states_dict[self.resting_left_state.get_name()] = self.resting_left_state

        self.set_current_state(self.resting_right_state.get_name())
        self.image = self.current_state.get_sprite()
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py

    def calculate_gravity(self):
        self.dy = self.dy + 0.35

    def jump(self, jump_force):
        self.impulse(self.dx, -jump_force)

    def key_down(self, key):
        if key == pygame.K_UP:
            if not self.jumping:
                pygame.mixer.Sound.play(pygame.mixer.Sound("assets/audio/jump.wav"))
                self.jump(10)
                self.jumping = True
        if key == pygame.K_DOWN:
            pass
        if key == pygame.K_RIGHT:
            self.dx = self.speed
            self.set_current_state(self.walking_right_state.get_name())
        if key == pygame.K_LEFT:
            self.dx = -self.speed
            self.set_current_state(self.walking_left_state.get_name())

    def key_up(self, key):
        if key == pygame.K_UP:
            pass
        if key == pygame.K_DOWN:
            pass
        if key == pygame.K_RIGHT:
            if self.dx > 0:
                self.dx = 0
                self.set_current_state(self.resting_right_state.get_name())
        if key == pygame.K_LEFT:
            if self.dx < 0:
                self.dx = 0
                self.set_current_state(self.resting_left_state.get_name())

    def update(self, dt):
        self.calculate_gravity()
        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy
        if self.rect.y + self.rect.height > self.display.get_height() - 62:
            self.rect.y = self.display.get_height() - 62 - self.rect.height
            self.jumping = False
            self.dy = 0
        self.current_state.update(dt)
        self.image = self.current_state.get_sprite()
