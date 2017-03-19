#!/usr/bin/python

""" To document. """

from mock_surface import MockSurface


class MockScreen(object):
    """ Mock class for Screen. """

    def __init__(self, name):
        """ Default constructor. """
        self._font_manager = None
        self.name = name
        self.preview_generated = 0

    def configure_styles(self, style_factory):
        """ """
        pass

    def generate_preview(self, size):
        """ """
        self.preview_generated += 1
        return MockSurface(size)
