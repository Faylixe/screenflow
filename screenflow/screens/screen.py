#!/usr/bin/python

""" To document """

from screenflow.constants import WHITE

import pygame

class Screen(object):
    """ Base class for screen object. """

    def __init__(self, background_color=WHITE):
        """Default constructor.

        :param background_color:
        """
        self.font_manager = None
        self.background_color = background_color

    def set_font_manager(self, font_manager):
        """
        :param font_manager:
        """
        self.font_manager = font_manager

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
