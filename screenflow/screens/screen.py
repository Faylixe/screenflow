#!/usr/bin/python

""" To document """

from screenflow.constants import WHITE

import pygame

class Screen(object):
    """ Base class for screen object. """

    def __init__(self, background_color=WHITE, primary_color=BLACK):
        """Default constructor.

        :param background_color:
        :param primary_color:
        """
        self.font_provider = None
        self.background_color = background_color
        self.primary_color = primary_color
    
    def set_font_provider(self, provider):
        """
        :param provider:
        """
        self.font_provider = provider

    def get_primary_font(self):
        """Returns font instance to use for rendering text.
        """
        return self.font_provider.get_primary_font()

    def get_secondary_font(self):
        """Returns font instance to use for rendering text.
        """
        return self.font_provider.get_secondary_font()

    def get_surface_size(self, surface):
        """
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
