#!/usr/bin/python

""" To document. """

# Default surface size used for testing.
DEFAULT_SURFACE_SIZE = (640, 480)


class SurfaceMock(object):
    """ Mock class for pygame Surface. """

    def __init__(self, size=DEFAULT_SURFACE_SIZE):
        """ Default constructor.

        :param size: Size of this mock surface (optional, default to 640x480)
        """
        self.size = size
        self.blit_call = 0

    def get_size(self):
        """ Returns the size of this surface.

        :returns: Size of this surface.
        """
        return self.size

    def blit(self, source, position):
        """ Blit method mocking.

        :param source: Source to blit into this surface.
        :param position: Position to blit source to.
        """
        self.blit_call += 1
