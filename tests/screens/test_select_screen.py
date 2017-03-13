#!/usr/bin/python

""" Simple test suite for Select screen associated classes. """

from screenflow.constants import XML_NAME
from screenflow.font_manager import FontManager, FontHolder
from screenflow.screens import SelectScreen
from screenflow.screens.message_based_screen import XML_MESSAGE
from screenflow.screens.select_screen import factory, XML_OPTION
from tests.mocks.surface_mock import SurfaceMock
from pytest import raises

# Default name for testing.
DEFAULT_NAME = 'select'

# Default options used for testing.
DEFAULT_OPTIONS = ['Yes', 'No']

# Default label used for testing.
DEFAULT_LABEL = 'Yes or no ?'


def create_select_screen(name=DEFAULT_NAME, label=DEFAULT_LABEL, options=DEFAULT_OPTIONS):
    """Simple factory method that creates
    a select screen using the given name, label and options.

    :param name: Name of the created screen.
    :param label: Label of the created screen.
    :param options: Options of the created screen.
    """
    screen_def = {}
    screen_def[XML_NAME] = name
    screen_def[XML_MESSAGE] = label
    screen_def[XML_OPTION] = options
    screen = factory(screen_def)
    return screen


def test_factory():
    """ Test case for select screen factory. """
    screen = create_select_screen()
    assert isinstance(screen, SelectScreen)
    assert screen.name == DEFAULT_NAME


def test_labelless_factory():
    """ Test case for select screen factory with invalid definition. """
    screen_def = {}
    screen_def[XML_OPTION] = DEFAULT_OPTIONS
    with raises(AttributeError) as e:
        factory(screen_def)


def test_optionless_factory():
    """ Test case for select screen factory with invalid definition. """
    screen_def = {}
    screen_def[XML_MESSAGE] = DEFAULT_LABEL
    with raises(AttributeError) as e:
        factory(screen_def)


def test_optioninvalid_factory():
    """ Test case for select screen factory with invalid definition. """
    screen_def = {}
    screen_def[XML_MESSAGE] = DEFAULT_LABEL
    screen_def[XML_OPTION] = 1
    with raises(AttributeError) as e:
        factory(screen_def)


def test_on_select():
    """ Test case for on_select event binding. """
    screen = create_select_screen()

    @screen.on_select
    def callback(option):
        pass
    assert screen.callback == callback


def test_mouse_event():
    """ Test case for mouse event. """
    pass


def test_draw():
    """ Test case for select screen drawing method. """
    pass
