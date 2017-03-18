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
        raise NotImplementedError()

    def _get_font(self, style):
        """
        :param style:
        :returns:
        """
        return self.font_manager.get(style.name, style.size)

    def get_text_surface(self, text, style):
        """Creates a text surface for the given text with primary font style.

        :param text: Text to render.
        :param style: Font style to use for text rendering.
        :returns: Created text surface.
        """
        font = self._get_font(style)
        return font.render(text, 0, style.color)

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
