#!/usr/bin/python

"""
    A FontManager is responsible for creating and caching font
    instance. Should be subclassed and provide implementation
    for create_font(name, size) method.s
"""


class FontManager(object):
    """ FontManager is a simple font caching factory. """

    def __init__(self):
        """ Default constructor. """
        self._fonts = {}

    def create_font(self, name, size):
        """Font factory method, create a font object from the given font name
        using the given font size.

        :param name: Name of the font to create object for.
        :param size: Size of the font to create.
        """
        raise NotImplementedError()

    def get(self, name, size):
        """Font access method. Creates the font instance if not exists.

        :param name: Name of the font to get.
        :param size: Size of the font to get.
        :returns: Required font instance.
        """
        if name not in self._fonts.keys():
            self._fonts[name] = {}
        if size not in self._fonts[name].keys():
            self._fonts[name][size] = self.create_font(name, size)
        return self._fonts[name][size]
