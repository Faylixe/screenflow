#!/usr/bin/python

""" Simple test suite for FontHolder and FontManager classes. """

import pygame
from screenflow.font_manager import FontHolder, FontManager, draw_text
from screenflow.constants import BLACK, WHITE
from mocks.surface_mock import SurfaceMock

# Drawing position for testing.
DEFAULT_DRAW_POSITION = (0, 0)


def setup_module():
    """ Module font setup """
    pygame.init()
    pygame.font.init()


def check_font_holder_value(holder, expected_text_color, expected_font=None):
    """Ensures that font holder value matches given expected ones.

    :param holder: Holder to check value from.
    :param expected_text_color: Expected value returned by holder.get_text_color() method.
    :param expected_font: Expected value returnred by holder.get_font() method (optional).
    """
    assert isinstance(holder.font, pygame.font.Font)
    if expected_font is not None:
        assert holder.font == expected_font
    assert holder.text_color is not None
    assert holder.text_color == expected_text_color


def test_default_font_holder():
    """ Test case for default unsettled font holder instance. """
    holder = FontHolder(10)
    check_font_holder_value(holder, BLACK)


def test_custom_font_holder():
    """ Test case for settled font holder instance. """
    holder = FontHolder(10)
    font = pygame.font.SysFont('arial', 15)
    holder.font = font
    holder.text_color = WHITE
    check_font_holder_value(holder, WHITE, font)

def test_draw_text():
    """ Test case for draw_test. """
    holder = FontHolder(10)
    surface = SurfaceMock()
    draw_text('foo', surface, holder, DEFAULT_DRAW_POSITION)
    assert surface.blit_call == 1


def test_draw_primary_text():
    """ Test case for primary text drawing. """
    manager = FontManager()
    surface = SurfaceMock()
    manager.draw_primary_text('foo', surface, DEFAULT_DRAW_POSITION)
    assert surface.blit_call == 1


def test_draw_secondary_text():
    """ Test case for secondary text drawing. """
    manager = FontManager()
    surface = SurfaceMock()
    manager.draw_secondary_text('foo', surface, DEFAULT_DRAW_POSITION)
    assert surface.blit_call == 1
