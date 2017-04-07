#!/usr/bin/env python
# coding: utf-8

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
    :param collection:
    :param sizer:
    :param axis:
    :returns:
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
        """Configures screen associated style attributes using the given style_factory.
        Client should override this methods in order to support custom style.

        :param style_factory: Style factory instance to use for configuring.
        """
        self._style = style_factory.get_style(self)
        fonts = style_factory.get_font_styles(self)
        self._primary_style = fonts[0]
        self._secondary_style = fonts[1]

    @property
    def font_manager(self):
        """Property getter for font manager attribute. If font manager instance is not
        settled, then an exception will be raised when trying to access.

        :returns: Font manager instance if any, raise a exception otherwise.
        """
        if self._font_manager is None:
            raise AttributeError('Font manager not initialized')
        return self._font_manager

    @font_manager.setter
    def font_manager(self, font_manager):
        """Property setter for font manager attribute.

        :param font_manager: Font manager instance to use.
        """
        self._font_manager = font_manager

    @property
    def surface_factory(self):
        """Property getter for surface factory attribute.
        If such factory is not settled, then a default one
        that creates pygame.Surface will be used.

        :returns: Surface factory instance to use.
        """
        if self._surface_factory is None:
            def pygame_factory(size):
                return Surface(size)
            self._surface_factory = pygame_factory
        return self._surface_factory

    @surface_factory.setter
    def surface_factory(self, surface_factory):
        """Property setter for surface factory attribute.

        :param surface_factory: Surface factory instance to use.
        """
        self._surface_factory = surface_factory

    def draw_background(self, surface):
        """Draw a background into the given surface.

        :param surface: Surface to draw background into.
        """
        # TODO : Consider using background image variant ?
        surface.fill(self._style.background_color)

    def _get_font(self, style):
        """
        :param style:
        :returns:
        """
        return self.font_manager.get(style.name, style.size)

    def _get_text(self, text, style):
        """Creates a text surface for the given text with primary font style.

        :param text: Text to render.
        :param style: Font style to use for text rendering.
        :returns: Created text surface.
        """
        font = self._get_font(style)
        return font.render(text, 0, style.color)

    def primary_size(self, text):
        """
        :param text:
        :returns:
        """
        return self._get_font(self._primary_style).size(text)

    def secondary_size(self, text):
        """
        :param text:
        :returns:
        """
        return self._get_font(self._secondary_style).size(text)

    def draw_primary_text(self, text):
        """Creates a text surface for the given text with primary font style.

        :param text: Text to render.
        :returns: Created text surface.
        """
        return self._get_text(text, self._primary_style)

    def draw_secondary_text(self, text):
        """Creates a text surface for the given text  with secondary font style.

        :param text: Text to render.
        :returns: Created text surface.
        """
        return self._get_text(text, self._secondary_style)

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
        original_size = surface.get_size()
        padded_size = [original_size[0], original_size[1]]
        padded_size[0] -= self._style.padding * 2
        padded_size[1] -= self._style.padding * 2
        return padded_size

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
