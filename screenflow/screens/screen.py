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

    def __init__(self, name, type):
        """Default constructor.

        :param name: Name of this screen.
        :param type: Type of this screen.
        """
        self.name = name
        self.type = type
        self._surface_factory = None
        self._font_manager = None
        self._style = None
        self._primary_style = None
        self._secondary_style = None

    def configure_styles(self, style_factory):
        """
        :param style_factory:
        """
        self._style = style_factory.get_style(self)
        fonts = style_factory.get_font_styles(self)
        self._primary_style = fonts[0]
        self._secondary_style = fonts[1]

    @property
    def font_manager(self):
        """
        :returns: Font manager instance if any, raise a exception otherwise.
        """
        if self._font_manager is None:
            raise AttributeError('Font manager not initialized')
        return self._font_manager

    @font_manager.setter
    def font_manager(self, font_manager):
        """
        :param font_manager:
        """
        self._font_manager = font_manager

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

    def draw_background(self, surface):
        """Draw a background into the given surface.

        :param surface: Surface to draw background into.
        """
        # TODO : Consider using background image variant ?
        surface.fill(self._style.background_color)

    def __get_font(self, style):
        """
        :param style:
        :returns:
        """
        return self.font_manager.get(style.name, style.size)

    def __get_text(self, text, style):
        """Creates a text surface for the given text with primary font style.

        :param text: Text to render.
        :param style: Font style to use for text rendering.
        :returns: Created text surface.
        """
        font = self.__get_font(style)
        return font.render(text, 0, style.color)

    def primary_size(self, text):
        """
        :param text:
        :returns:
        """
        return self.__get_font(self._primary_style).size(text)

    def secondary_size(self, text):
        """
        :param text:
        :returns:
        """
        return self.__get_font(self._secondary_style).size(text)

    def draw_primary_text(self, text):
        """Creates a text surface for the given text with primary font style.

        :param text: Text to render.
        :returns: Created text surface.
        """
        return self.__get_text(text, self._primary_style)

    def draw_secondary_text(self, text):
        """Creates a text surface for the given text  with secondary font style.

        :param text: Text to render.
        :returns: Created text surface.
        """
        return self.__get_text(text, self._secondary_style)

    def draw_button(self, label, size):
        """
        :param label:
        :param size:
        :returns:
        """
        surface = self.create_surface(size)
        # surface.fill(self.__button_style.background_color)
        # text = self.__get_text(self, label, self.__button_style)
        self.draw_centered(surface, text)
        return surface

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

    def get_surface_drawable_size(self, surface):
        """ Surface

        :param surface:
        """
        return surface.get_size()

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
