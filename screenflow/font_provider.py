#!/usr/bin/python

""" Module that provides FontProvider base class. """

import logging
import pygame

# Configure logger.
logging.basicConfig()
logger = logging.getLogger(__name__)

class FontProvider(object):
    """A FontProvider is responsible for storing two fonts :

    - Primary font that will be used for important text display.
    - Secondary font that will be used for tips, subheading, and so on.

    When accessing a font through getter method, if font has not been settled,
    default system font is used (Arial, 15 for primary, 10 for secondary).
    """

    def __init__(self):
        """ Default constructor. """
        self.primary_font = None
        self.secondary_font = None

    def get_primary_font(self):
        """Primary font instance getter. Creating
        one is not available using arial system font.

        :returns: Primary font instance to use.
        """
        if self.primary_font is None:
            logging.debug('Primary font not settled, using default Arial from system')
            self.primary_font = pygame.font.SysFont("arial", 15)
        return self.primary_font

    def get_secondary_font(self):
        """Secondary font instance getter. Creating
        one is not available using arial system font.

        :returns: Secondary font instance to use.
        """
        if self.secondary_font is None:
            logging.debug('Secondary font not settled, using default Arial from system')
            self.primary_font = pygame.font.SysFont("arial", 10)
        return self.secondary_font
