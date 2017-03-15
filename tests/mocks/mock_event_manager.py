#!/usr/bin/python

""" Mock implementation for EventManager. """

from screenflow.graphics.event_manager import EventManager

# Event type enumeration.
QUIT = 1
MOUSEUP = 2
MOUSEDOWN = 3


class MockEventManager(EventManager):
    """ Mock implementation of EventManager class. """

    def __init__(self):
        """ Default constructor. """
        EventManager.__init__(self)
        self._mouse_position = (0, 0)
        self._event_queue = []

    def get_events(self):
        """Events getter method.

        :returns: Collection of event captured.
        """
        return self._event_queue

    def set_mouse_position(self, position):
        """Mock specific method, for setting current mouse position.

        :param position: Current position of the mouse to set.
        """
        self._mouse_position = position

    def get_mouse_position(self):
        """Mouse position getter.

        :returns: Current position of the mouse cursor.
        """
        raise self._mouse_position

    def is_quit(self, event):
        """Indicates if the given event denotes a quit event.

        :returns: True if the event is a quit, False otherwise.
        """
        return event == QUIT

    def is_mouse_up(self, event):
        """Indicates if the given event denotes a mouse button up event.

        :returns: True if the event is a mouse button up, False otherwise.
        """
        return event == MOUSEUP

    def is_mouse_down(self, event):
        """Indicates if the given event denotes a mouse button down event.

        :returns: True if the event is a mouse button down, False otherwise.
        """
        return event == MOUSEDOWN
