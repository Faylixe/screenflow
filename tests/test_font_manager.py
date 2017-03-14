#!/usr/bin/python

""" Simple test suite for FontManager class. """

from pygame.font import SysFont, init as font_init
from screenflow.font_manager import FontManager


def setup_module(module):
    """Module fixture.

    :param module: Test module to setup.
    """
    font_init()


def test_get():
    """ FontManager access test case."""
    manager = FontManager()
    font = manager.get('arial', 20)
    assert font == manager.get('arial', 20)
    assert font != manager.get('arial', 30)


def test_font_factory():
    """ FontManager delegate factory test case. """
    manager = FontManager()
    assert manager.font_factory == SysFont

    def factory(name, size):
        return None
    manager.font_factory = factory
    assert manager.get('arial', 20) is None
