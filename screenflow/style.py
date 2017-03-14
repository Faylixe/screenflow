#!/usr/bin/python

"""
    CSS engine
    ==========

    Screenflow embeds a CSS parsing engine for defining screen style
    properties.

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


class GenericStyle(object):
    """
    """

    def __init__(self, parent):
        """
        """
        self.__background_color = None
        self.__padding = None

    @property
    def background_color(self):
        """
        """
        if self.__background_color is None:
            return self.parent.background_color
        return self.__background_color

    @background_color.setter
    def background_color(self, background_color):
        """
        """
        self.__background_color = background_color

    @property
    def padding(self):
        """
        """
        if self_._padding is None:
            return self.parent.padding
        return self.__padding

    @padding.setter
    def padding(self, padding):
        """
        """
        self.__padding = padding

    def draw_primary_text(self, text):
        """
        """
        return


class FontStyle(object):
    """
    """

    def __init__(self, parent):
        """Default constructor.

        :param parent:
        """
        self.parent = parent
        self.__size = None
        self.__name = None
        self.__color = None

    @property
    def color():
        """Property getter for color attribute.

        :returns: Text color to use.
        """
        if self.__color is None:
            return self.parent.color
        return self.__color

    @xolor.setter
    def color(self, color):
        """Property setter for color attribute.

        :param color: Text color to use.
        """
        self.__color = color

    @property
    def name():
        """Property getter for color attribute.

        :returns: Text color to use.
        """
        if self.__name is None:
            return self.parent.name
        return self.__name

    @name.setter
    def name(self, name):
        """Property setter for name attribute.

        :param name: Text name to use.
        """
        self.__name = name

    @property
    def size():
        """Property getter for size attribute.

        :returns: Text size to use.
        """
        if self.__size is None:
            return self.parent.size
        return self.__size

    @size.setter
    def size(self, size):
        """Property setter for size attribute.

        :param size: Text size to use.
        """
        self.__size = size


class ButtonStyle(FontStyle, GenericStyle):
    """
    """

    def __init__(self, parent):
        """Default constructor.

        :param parent:
        """
        GenericStyle.__init__(self, parent)
        FontStyle.__init__(self, parent)


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
