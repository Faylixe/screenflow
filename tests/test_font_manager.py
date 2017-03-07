#!/usr/bin/python

""" Simple test suite for FontHolder and FontManager classes. """

import pygame

from screenflow.font_manager import FontHolder, FontManager
from screenflow.constants import BLACK, WHITE

def setup_module():
    """ Module font setup """
    pygame.init()
    pygame.font.init()

def check_created_font_holder(holder, expected_default_size=10):
    """Ensures the given created holder as default expected values.

    :param holder: Holder to check state for.
    :param expected_default_size: Expected holder default size (optional, default to 10).
    """
    assert holder.font is None
    assert holder.text_color is None
    assert holder.default_size == expected_default_size

def check_font_holder_value(holder, expected_text_color, expected_font=None):
    """Ensures that font holder value matches given expected ones.
    
    :param holder: Holder to check value from.
    :param expected_text_color: Expected value returned by holder.get_text_color() method.
    :param expected_font: Expected value returnred by holder.get_font() method (optional).
    """
    font = holder.get_font()
    text_color = holder.get_text_color()
    assert isinstance(font, pygame.font.Font)
    if expected_font is not None:
        assert font == expected_font
    assert text_color is not None
    assert text_color == expected_text_color

def test_default_font_holder():
    """ Test case for default unsettled font holder instance. """
    holder = FontHolder(10)
    check_created_font_holder(holder)
    check_font_holder_value(holder, BLACK)

def test_custom_font_holder():
    """ Test case for settled font holder instance. """
    holder = FontHolder(10)
    check_created_font_holder(holder)
    font = pygame.font.SysFont('arial', 15)
    holder.font = font
    holder.text_color = WHITE
    check_font_holder_value(holder, WHITE, font)

def test_font_manager():
    """ FontManager test. """
    manager = FontManager()
    check_created_font_holder(manager.primary, 15)
    check_created_font_holder(manager.secondary)
