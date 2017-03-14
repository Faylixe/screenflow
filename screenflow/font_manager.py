#!/usr/bin/python

"""
    FontManager
    ===========

    A FontManager is responsible for creating and caching font instance.
"""

from pygame.font import SysFont


class FontManager(object):
    """ FontManager is a simple font caching factory. """

    def __init__(self):
        """ Default constructor. """
        self.fonts = {}
        self.__font_factory = None

    @property
    def font_factory(self):
        """Font factory property getter.

        :returns: Font factory instance to use.
        """
        if self.__font_factory is None:
            self.__font_factory = SysFont
        return self.__font_factory

    @font_factory.setter
    def font_factory(self, font_factory):
        """Font factory property setter.

        :param font_factory: Font factory instance to use.
        """
        self.__font_factory = font_factory

    def get(self, name, size):
        """Font access method. Creates the font instance if not exists.

        :param name: Name of the font to get.
        :param size: Size of the font to get.
        :returns: Required font instance.
        """
        if name not in self.fonts.keys():
            self.fonts[name] = {}
        if size not in self.fonts.keys():
            self.fonts[name][size] = font_factory(name, size)
        return self.fonts[name][size]
