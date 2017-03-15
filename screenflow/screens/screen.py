#!/usr/bin/python

"""

    Screen
    ======

    A **Screen** is a basic unit which is manipulated by a **Screenflow**.

    Rendering
    ---------

    Text rendering
    ~~~~~~~~~~~~~~

    In order to draw text, a **Screen** use a **FontManager**, which manages.

    Background
    ~~~~~~~~~~

    Event handling
    --------------

"""

from screenflow.constants import VERTICAL, HORIZONTAL


class Oriented(object):
    """ Simple class that provides orientation information. """

    def __init__(self, orientation):
        """ Default constructor.

        :param orientation: Orientation attribute.
        """
        self._orientation = orientation

    def isVertical(self):
        """Indicates if this orientation is vertical.

        :returns: True if this orientation is vertical, False otherwise.
        """
        return self._orientation == VERTICAL

    def isHorizontal(self):
        """Indicates if this orientation is horizontal.

        :returns: True if this orientation is horizontal, False otherwise.
        """
        return self._orientation == HORIZONTAL


class Screen(Drawer):
    """ Base class for screen object. """

    def __init__(self, name, type):
        """Default constructor.

        :param name: Name of this screen.
        :param type: Type of this screen.
        """
        Drawer.__init__(self)
        self.name = name
        self.type = type
        self._drawer = None
        self._event_manager = None

    @property
    def drawer(self):
        """
        """
        if self._drawer is None:
            raise AttributeError('Drawer not configured')
        return self._drawer

    @drawer.setter
    def drawer(self, drawer):
        """
        """
        self._drawer = drawer

    @property
    def event_manager(self):
        """
        """
        if self._event_manager is None:
            raise AttributeError('Event provider not configured')
        return self._event_manager

    @event_manager.setter
    def event_manager(self, event_manager):
        """
        """
        self._event_manager = event_manager

    def draw(self, surface):
        """
        :param surface: Surface to draw screen into.
        """
        self.drawer.draw_background(surface)

    def process_event(self):
        """ To doc
        :returns:
        """
        for event in self._event_manager.get_events():
            if self._event_manager.is_mouse_down(event):
                self.on_mouse_down(mouse_position())
            elif self._event_manager.is_mouse_up(event):
                self.on_mouse_up(mouse_position())
            elif self._event_manager.is_quit(event):
                return False
        return True

    def generate_preview(self, size):
        """
        :param size:
        :returns:
        """
        surface = self.drawer.create_surface(size)
        self.draw(surface)
        return surface

    def on_screen_activated(self):
        """ Callback method for screen activation pre processing. """
        pass

    def on_mouse_down(self, position):
        """
        :param position:
        """
        pass

    def on_mouse_up(self, position):
        """
        :param position:
        """
        pass
