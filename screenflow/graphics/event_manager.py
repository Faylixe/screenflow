#!/usr/bin/python

""" An EventManager is a simple gateway for accessing I/O event. """


class EventManager(object):
    """ EventManager gateway class. """

    def get_events(self):
        """Events getter method.

        :returns: Collection of event captured.
        """
        raise NotImplementedError()

    def get_mouse_position(self):
        """Mouse position getter.

        :returns: Current position of the mouse cursor.
        """
        raise NotImplementedError()

    def is_quit(self, event):
        """Indicates if the given event denotes a quit event.

        :returns: True if the event is a quit, False otherwise.
        """
        raise NotImplementedError()

    def is_mouse_up(self, event):
        """Indicates if the given event denotes a mouse button up event.

        :returns: True if the event is a mouse button up, False otherwise.
        """
        raise NotImplementedError()

    def is_mouse_down(self, event):
        """Indicates if the given event denotes a mouse button down event.

        :returns: True if the event is a mouse button down, False otherwise.
        """
        raise NotImplementedError()
