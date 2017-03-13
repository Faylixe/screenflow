#!/usr/bin/python

""" Simple test suite for Message based screen associated classes. """

from screenflow.font_manager import FontManager, FontHolder
from screenflow.screens.message_based_screen import MessageBasedScreen
from screenflow.screens.message_based_screen import Message, XML_MESSAGE
from tests.mocks.surface_mock import factory as mock_factory
from pytest import raises

# Default name for testing.
DEFAULT_NAME = 'select'

# Default message used for testing.
DEFAULT_MESSAGE = 'Message'


def test_get_message_surface():
    """ Test case for surface factory method. """
    screen = MessageBasedScreen(DEFAULT_NAME, DEFAULT_MESSAGE)
    screen.font_manager = FontManager()
    screen.surface_factory = mock_factory
    surface = screen.get_message_surface((500, 500))
    assert surface.blit_call == 1
    assert surface.fill_call == 1
    lines = screen.message.lines(None, 500)
    assert len(lines) >= 0
    assert lines[0] == DEFAULT_MESSAGE


def test_message_lines():
    """ Test case for message splitting. """
    sizer = FontHolder(10)
    text = 'This is a very long text which requires to be splitted'
    message = Message(text)
    lines = message.lines(sizer, 100)
    assert len(lines) > 1


def test_message_large_token():
    """ Test case for message splitting with large token. """
    sizer = FontHolder(10)
    text = 'Thisisaverylongtextwhichrequirestobesplitted'
    message = Message(text)
    lines = message.lines(sizer, 200)
    assert len(lines) == 1
    assert lines[0] == 'Thisisaverylongtextwhichrequirestobesplitted'
