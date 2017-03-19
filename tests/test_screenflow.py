#!/usr/bin/python

""" Test suite for ScreenFlow class. """

from screenflow import ScreenFlow, NavigationException
from screenflow.css.font_manager import FontManager
from screenflow.constants import XML_TYPE, XML_NAME
from screenflow.screens import MessageScreen
from mocks.mock_surface import MockSurface
from mocks.mock_screen import MockScreen
from pytest import raises, fixture
from os.path import join


@fixture
def surface():
    """ Fixture for surface parameter. """
    return MockSurface()


def test_add_screen(surface):
    """ Test case for screen insertion. """
    name = 'foo'
    screen = MockScreen(name)
    screenflow = ScreenFlow(surface)
    screenflow.add_screen(screen)
    assert screen.font_manager == screenflow._font_manager
    assert name in screenflow._screens.keys()
    assert screenflow._screens[name] == screen
    assert screenflow.foo == screen


def test_unknown_screen_access(surface):
    """ Test case for unknown screen access. """
    screenflow = ScreenFlow(surface)
    with raises(AttributeError) as e:
        screen = screenflow.foo
        assert screen is not None


def test_get_current_screen(surface):
    """ Test case for top stack access. """
    screenflow = ScreenFlow(surface)
    screen = MockScreen('foo')
    screenflow._stack.append(screen)
    current = screenflow.get_current_screen()
    assert current == screen


def test_get_current_screen_empty_stack(surface):
    """ Test case for empty stack access. """
    screenflow = ScreenFlow(surface)
    with raises(IndexError) as e:
        screenflow.get_current_screen()


def test_navigate_to(surface):
    """ Test case for navigating to another screen. """
    screenflow = ScreenFlow(surface)
    foo = MockScreen('foo')
    bar = MockScreen('bar')
    screenflow._stack.append(foo)
    screenflow.navigate_to(bar)
    assert screenflow._state == ScreenFlow.IN_TRANSITION
    assert len(screenflow._stack) == 2
    assert screenflow._stack[0] == foo
    assert screenflow._stack[1] == bar


def test_navigate_back_error(surface):
    """ Test case for navigating back error handling. """
    screenflow = ScreenFlow(surface)
    with raises(NavigationException) as e:
        screenflow.navigate_back()


def test_navigate_back(surface):
    """ Test case for navigatixng back. """
    screenflow = ScreenFlow(surface)
    foo = MockScreen('foo')
    bar = MockScreen('bar')
    screenflow._stack.append(foo)
    screenflow._stack.append(bar)
    screenflow.navigate_back()
    assert screenflow._state == ScreenFlow.IN_TRANSITION
    assert len(screenflow._stack) == 1
    assert screenflow._stack[0] == foo


def test_main_loop():
    """ Test case for the main loop. """
    pass


def test_register_factory(surface):
    """ Test case for screen factory registration. """
    screenflow = ScreenFlow(surface)

    def factory(metadata):
        pass
    name = 'foo'
    screenflow.register_factory(name, factory)
    assert name in screenflow._factories.keys()
    assert screenflow._factories[name] == factory


def test_register_factory_duplicate(surface):
    """ Test case for screen factory duplicate registration. """
    screenflow = ScreenFlow(surface)
    name = 'foo'
    screenflow.register_factory(name, None)
    with raises(ValueError) as e:
        screenflow.register_factory(name, None)


def test_create_screen(surface):
    """ Test case for create_screen method. """
    screenflow = ScreenFlow(surface)
    screendef = {}
    screendef[XML_TYPE] = 'message'
    screendef[XML_NAME] = 'foo'
    screendef['message'] = 'test'
    screen = screenflow.create_screen(screendef)
    assert isinstance(screen, MessageScreen)
    assert screen.name == 'foo'


def test_create_screen_not_valid_xml(surface):
    """ Test case for creating screen without type. """
    screenflow = ScreenFlow(surface)
    with raises(AttributeError) as e:
        screenflow.create_screen({})


def test_create_unknown_type_screen(surface):
    """ Test case for creating screen with unknown type. """
    screenflow = ScreenFlow(surface)
    with raises(ValueError) as e:
        screenflow.create_screen({XML_TYPE: 'foo'})


def check_xml_screenflow(surface, file):
    """ Base test for XML screenflow loading. """
    screenflow = ScreenFlow(surface)
    screenflow.load_from_file(file)
    assert isinstance(screenflow.foo, MessageScreen)
    return screenflow


def test_load_from_file_single(surface):
    """ Test case for XML file loading with one screen. """
    check_xml_screenflow(surface, 'tests/resources/test_single_screenflow.xml')

# Path for XML test resources.
RESOURCES_PATH = 'tests/resources'


def test_load_from_file_multiple(surface):
    """ Test case for XML file loading with multiple screen. """
    file = join(RESOURCES_PATH, 'test_multiple_screenflow.xml')
    screenflow = check_xml_screenflow(surface, file)
    assert isinstance(screenflow.bar, MessageScreen)


def test_load_from_not_existing_file(surface):
    """ Test case for XML file loading error handling (file not exists). """
    screenflow = ScreenFlow(surface)
    with raises(IOError) as e:
        screenflow.load_from_file('ghost_file.xml')


def test_load_from_file_without_root(surface):
    """ Test case for XML file loading error handling (no root element). """
    file = join(RESOURCES_PATH, 'test_screenflow_without_root.xml')
    screenflow = ScreenFlow(surface)
    with raises(AttributeError) as e:
        screenflow.load_from_file(file)


def test_load_from_file_without_screen(surface):
    """ Test case for XML file loading error handling (no screen element). """
    file = join(RESOURCES_PATH, 'test_screenflow_without_screen.xml')
    screenflow = ScreenFlow(surface)
    with raises(AttributeError) as e:
        screenflow.load_from_file(file)


def test_load_style():
    """ Test case for load style method. """
    pass


def test_load_style_from_not_existing_file():
    """ Test case for load style method with not existing file. """
    pass
