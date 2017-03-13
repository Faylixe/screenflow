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

from screenflow.constants import WHITE

from pygame import Surface
from pygame.mouse import get_pos as mouse_position
from pygame.event import get as events
from pygame.constants import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP


class Screen(object):
    """ Base class for screen object. """

    def __init__(self, name, background_color=WHITE):
        """Default constructor.

        :param name: Name of this screen.
        :param background_color: Default background color.
        """
        self.name = name
        self.padding = (0, 0)
        self._surface_factory = None
        self._font_manager = None
        self.background_color = background_color

    @property
    def font_manager(self):
        """
        :returns:
        """
        if self._font_manager is None:
            raise AttributeError('Font manager not initialized')
        return self._font_manager

    @font_manager.setter
    def font_manager(self, delegate):
        """
        :param delegate:
        """
        self._font_manager = delegate

    @property
    def surface_factory(self):
        """
        :returns:
        """
        if self._surface_factory is None:
            def pygame_factory(size):
                return Surface(size)
            self._surface_factory = pygame_factory
        return self._surface_factory

    @surface_factory.setter
    def surface_factory(self, factory):
        """
        :param factory:
        """
        self._surface_factory = factory

    def create_surface(self, size):
        """
        :param size:
        :returns:
        """
        return self.surface_factory(size)

    def get_surface_size(self, surface):
        """ Surface
        """
        return surface.get_size()

    def process_event(self):
        """ To doc
        """
        for event in events():
            if event.type == MOUSEBUTTONDOWN:
                self.on_mouse_down(mouse_position())
            elif event.type == MOUSEBUTTONUP:
                self.on_mouse_up(mouse_position())
            elif event.type == QUIT:
                return False
        return True

    def generate_preview(self, size):
        """
        :param size:
        :returns:
        """
        surface = Surface(size)
        self.draw(surface)
        return surface

    def draw_background(self, surface):
        """Draw screen background by filling it with the background color.

        :param surface: Surface to draw background into.
        """
        surface.fill(self.background_color)

    def draw(self, surface):
        """
        :param surface: Surface to draw screen into.
        """
        self.draw_background(surface)

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
