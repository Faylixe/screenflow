#!/usr/bin/python

"""
"""


class FontManager(object):
    """
    """

    def __init__(self):
        """ Default constructor. """
        self.fonts = {}

    def _create(self, name, size):
        """
        :param name:
        :param size:
        :returns:
        """
        return None

    def get(self, name, size):
        """
        :param name:
        :returns:
        """
        if name not in self.fonts.keys():
            self.fonts[name] = {}
        if size not in self.fonts.keys():
            self.fonts[name][size] = self._create(name, size)
        return self.fonts[name][size]
