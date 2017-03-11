#!/usr/bin/python

""" Simple test suite for Select screen associated classes. """

from screenflow.constants import XML_NAME
from screenflow.font_manager import FontManager, FontHolder
from screenflow.screens import SelectScreen
from screenflow.screens.select_screen import factory, XML_LABEL, XML_OPTION
from tests.mocks.surface_mock import SurfaceMock
from pytest import raises

# Default options used for testing.
DEFAULT_OPTIONS = ['Yes', 'No']


def create_select_screen(name, label, options=DEFAULT_OPTIONS):
    """Simple factory method that creates
    a select screen using the given name, label and options.

    :param name: Name of the created screen.
    :param label: Label of the created screen.
    :param options: Options of the created screen.
    """
    screen_def = {}
    screen_def[XML_NAME] = name
    screen_def[XML_LABEL] = label
    screen_def[XML_OPTION] = options
    screen = factory(screen_def)
    return screen


def test_factory():
    """ Test case for select screen factory. """
    name = 'foo'
    screen = create_select_screen(name, name)
    assert isinstance(screen, SelectScreen)
    assert screen.name == name


def test_labelless_factory():
    """ Test case for select screen factory with invalid definition. """
    screen_def = {}
    screen_def[XML_OPTION] = DEFAULT_OPTIONS
    with raises(AttributeError) as e:
        factory(screen_def)


def test_optionless_factory():
    """ Test case for select screen factory with invalid definition. """
    screen_def = {}
    screen_def[XML_LABEL] = 'foo'
    with raises(AttributeError) as e:
        factory(screen_def)
