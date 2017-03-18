#!/usr/bin/python

""" """

from screenflow.graphics.drawer import Drawer
from mock_surface import MockSurface


class MockDrawer(Drawer):
    """ """

    def __init__(self):
        """ """
        Drawer.__init__(self)

    def create_surface(self, size):
        """
        :param size:
        :returns:
        """
        return MockSurface(size)

    def fill_surface(self, surface, color):
        """
        :param surface:
        :param color:
        """
        surface.fill(color)

    def blit_surface(self, destination, source, position):
        """
        :param destination:
        :param source:
        :param position:
        """
        raise NotImplementedError()

