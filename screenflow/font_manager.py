#!/usr/bin/python

""" Module that provides FontManager base class. """

import logging
import pygame

from constants import BLACK

# Configure logger.
logging.basicConfig()
logger = logging.getLogger(__name__)


class FontHolder(object):
    """Holder class for a font and a text color.

    When accessing a font through getter method, if font has not been settled,
    default system Arial font is used.
    """

    def __init__(self, default_size):
        """ Default constructor. """
        self._font = None
        self.text_color = BLACK
        self.default_size = default_size

    @property
    def font(self):
        """Delegate font instance getter. Creating
        one if not available using arial system font.

        :returns: Font instance to use.
        """
        if self._font is None:
            logging.debug('Font not settled, using default Arial from system')
            self._font = pygame.font.SysFont('arial', self.default_size)
        return self._font


def draw_text(text, surface, holder, position):
    """Simple methods that draws text on the given surface
    using the given font holder for resources.

    :param text: Text to draw.
    :param surface: Surface to draw text into.
    :param holder: FontHolder instance to use for getting font and text color.
    :param position: Position of the text to draw relative to the surface.
    """
    surface.blit(holder.font.render(text, 1, holder.text_color, None), position)


class FontManager(object):
    """A FontManager is responsible for storing two fonts :

    - Primary font that will be used for important text display.
    - Secondary font that will be used for tips, subheading, and so on.

    """

    def __init__(self):
        """ Default constructor. """
        self.primary = FontHolder(15)
        self.secondary = FontHolder(10)

    def draw_primary_text(self, text, surface, position):
        """Draws text to screen using primary font.

        :param text: Text to draw.
        :param surface: Surface to draw text into.
        :param position: Position of the text to draw relative to the surface.
        """
        draw_text(text, surface, self.primary, position)

    def draw_secondary_text(self, text, surface, position):
        """Draws text to screen using secondary font.

        :param text: Text to draw.
        :param surface: Surface to draw text into.
        :param position: Position of the text to draw relative to the surface.
        """
        draw_text(text, surface, self.secondary, position)
