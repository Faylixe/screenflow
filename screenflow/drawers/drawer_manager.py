#!/usr/bin/python

""" 

    Supported CSS rules
    -------------------

    Selector
    ~~~~~~~~~~~~~

    There is three top level selector (TLS) that can be used :

    - screenflow
    - #screen_name
    - .screen_type

    General selector properties
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Here are the rules supported by any **TLS** selector
    with their default values :

    .. code-block:: css

        tls {
            background-color: white;
            padding: 20;
        }

    Component font selector
    ~~~~~~~~~~~~~~~~~~~~~~~

    For any top level selector, we can add specific rule
    for **primary** as **secondary** font to be used for
    the target componenents :

    .. code-block:: css

        tls primary {
            color: black;
            font-size: 20;
            font-familiy: Arial;
        }

    Component button selector
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    For any top level selector, we can add specific rule
    for **button** design to be used for the target componenents :

    .. code-block:: css

        tls button {
            background-color: black;
            padding: 20;
            color: white;
            font-size: 20;
            font-familiy: Arial;
        }
"""

import logging
import tinycss
from pygame.font import SysFont
from webcolors import hex_to_rgb, name_to_rgb

# Configure logger.
logging.basicConfig()
logger = logging.getLogger(__name__)


def get_color(value):
    """
    :param value:
    :returns:
    """
    if value[0] == '#':
        return hex_to_rgb(value)
    return name_to_rgb(value)


class DrawerManager(object):
    """To document.
    """

    def __init__(self):
        """ Default constructor. """
        self.declaration_parser = {}
        self.name_drawers = {}
        self.type_drawers = {}
        self.screenflow_drawer = Drawer()
        self.screenflow_drawer.background_color = (255, 255, 255)
        self.screenflow_drawer.text_color = (0, 0, 0)
        self.screenflow_drawer.padding = 20
        self.screenflow_drawer.cell_padding = 20

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
        """
        :param file:
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
