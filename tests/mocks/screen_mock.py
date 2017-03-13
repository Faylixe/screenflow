#!/usr/bin/python

""" To document. """

from surface_mock import SurfaceMock


class ScreenMock(object):
    """ Mock class for Screen. """

    def __init__(self, name):
        """ Default constructor. """
        self.font_manager = None
        self.name = name
        self.preview_generated = 0

    def set_font_manager(self, manager):
        """ """
        self.font_manager = manager

    def generate_preview(self, size):
        """ """
        self.preview_generated += 1
        return SurfaceMock(size)
