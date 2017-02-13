#!/usr/bin/python

""" To Document """

from screenflow.views.view import View

class Layout(View):
    """ To document. """

    def __init__(self):
        """Default constructor.
        """
        View.__init__(self)

    def get_expected_size(self, parent_size):
        """
        :param parent_size:
        :returns:
        """
        return (0, 0)

    def draw(self, surface, position):
        """
        :param surface:
        :param position:
        """
        pass
