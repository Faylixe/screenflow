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

from screenflow.constants import WHITE, VERTICAL, HORIZONTAL

from pygame import Surface
from pygame.mouse import get_pos as mouse_position
from pygame.event import get as events
from pygame.constants import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP


def find(collection, sizer, axis):
    """
    """
    best = max(collection, key=lambda x: sizer(x)[axis])
    return sizer(best)[axis]


def get_longest(collection, sizer):
    """
    :param collection:
    :param sizer:
    :returns:
    """
    return find(collection, sizer, 0)


def get_highest(collection, sizer):
    """
    :param collection:
    :param sizer:
    :returns:
    """
    return find(collection, sizer, 1)


class Oriented(object):
    """
    """

    def __init__(self, orientation,  **kwargs):
        """
        """
        self.orientation = orientation

    def isVertical(self):
        """
        """
        return self.orientation == VERTICAL

    def isHorizontal(self):
        """
        """
        return self.orientation == HORIZONTAL


class Screen(object):
    """ Base class for screen object. """

    def __init__(self, name, background_color=WHITE):
        """Default constructor.

        :param name: Name of this screen.
        :param background_color: Default background color.
        """
        self.name = name
        self.padding = (0, 0)
        self.__surface_factory = None
        self.__font_manager = None
        self.__style = None
        self.__primary_style = None
        self.__secondary_style = None
        self.__button_style = None
        self.background_color = background_color

    def draw_background(self, surface):
        """
        :param surface:
        """
        surface.fill(self.style.background_color)

    def draw_primary_text(self, text):
        """
        """
        return None

    def draw_secondary_text(self, text):
        """
        """
        return None

    def draw_button(self, label, size):
        """
        """
        surface = self.create_surface(size)
        # TODO : Find button style background color.
        surface.fill(self.button_style.background_color)
        # TODO : Find button style font
        # TODO : Draw text.
        return surface

    def get_surface_drawable_size(self, surface):
        """ Surface

        :param surface:
        """
        return surface.get_size()

    @property
    def drawer(self):
        """
        """
        if self.__drawer is None:
            raise AttributeError('')

    @property
    def surface_factory(self):
        """
        :returns:
        """
        if self.__surface_factory is None:
            def pygame_factory(size):
                return Surface(size)
            self.__surface_factory = pygame_factory
        return self.__surface_factory

    @surface_factory.setter
    def surface_factory(self, factory):
        """
        :param factory:
        """
        self.__surface_factory = factory

    def create_surface(self, size):
        """
        :param size:
        :returns:
        """
        return self.surface_factory(size)

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

    def draw_centered(self, surface, delegate):
        """
        """
        surface_size = surface.get_size()
        delegate_surface_size = delegate.get_size()
        x = (surface_size[0] - delegate_surface_size[0]) / 2
        y = (surface_size[1] - delegate_surface_size[1]) / 2
        surface.blit(delegate, (x, y))

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
