#!/usr/bin/python

""" Simple test suite for EventManager class. """

import pytest
from tests.mocks.mock_event_manager import MockEventManager


class TestEventManager(object):
    """ Test suite for EventManager class. """

    @pytest.fixture
    def event_manager(self):
        return MockEventManager()

    def test_get_events(self, event_manager):
        """ """
        events = event_manager.get_events()
        assert len(events) == 0

    def test_get_mouse_position(self, event_manager):
        """ """
        pass

    def test_is_quit(self, event_manager):
        """ """
        pass

    def test_is_mouse_up(self, event_manager):
        """ """
        pass

    def test_is_mouse_down(self, event_manager):
        """ """
        pass
