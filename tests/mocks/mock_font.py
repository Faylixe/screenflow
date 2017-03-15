#!/usr/bin/python

""" Mock font object implementation """


class MockFont(object):
    """ Simple font mock representation. """

    def __init__(self, name, size):
        """Default constructor.

        :param name: Name of this font.
        :param size: Size of this font.
        """
        self.name = name
        self.size = size
