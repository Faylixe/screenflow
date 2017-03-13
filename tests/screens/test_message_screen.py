#!/usr/bin/python

""" Simple test suite for Message screen associated classes. """

from screenflow.constants import XML_NAME
from screenflow.font_manager import FontManager
from screenflow.screens import MessageScreen
from screenflow.screens.message_screen import factory
from screenflow.screens.message_based_screen import Message, XML_MESSAGE
from tests.mocks.surface_mock import SurfaceMock, factory as mock_factory
from pytest import raises

# Default name for testing.
DEFAULT_NAME = 'select'

# Default message used for testing.
DEFAULT_MESSAGE = 'Message'


def create_message_screen(name=DEFAULT_NAME, message=DEFAULT_MESSAGE):
    """Simple factory method that creates
    a message using the given name and message.

    :param name: Name of the created screen.
    :param message: Message of the created screen.
    """
    screen_def = {}
    screen_def[XML_NAME] = name
    screen_def[XML_MESSAGE] = message
    screen = factory(screen_def)
    return screen


def test_factory():
    """ Test case for message screen factory. """
    screen = create_message_screen()
    assert isinstance(screen, MessageScreen)
    assert screen.name == DEFAULT_NAME


def test_messageless_factory():
    """ Test case for message screen factory with invalid definition. """
    with raises(AttributeError) as e:
        factory({})


def test_on_touch():
    """ Test case for on_touch event binding. """
    screen = create_message_screen()

    @screen.on_touch
    def callback():
        pass
    assert screen.callback == callback


def test_mouse_event():
    """ Test case for mouse event. """
    screen = create_message_screen()
    call = []

    def callback():
        call.append(True)
    screen.callback = callback
    screen.on_mouse_up(None)
    assert len(call) == 1


def test_draw():
    """ Test case for message screen drawing method. """
    screen = create_message_screen()
    screen.font_manager = FontManager()
    screen.surface_factory = mock_factory
    surface = SurfaceMock()
    screen.draw(surface)
    assert surface.fill_call == 1
    assert surface.blit_call == 1
    lines = screen.message.lines(None, surface.get_size()[0])
    assert len(lines) >= 0
    assert lines[0] == DEFAULT_MESSAGE
