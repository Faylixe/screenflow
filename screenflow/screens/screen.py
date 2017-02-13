#!/usr/bin/python

""" To document """

import pygame

class Screen(object):
    """ Base class for screen object. """

    def __init__(self):
        """Default constructor.
        """
        pass

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

    def draw(self, surface):
        """
        :param surface:
        """
        pass

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

    @staticmethod
    def create(metadata):
        """
        :param metadata:
        """
        if '@type' not in metadata.keys():
            raise AttributeError('No screen type specified.')
        screen_type = metadata['@type']
        if type == 'select':
            pass
        elif type == 'input':
            pass
        else:
            raise ValueError('Unknown screen type %s' % screen_type)
