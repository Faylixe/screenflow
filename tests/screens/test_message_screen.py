#!/usr/bin/python

""" Simple test suite for Message screen associated classes. """

from screenflow.constants import XML_NAME
from screenflow.font_manager import FontManager
from screenflow.style_factory import StyleFactory
from screenflow.screens import MessageScreen
from screenflow.screens.message_screen import factory
from screenflow.screens.message_based_screen import Message, XML_MESSAGE
from tests.mocks.mock_surface import MockSurface, factory as mock_factory
from pytest import raises, fixture

# Default name for testing.
DEFAULT_NAME = 'select'

# Default message used for testing.
DEFAULT_MESSAGE = 'Message'


@fixture
def screen():
    """ Fixture for screen parameter. """
    screen_def = {}
    screen_def[XML_NAME] = DEFAULT_NAME
    screen_def[XML_MESSAGE] = DEFAULT_MESSAGE
    screen = factory(screen_def)
    return screen


def test_factory(screen):
    """ Test case for message screen factory. """
    assert isinstance(screen, MessageScreen)
    assert screen.name == DEFAULT_NAME


def test_messageless_factory():
    """ Test case for message screen factory with invalid definition. """
    with raises(AttributeError) as e:
        factory({})


def test_on_touch(screen):
    """ Test case for on_touch event binding. """
    @screen.on_touch
    def callback():
        pass
    assert screen._callback == callback


def test_mouse_event(screen):
    """ Test case for mouse event. """
    call = []

    def callback():
        call.append(True)
    screen._callback = callback
    screen.on_mouse_up(None)
    assert len(call) == 1


def test_draw(screen):
    """ Test case for message screen drawing method. """
    screen.font_manager = FontManager()
    screen.configure_styles(StyleFactory())
    screen.surface_factory = mock_factory
    surface = MockSurface()
    screen.draw(surface)
    assert surface.fill_call == 1
    assert surface.blit_call == 1
    drawable_size = screen.get_surface_drawable_size(surface)
    lines = screen.message.lines(None, drawable_size[0])
    assert len(lines) >= 0
    assert lines[0] == DEFAULT_MESSAGE
