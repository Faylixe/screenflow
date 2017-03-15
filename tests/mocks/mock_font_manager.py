#!/usr/bin/python

""" Mock implementation for FontManager. """

from screenflow.graphics.font_manager import FontManager
from mock_font import MockFont


class MockFontManager(FontManager):
    """ Mock implementation of FontManager class. """

    def __init__(self):
        """ Default constructor. """
        FontManager.__init__(self)

    def create_font(self, name, size):
        """Font factory method, create a font object from the given font name
        using the given font size.

        :param name: Name of the font to create object for.
        :param size: Size of the font to create.
        """
        return MockFont(name, size)
