#!/usr/bin/python

"""
    To be documented.
"""

import logging
import tinycss
from pygame.font import SysFont
from webcolors import hex_to_rgb, name_to_rgb

# Configure logger.
logging.basicConfig()
logger = logging.getLogger(__name__)


def get_color(value):
    """Simple factory method that takes a CSS color definition
    and transforms it into a valid RGB color tuple.

    :param value: CSS color value.
    :returns: Associated RGB color tuple.
    """
    if value[0] == '#':
        return hex_to_rgb(value)
    return name_to_rgb(value)


class StyleFactory(object):
    """To document.
    """

    def __init__(self):
        """ Default constructor. """
        self.declaration_parser = {}
        self.name_drawers = {}
        self.type_drawers = {}
        self.screenflow_drawer = Drawer()

    def create_screen_name_drawer(self, selector):
        """
        """
        screen_name = selector[1:]
        if screen_name not in self.name_drawers.keys():
            # TODO : retrieve screen type and ensure parent.
            self.name_drawers[screen_name] = Drawer(self.screenflow_drawer)
        return self.name_drawers[screen_name]

    def create_screen_type_drawer(self, selector):
        """
        """
        screen_type = selector[1:]
        if screen_type not in self.type_drawers.keys():
            self.type_drawers[screen_type] = Drawer(self.screenflow_drawer)
        return self.type_drawers[screen_type]

    def create_drawer(self, selector):
        """
        :param selector:
        :returns:
        """
        if selector[0] == '#':
            return self.create_screen_name_drawer(selector)
        elif selector[0] == '.':
            return self.create_screen_type_drawer(selector)
        return self.screenflow_drawer

    def evaluate(self, declaration, drawer):
        """
        """
        name = declaration.name
        if name not in self.declaration_parser.keys():
            # TODO : Warning
            pass
        else:
            value = declaration.value.as_css()
            self.declaration_parser(declaration, drawer)

    def load(self, file):
        """Loads and parses the given CSS file.

        :param file: CSS file to load.
        """
        parser = tinycss.make_parser('fonts3')
        stylesheet = parser.parse_stylesheet_file(file)
        for ruleset in stylesheet.rules:
            selector = ruleset.selector.as_css()
            drawer = self.create_drawer(selector)
            for declaration in ruleset.declarations:
                evaluate_declaration(declaration, drawer)

    def get_drawer(self, screen):
        """
        :param screen:
        :returns:
        """
        if screen.name in self.name_drawers.keys():
            return self.name_drawers[screen.name]
        elif screen.type in self.type_drawers.keys():
            return self.type_drawers[screen.type]
        return self.screenflow_drawer

    def get_style(self, screen):
        """
        :param screen:
        :returns:
        """
        return None

    def get_font_styles(self, screen):
        """
        :param screen:
        :returns:
        """
        return (None, None)
