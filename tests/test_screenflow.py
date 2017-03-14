#!/usr/bin/python

""" Test suite for ScreenFlow class. """

from screenflow import ScreenFlow, NavigationException
from screenflow.font_manager import FontManager
from screenflow.constants import XML_TYPE, XML_NAME
from screenflow.screens import MessageScreen
from mocks.surface_mock import SurfaceMock
from mocks.screen_mock import ScreenMock
from pytest import raises
from os.path import join

# Mock surface used for created screenflow.
surface = SurfaceMock()


def test_add_screen():
    """ Test case for screen insertion. """
    name = 'foo'
    screen = ScreenMock(name)
    screenflow = ScreenFlow(surface)
    screenflow.add_screen(screen)
    assert screen.font_manager == screenflow._font_manager
    assert name in screenflow._screens.keys()
    assert screenflow._screens[name] == screen
    assert screenflow.foo == screen


def test_unknown_screen_access():
    """ Test case for unknown screen access. """
    screenflow = ScreenFlow(surface)
    with raises(AttributeError) as e:
        screen = screenflow.foo
        assert screen is not None


def test_get_current_screen():
    """ Test case for top stack access. """
    screenflow = ScreenFlow(surface)
    screen = ScreenMock('foo')
    screenflow._stack.append(screen)
    current = screenflow.get_current_screen()
    assert current == screen


def test_get_current_screen_empty_stack():
    """ Test case for empty stack access. """
    screenflow = ScreenFlow(surface)
    with raises(IndexError) as e:
        screenflow.get_current_screen()


def test_navigate_to():
    """ Test case for navigating to another screen. """
    screenflow = ScreenFlow(surface)
    foo = ScreenMock('foo')
    bar = ScreenMock('bar')
    screenflow._stack.append(foo)
    screenflow.navigate_to(bar)
    assert screenflow._state == ScreenFlow.IN_TRANSITION
    assert len(screenflow._stack) == 2
    assert screenflow._stack[0] == foo
    assert screenflow._stack[1] == bar


def test_navigate_back_error():
    """ Test case for navigating back error handling. """
    screenflow = ScreenFlow(surface)
    with raises(NavigationException) as e:
        screenflow.navigate_back()


def test_navigate_back():
    """ Test case for navigatixng back. """
    screenflow = ScreenFlow(surface)
    foo = ScreenMock('foo')
    bar = ScreenMock('bar')
    screenflow._stack.append(foo)
    screenflow._stack.append(bar)
    screenflow.navigate_back()
    assert screenflow._state == ScreenFlow.IN_TRANSITION
    assert len(screenflow._stack) == 1
    assert screenflow._stack[0] == foo


def test_main_loop():
    """ Test case for the main loop. """
    pass


def test_register_factory():
    """ Test case for screen factory registration. """
    screenflow = ScreenFlow(surface)

    def factory(metadata):
        pass
    name = 'foo'
    screenflow.register_factory(name, factory)
    assert name in screenflow._factories.keys()
    assert screenflow._factories[name] == factory


def test_register_factory_duplicate():
    """ Test case for screen factory duplicate registration. """
    screenflow = ScreenFlow(surface)
    name = 'foo'
    screenflow.register_factory(name, None)
    with raises(ValueError) as e:
        screenflow.register_factory(name, None)


def test_create_screen():
    """ Test case for create_screen method. """
    screenflow = ScreenFlow(surface)
    screendef = {}
    screendef[XML_TYPE] = 'message'
    screendef[XML_NAME] = 'foo'
    screendef['message'] = 'test'
    screen = screenflow.create_screen(screendef)
    assert isinstance(screen, MessageScreen)
    assert screen.name == 'foo'


def test_create_screen_not_valid_xml():
    """ Test case for creating screen without type. """
    screenflow = ScreenFlow(surface)
    with raises(AttributeError) as e:
        screenflow.create_screen({})


def test_create_unknown_type_screen():
    """ Test case for creating screen with unknown type. """
    screenflow = ScreenFlow(surface)
    with raises(ValueError) as e:
        screenflow.create_screen({XML_TYPE: 'foo'})


def check_xml_screenflow(file):
    """ Base test for XML screenflow loading. """
    screenflow = ScreenFlow(surface)
    screenflow.load_from_file(file)
    assert isinstance(screenflow.foo, MessageScreen)
    return screenflow


def test_load_from_file_single():
    """ Test case for XML file loading with one screen. """
    check_xml_screenflow('tests/resources/test_single_screenflow.xml')

# Path for XML test resources.
RESOURCES_PATH = 'tests/resources'


def test_load_from_file_multiple():
    """ Test case for XML file loading with multiple screen. """
    file = join(RESOURCES_PATH, 'test_multiple_screenflow.xml')
    screenflow = check_xml_screenflow(file)
    assert isinstance(screenflow.bar, MessageScreen)


def test_load_from_not_existing_file():
    """ Test case for XML file loading error handling (file not exists). """
    screenflow = ScreenFlow(surface)
    with raises(IOError) as e:
        screenflow.load_from_file('ghost_file.xml')


def test_load_from_file_without_root():
    """ Test case for XML file loading error handling (no root element). """
    file = join(RESOURCES_PATH, 'test_screenflow_without_root.xml')
    screenflow = ScreenFlow(surface)
    with raises(AttributeError) as e:
        screenflow.load_from_file(file)


def test_load_from_file_without_screen():
    """ Test case for XML file loading error handling (no screen element). """
    file = join(RESOURCES_PATH, 'test_screenflow_without_screen.xml')
    screenflow = ScreenFlow(surface)
    with raises(AttributeError) as e:
        screenflow.load_from_file(file)


def test_load_style():
    """ """
    pass


def test_load_style_from_not_existing_file():
    """ """
    pass
