#!/usr/bin/python

"""

    Screen
    ======

    A **Screen** is a basic unit which is manipulated by a **Screenflow**.

    Rendering
    ---------

    Text rendering
    ~~~~~~~~~~~~~~

    In order to draw text, a **Screen** use a **FontManager**, which manages.

    Background
    ~~~~~~~~~~

    Event handling
    --------------

"""

from screenflow.constants import WHITE

import pygame


class Sizeable(object):
    """
    """

    def __init__(self, object, sizer):
        """Default constructor.

        :param data:
        """
        self.data = data
        self.sizer = sizer
        self._size = None

    @property
    def size(self):
        """
        :returns:
        """
        if self._size is None:
            self._size = self.sizer(data)
        return self._size


class Screen(object):
    """ Base class for screen object. """

    def __init__(self, name, background_color=WHITE):
        """Default constructor.

        :param name: Name of this screen.
        :param background_color: Default background color.
        """
        self.name = name
        self.padding = (0, 0)
        self._font_manager = None
        self.background_color = background_color

    @property
    def font_manager(self):
        """
        :returns:
        """
        if self._font_manager is None:
            raise AttributeError('Font manager not initialized')
        return self._font_manager

    @font_manager.setter
    def font_manager(self, delegate):
        """
        :param delegate:
        """
        self._font_manager = delegate

    def create_primary_sizeable(self, sizeable):
        """
        """
        pass

    def get_surface_size(self, surface):
        """ Surface
        """
        return surface.get_size()

    def process_event(self):
        """ To doc
        """
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                self.on_mouse_down(pygame.mouse.get_pos())
            elif event.type == MOUSEBUTTONUP:
                self.on_mouse_up(pygame.mouse.get_pos())

    def generate_preview(self, size):
        """
        :param size:
        :returns:
        """
        surface = pygame.Surface(size)
        self.draw(surface)
        return surface

    def draw_background(self, surface):
        """Draw screen background by filling it with the background color.

        :param surface: Surface to draw background into.
        """
        surface.fill(self.background_color)

    def draw(self, surface):
        """
        :param surface: Surface to draw screen into.
        """
        self.draw_background(surface)

    def on_screen_activated(self):
        """ Callback method for screen activation pre processing. """
        pass

    def on_mouse_down(self, position):
        """
        :param position:
        """
        pass

    def on_mouse_up(self, position):
        """
        :param position:
        """
        pass
