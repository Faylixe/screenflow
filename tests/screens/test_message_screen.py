#!/usr/bin/python

""" Simple test suite for Message screen associated classes. """

from screenflow.constants import XML_NAME
from screenflow.font_manager import FontManager
from screenflow.screens import MessageScreen
from screenflow.screens.message_screen import factory, XML_MESSAGE
from tests.mocks.surface_mock import SurfaceMock
from nose.tools import raises


def create_message_screen(name, message):
    """Simple factory method that creates
    a message using the given name and message.

    :param name: Name of the created screen.
    :param message: Message of the created screen.
    """
    screendef = {}
    screendef[XML_NAME] = name
    screendef[XML_MESSAGE] = message
    screen = factory(screendef)
    return screen


def test_factory():
    """ Test case for message screen factory. """
    name = 'foo'
    screen = create_message_screen(name, name)
    assert isinstance(screen, MessageScreen)
    assert screen.name == 'foo'


@raises(AttributeError)
def test_messageless_factory():
    """ Test case for message screen factory with invalid definition. """
    factory({})


def test_on_touch():
    """ Test case for on_touch event binding. """
    screen = create_message_screen('foo', 'foo')

    @screen.on_touch
    def callback():
        pass
    assert screen.callback == callback


def test_mouse_event():
    """ Test case for mouse event. """
    screen = create_message_screen('foo', 'foo')
    call = []

    def callback():
        call.append(True)
    screen.callback = callback
    screen.on_mouse_up(None)
    assert len(call) == 1


def test_draw():
    """ """
    screen = create_message_screen('foo', 'foo')
    screen.set_font_manager(FontManager())
    surface = SurfaceMock()
    screen.draw(surface)


def test_message_normalize():
    """ """
    pass


def test_message_line_normalize():
    """ """
    pass


