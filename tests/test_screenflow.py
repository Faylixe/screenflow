#!/usr/bin/python

""" Test suite for ScreenFlow class. """

from screenflow import ScreenFlow, NavigationException
from screenflow.constants import XML_TYPE, XML_NAME
from screenflow.screens import MessageScreen
from mocks.surface_mock import SurfaceMock, DEFAULT_SURFACE_SIZE
from mocks.screen_mock import ScreenMock
from nose.tools import raises

def test_add_screen():
    """ Test case for screen insertion. """
    name = 'foo'
    screen = ScreenMock(name)
    screenflow = ScreenFlow()
    screenflow.add_screen(screen)
    assert screen.font_manager == screenflow
    assert name in screenflow.screens.keys()
    assert screenflow.screens[name] == screen
    assert screenflow.foo == screen

def test_get_current_screen():
    """ Test case for top stack access. """
    screenflow = ScreenFlow()
    screen = ScreenMock('foo')
    screenflow.stack.append(screen)
    current = screenflow.get_current_screen()
    assert current == screen

@raises(IndexError)
def test_get_current_screen_empty_stack():
    """ Test case for empty stack access. """
    screenflow = ScreenFlow()
    screenflow.get_current_screen()

def test_navigate_to():
    """ Test case for navigating to another screen. """
    screenflow = ScreenFlow()
    foo = ScreenMock('foo')
    bar = ScreenMock('bar')
    screenflow.stack.append(foo)
    screenflow.navigate_to(bar)
    assert screenflow.state == ScreenFlow.IN_TRANSITION
    assert len(screenflow.stack) == 2
    assert screenflow.stack[0] == foo
    assert screenflow.stack[1] == bar

@raises(NavigationException)
def test_navigate_back_error():
    """ Test case for navigating back error handling. """
    screenflow = ScreenFlow()
    screenflow.navigate_back()

def test_navigate_back():
    """ Test case for navigating back. """
    screenflow = ScreenFlow()
    foo = ScreenMock('foo')
    bar = ScreenMock('bar')
    screenflow.stack.append(foo)
    screenflow.stack.append(bar)
    screenflow.navigate_back()
    assert screenflow.state == ScreenFlow.IN_TRANSITION
    assert len(screenflow.stack) == 1
    assert screenflow.stack[0] == foo

def test_main_loop():
    """ Test case for the main loop. """
    pass

def test_register_factory():
    """ Test case for screen factory registration. """
    screenflow = ScreenFlow()
    def factory(metadata):
        pass
    name = 'foo'
    screenflow.register_factory(name, factory)
    assert name in screenflow.factories.keys()
    assert screenflow.factories[name] == factory

@raises(ValueError)
def test_register_factory_duplicate():
    """ Test case for screen factory duplicate registration. """
    screenflow = ScreenFlow()
    name = 'foo'
    screenflow.register_factory(name, None)
    screenflow.register_factory(name, None)

def test_create_screen():
    """ Test case for create_screen method. """
    screenflow = ScreenFlow()
    screendef = {}
    screendef[XML_TYPE] = 'message'
    screendef[XML_NAME] = 'foo'
    screendef['message'] = 'test'
    screen = screenflow.create_screen(screendef)
    assert isinstance(screen, MessageScreen)
    assert screen.message == 'test'
    assert screen.name == 'foo'

@raises(AttributeError)
def test_create_screen_not_valid_xml():
    """ Test case for creating screen without type. """
    screenflow = ScreenFlow()
    screenflow.create_screen({})

@raises(ValueError)
def test_create_unknown_type_screen():
    """ Test case for creating screen with unknown type. """
    screenflow = ScreenFlow()
    screenflow.create_screen({XML_TYPE: 'foo'})

def test_load_from_file():
    """ Test case for XML file loading. """
    screenflow = ScreenFlow()
    screenflow.load_from_file('tests/resources/test_screenflow.xml')
    assert isinstance(screenflow.foo, MessageScreen)
    #TODO : Check stack ?

@raises(IOError)
def test_load_from_not_existing_file():
    """ Test case for XML file loading error handling (file not exists). """
    screenflow = ScreenFlow()
    screenflow.load_from_file('ghost_file.xml')

@raises(AttributeError)
def test_load_from_file_without_root():
    """ Test case for XML file loading error handling (no root element). """
    screenflow = ScreenFlow()
    screenflow.load_from_file('tests/resources/test_screenflow_without_root.xml')

@raises(AttributeError)
def test_load_from_file_without_screen():
    """ Test case for XML file loading error handling (no screen element). """
    screenflow = ScreenFlow()
    screenflow.load_from_file('tests/resources/test_screenflow_without_screen.xml')