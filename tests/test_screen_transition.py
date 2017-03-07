#!/usr/bin/python

""" Simple test suite for ScreenTransition class. """

from screenflow.screenflow import ScreenTransition
from mocks.surface_mock import SurfaceMock, DEFAULT_SURFACE_SIZE

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
    final_position = check_transition(
        ScreenTransition.FORWARD,
        20,
        DEFAULT_SURFACE_SIZE[0],
        -20,
        DEFAULT_SURFACE_SIZE[0])
    assert final_position < 0

def test_backward_transition():
    """ Test case for backward transition. """
    final_position = check_transition(
        ScreenTransition.BACKWARD,
        20,
        DEFAULT_SURFACE_SIZE[0],
        20,
        0)
    assert final_position > DEFAULT_SURFACE_SIZE[0]