#!/usr/bin/python

""" To document. """

class FontProvider(object):
    """ To document. """

    def __init__(self):
        """ """
        self.primary_font = None
        self.secondary_font = None

    def get_primary_font(self):
        """ """
        if self.primary_font is None:
            # TODO : Load default font.
        return self.primary_font

    def get_secondary_font(self):
        """ """
        if self.secondary_font is None:
            # TODO : Load default font.
        return self.secondary_font