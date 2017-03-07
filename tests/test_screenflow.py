#!/usr/bin/python

""" To document. """

import pygame

from screenflow import ScreenFlow, NavigationException, ScreenTransition
from screenflow.constants import BLACK, WHITE
from screenflow.constants import XML_SCREENFLOW, XML_SCREEN, XML_TYPE

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
        return size

    def blit(self, source, position):
        """ Blit method mocking.

        :param source: Source to blit into this surface.
        :param position: Position to blit source to.
        """
        self.blit_call += 1

def check_transition(side, speed, width, expected_speed, expected_position):
    """ Executes and check a transition using given side, speed and surface width.

    :param side: Side of the created transition.
    :param speed: Speed of the created transition.
    :param width: Width of the target surface transition is running into.
    :param expected_speed: Expected effective speed value for transition.
    :param expected_position: Expected starting position for transition.
    """
    surface = SurfaceMock()
    previews = [SurfaceMock(), SurfaceMock()]
    transition = ScreenTransition(previews, side, speed)
    assert transition.speed == expected_speed
    assert transition.position == expected_position
    while transition.update(surface):
        continue
    assert surface.blit_call == (width / speed) * 2
    return transition.position

def test_forward_transition():
    """ Test case for forward transition. """
    final_position = check_transition(ScreenTransition.FORWARD, 20, 480,  -20, 480)
    assert final_position < 0

def test_backward_transition():
    """ Test case for backward transition. """
    final_position = check_transition(ScreenTransition.BACKWARD, 20, 480,  20, 0)
    assert final_position > 480