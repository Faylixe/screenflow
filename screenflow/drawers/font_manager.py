#!/usr/bin/python

"""
"""


class FontManager(object):
    """ FontManager is a simple font caching factory. """

    def __init__(self, font_factory):
        """ Default constructor. """
        self.fonts = {}
        self.font_factory = font_factory

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
