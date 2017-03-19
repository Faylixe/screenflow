#!/usr/bin/python

""" Simple test suite for Message based screen associated classes. """

from screenflow.css.font_manager import FontManager
from screenflow.css.style_factory import StyleFactory
from screenflow.screens.message_based_screen import MessageBasedScreen
from screenflow.screens.message_based_screen import Message, XML_MESSAGE
from tests.mocks.mock_surface import factory as mock_factory
from pytest import raises, fixture

# Default name for testing.
DEFAULT_NAME = 'select'

# Default message used for testing.
DEFAULT_MESSAGE = 'Message'

# Screen type parameter.
SCREEN_TYPE = 'test_screen'


@fixture
def screen():
    """ Fixture for message based screen parameter. """
    screen = MessageBasedScreen(DEFAULT_NAME, SCREEN_TYPE, DEFAULT_MESSAGE)
    screen.configure_styles(StyleFactory())
    screen.font_manager = FontManager()
    return screen


def test_get_message_surface(screen):
    """ Test case for surface factory method. """
    screen.surface_factory = mock_factory
    surface = screen.get_message_surface((500, 500))
    assert surface.blit_call == 1
    assert surface.fill_call == 1
    lines = screen.message.lines(None, 500)
    assert len(lines) >= 0
    assert lines[0] == DEFAULT_MESSAGE


def test_message_lines(screen):
    """ Test case for message splitting. """
    text = 'This is a very long text which requires to be splitted'
    message = Message(text)
    lines = message.lines(screen.primary_size, 100)
    assert len(lines) > 1


def test_message_large_token(screen):
    """ Test case for message splitting with large token. """
    text = 'Thisisaverylongtextwhichrequirestobesplitted'
    message = Message(text)
    lines = message.lines(screen.primary_size, 200)
    assert len(lines) == 1
    assert lines[0] == 'Thisisaverylongtextwhichrequirestobesplitted'
