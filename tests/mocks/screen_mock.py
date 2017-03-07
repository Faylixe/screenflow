#!/usr/bin/python

""" To document. """

class ScreenMock(object):
    """ Mock class for Screen. """

    def __init__(self, name):
        """ Default constructor. """
        self.font_manager = None
        self.name = name

    def set_font_manager(self, manager):
        """ """
        self.font_manager = manager
    