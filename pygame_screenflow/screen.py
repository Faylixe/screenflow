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
                pass
            elif event.type == MOUSEBUTTONUP:
                pass

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
