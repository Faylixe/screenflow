#!/usr/bin/python

"""
"""


class Drawer(object):
    """
    """

    def __init__(self):
        """
        """
        self._font_manager = None
        self._style = None
        self._primary_style = None
        self._secondary_style = None
        self._button_style = None

    def configure_styles(self, style_factory):
        """Configures screen associated style attributes using the given style_factory.
        Client should override this methods in order to support custom style.

        :param style_factory: Style factory instance to use for configuring.
        """
        self._style = style_factory.get_style(self)
        fonts = style_factory.get_font_styles(self)
        self._primary_style = fonts[0]
        self._secondary_style = fonts[1]
        self._button_style = style_factory.get_button_style(self)

    def create_surface(self, size):
        """
        :param size:
        :returns:
        """
        raise NotImplementedError()

    def fill_surface(self, surface, color):
        """
        :param surface:
        :param color:
        """
        raise NotImplementedError()

    def blit_surface(self, destination, source, position):
        """
        :param destination:
        :param source:
        :param position:
        """
        raise NotImplementError()

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
        surface.fill(self._button_style.background_color)
        text = self._get_text(label, self._button_style)
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

    def get_surface_drawable_size(self, surface):
        """ Surface

        :param surface:
        """
        original_size = surface.get_size()
        padded_size = [original_size[0], original_size[1]]
        padded_size[0] -= self._style.padding * 2
        padded_size[1] -= self._style.padding * 2
        return padded_size
