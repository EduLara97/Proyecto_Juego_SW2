#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports
import pygame
from pygame.locals import *
from Utils import *
#from source.States import *

"""
    Version: 0.8
    Author: Anthony Del Pozo Matías
    Email: delan1997@gmail.com
"""

class FormFactory():

    """
        No se me ocurre nada aún
    """

    pass


class FormComponent():

    """
        Interface componente de formulario
    """

    def draw(self):
        pass

    def update(self):
        pass

class Form(FormComponent):

    """
        Clase contenedora de los componentes de un formulario
    """

    def __init__(self, screen):
        self.screen = screen
        self.childs = []

    def draw(self):
        for child in self.childs:
            child.draw()

    def add_child(self, child):
        child.form = self
        self.childs.append(child)

class EditText(FormComponent):

    """
        Clase que genera un input en formato EditText
    """

    # Constructor
    def __init__(self, x=0, y=0, width=200, height=40, border=2, value='', focus=False , max=20):
        self.x = x
        self.y = y
        self.width = self.calc_width(width, max)
        self.height = height
        self.border = border
        self.value = value
        self.max = max
        self.focus = focus
        self.alert = False

    def set_value(self, value):
        self.value = value

    def calc_width(self, width, max):
        return max * 7 if width < max * 7 else width

    # Escribir dentro del input
    def type_char(self, char):
        if len(self.value) < self.max and self.focus:
            self.value = ''.join([self.value, char])

    # Cambiar el color de los bordes, se modifican con el atributo Focus
    def load_border_color(self):
        if self.alert:
            return (255, 0, 0)
        return (247, 177, 33) if self.focus else (0, 0, 0)

    # Validar que el input no esté vacío
    def is_empty(self):
        return self.value.strip() == ''

    def empty_alert(self):
        self.alert = True

    # Dibujar el input en el Display
    def draw(self):
        margin = 5
        size = 40
        font = pygame.font.SysFont(None, size)
        title = font.render(self.value, True, (0, 0, 0))
        self.rect = pygame.draw.rect(self.form.screen, self.load_border_color(),(self.x,self.y,self.width,self.height),self.border)
        self.form.screen.blit(title, (self.x + margin, self.y + margin))

    # Evaluar si hicieron click dentro de la input (caja)
    def collidepoint(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            self.focus = True
        else:
            self.focus = False

    # Renderiza los nuevos cambios del input
    def update(self, e):
        self.draw()
        if e.type == KEYDOWN:
            # Catch enter
            if pygame.key.name(e.key) in ['up','down','left','right']:
                return
            if e.key == 'return':
                return True
            # Move cursor
            # elif key == 'left':
            #      self._cursor_back()
            # elif key == 'right':
            #     self._cursor_forward()
            # # Edit text
            # elif key == 'backspace':
            #      self._backspace()
            elif e.key == K_BACKSPACE and self.focus == True:
                self.value = self.value[0:len(self.value)-1]
            elif e.key == K_SPACE:
                self.type_char(' ')
            elif len(e.unicode) == 1:
                self.type_char(e.unicode)
            # Signal event unused
            else:
                r = True


class RadioButtonManager(FormComponent):

    """
        Clase gestora del comportamiento de los radios buttons
    """

    # Constructor
    def __init__(self):
        self.buttons = []

    def draw(self):
        for button in self.buttons:
            button.draw()

    # Elige el botón clickeado y deselecciona los otros botones
    def update(self, clicked_button):
        for button in self.buttons:
            if button == clicked_button:
                button.focus = True
            else:
                button.focus = False

    # Agrega botones al Radio Group
    def add_button(self, button):
        button.manager = self
        self.buttons.append(button)

    # Obtiene los botones del Radio Group
    def get_buttons(self):
        return self.buttons

    def get_button_focused(self):
        for button in self.buttons:
            if button.focus == True:
                return button

class Button(FormComponent):

    """
        Clase que genera y gestiona un botón
    """

    # Constuctor
    def __init__(self, x=0, y=0, width=200, height=40, border=2, value='', focus=False, args=''):
        self.x = x
        self.y = y
        self.width = len(value) * 19 if width < len(value) * 19 else width
        self.height = height
        self.border = border
        self.value = value
        self.focus = focus
        self.args = args

    # Cambiar el color de los bordes, se modifican con el atributo Focus
    def load_border_color(self):
        return (247, 177, 33)  if self.focus else (0, 0, 0)

    # Evalua si el botón fue clickeado
    def collidepoint(self, mouse_position):
        if self.rect.collidepoint(mouse_position):
            self.manager.update(self)

    # Renderiza el botón en el Display
    def draw(self):
        margin = 5
        size = 40
        font = pygame.font.SysFont(None, size)
        title = font.render(self.value,True, self.load_border_color())
        if hasattr(self,'form'):
            self.rect = pygame.draw.rect(self.form.screen, self.load_border_color(),(self.x,self.y,self.width,self.height),self.border)
            self.form.screen.blit(title, (self.x + margin, self.y + margin))
        else:
            self.rect = pygame.draw.rect(self.manager.form.screen, self.load_border_color(),(self.x,self.y,self.width,self.height),self.border)
            self.manager.form.screen.blit(title, (self.x + margin, self.y + margin))

class Title(FormComponent):
    # Constructor
    def __init__(self, x=0, y=0, value='', color=(247, 177, 33), h='H1', border = 0):
        self.x = x
        self.y = y
        self.h = self.get_h(h)
        self.value = value
        self.color = color
        self.hide = False
        self.border = border

    def get_h(self,h):
        hs = {
            'H1': 80,
            'H2': 70,
            'H3': 60,
            'H4': 50,
            'H5': 40,
            'H6': 30,
        }
        if h not in hs:
            return hs['H1']
        return hs[h]

    def draw(self):
        # self.hide = not self.hide
        # if self.hide:
        #     return
        font = pygame.font.SysFont(None, self.h)
        title = font.render(self.value, True, self.color)
        if not self.border == 0:
            pygame.draw.rect(self.form.screen, (247, 177, 33),(0,self.y - 10,self.form.screen.get_rect().width,75),2)
        self.form.screen.blit(title, (self.x, self.y))

# Título que parpadea

class DialogManager():

    """
        Clase gestora del comportamiento de los dialogs
    """

    # Constructor
    def __init__(self):
        self.dialogs = []
        self.current_dialog = None
        self.previous_dialogs = []
        self.index = 0

    def draw(self):
        [ dialog.draw() for dialog in self.previous_dialogs]
        self.current_dialog.draw()
        # for dialog in self.dialogs:
        #     dialog.draw()

    def next_dialog(self):
        self.current_dialog.previous = True
        self.previous_dialogs.append(self.current_dialog)
        if self.index + 1 < len(self.dialogs):
            self.index = self.index + 1
            self.current_dialog = self.dialogs[self.index]

    # Elige el botón clickeado y deselecciona los otros botones
    def update(self, clicked_button):
        for button in self.buttons:
            if button == clicked_button:
                button.focus = True
            else:
                button.focus = False

    # Agrega botones al Radio Group
    def add_dialog(self, dialog):
        if len(self.dialogs) == 0:
            self.current_dialog = dialog
        dialog.manager = self
        self.dialogs.append(dialog)

    # Obtiene los botones del Radio Group
    def get_dialogs(self):
        return self.dialogs


class Dialog():

    def __init__(self, x=0, y=0, value='', color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.h = 30
        self.value = value
        self.temp = ""
        self.index = 0
        self.color = color
        self.effect = None
        self.previous = False

    def draw(self):
        if self.index <= len(self.value):
            self.temp = self.value[0:self.index]
            self.index = self.index + 1
            if self.effect == None:
                pass
                # self.effect = pygame.mixer.Sound('mp3/dialog.wav')
                # self.effect.play()
        elif self.previous == False:
            # self.effect.stop()
            self.manager.next_dialog()
            pygame.time.delay(100)

        font = pygame.font.SysFont(None, self.h)
        title = font.render(self.temp, True, self.color)
        self.manager.form.screen.blit(title, (self.x, self.y))

class PrettyTitle():
    # Constructor
    def __init__(self, x=0, y=0, value='',options=[], color=(247, 177, 33), h='H1'):
        self.x = x
        self.y = y
        self.h = self.get_h(h)
        self.base = value
        self.value = ' '.join([value,options[0]])
        self.options = options
        self.color = color
        self.boo = True

    def get_h(self,h):
        hs = {
            'H1': 80,
            'H2': 70,
            'H3': 60,
            'H4': 50,
            'H5': 40,
            'H6': 30,
        }
        if h not in hs:
            return hs['H1']
        return hs[h]

    def draw(self):
        font = pygame.font.SysFont(None, self.h)
        title = font.render(self.value, True, self.color)
        self.form.screen.blit(title, (self.x, self.y))


class Label(FormComponent):

    # Constructor
    def __init__(self, x=0, y=0, value='', size=40, color=(247, 177, 33)):
        self.x = x
        self.y = y
        self.value = value
        self.size = size
        self.color = color

    def draw(self):
        font = pygame.font.SysFont(None, self.size)
        title = font.render(self.value, True, self.color)
        self.form.screen.blit(title, (self.x, self.y))


class Image(FormComponent):

    # Constructor
    def __init__(self, x=0, y=0, path=''):
        self.x = x
        self.y = y
        self.path = path

    def draw(self):
        image = pygame.image.load(self.path)
        rect = image.get_rect()
        self.form.screen.blit(image, rect)

class ImageGIF(FormComponent):

    # Constructor
    def __init__(self, x=0, y=0, path=''):
        self.x = x
        self.y = y
        self.path = path
        self.load_image()

    """def load_image(self):
        self.images = pygame.image.load(self.path)
        self.image_gif = AnimatedState(self.images, 2, 150, "logo")"""

    def draw(self):
        self.image_gif.update(20)
        rect = self.image_gif.get_sprite().get_rect()
        self.form.screen.blit(self.image_gif.get_sprite(), rect)