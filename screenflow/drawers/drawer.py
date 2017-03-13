#!/usr/bin/python

"""
"""


class Drawer(object):
    """
    """

    def __init__(self, parent):
        """
        :param parent:
        """
        self.cell_style = Style(parent.cell_style)

    def draw_background(self, surface):
        """Background drawing method.

        :param surface: Surface to draw background into.
        """
        surface.fill(self.background_color)

    def draw_text(self, text, color=None):
        """Text drawing method.

        :param text: Text to draw.
        """
        if color is None:
            color = self.text_color
        return self.font.render(text, color)

    def draw_button(self, surface, label):
        """Button drawing method.

        :param surface: Surface to draw button into.
        :param label: Button label.
        """
        surface.fill(self.cell_style.background_color)
        label_surface = self.draw_text(label, self.cell_style.text_color)