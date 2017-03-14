#!/usr/bin/python

"""
    StyleFactory
    ============

    CSS file parser.

    Declaration processing
    ----------------------

    **StyleFactory** maintains a map that provides declaration parser function
    for a given declaration name. Client can register at any moment a parser
    function in order to handle new CSS declaration. Such parser should have
    following signature:

    .. code-block:: python

        def my_parser(value, style):
            pass

    Where _value_ is the CSS value parsed for your declaration, and _style_ the
    associated Style instance to set declaration value in.

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


def get_styles(map, selector):
    """
    :param map:
    :param selector:
    :returns:
    """
    key = selector[1:]
    if key not in self.name_drawers.keys():
        map[key] = Styles()
    return map[key]


def background_color_parser(value, style):
    """
    :param value:
    :param style:
    """
    # TODO : Check instance.
    style.background_color = get_color(value)


def padding_parser(value, style):
    """
    :param value:
    :param style:
    """
    # TODO : Check instance.
    # TODO : Check padding value.
    style.padding = int(value)


def font_size_parser(value, style):
    """
    :param value:
    :param style:
    """
    # TODO : Check instance.
    # TODO : Check value.
    style.size = int(value)


def font_family_parser(value, style):
    """
    :param value:
    :param style:
    """
    # TODO : Check instance.
    # TODO : Check value.
    style.name = value


def color_parser(value, style):
    """
    :param value:
    :param style:
    """
    # TODO : Check instance.
    style.color = get_color(value)

# Default style properties.
DEFAULT_FONT = 'arial'
DEFAULT_PRIMARY_SIZE = 20
DEFAULT_SECONDARY_SIZE = 15
DEFAULT_PADDING = 20


def create_default_styles():
    """
    :returns:
    """
    styles = Styles()
    styles.style = GenericStyle()
    styles.style.background_color = WHITE
    styles.style.padding = DEFAULT_PADDING
    styles.primary = FontStyle()
    styles.primary.name = DEFAULT_FONT
    styles.primary.size = DEFAULT_PRIMARY_SIZE
    styles.primary.color = BLACK
    styles.secondary = FontStyle()
    styles.primary.name = DEFAULT_FONT
    styles.primary.size = DEFAULT_SECONDARY_SIZE
    styles.primary.color = GRAY
    return styles


class StyleFactory(object):
    """To document.
    """

    def __init__(self):
        """ Default constructor. """
        self.__declaration_parser = {}
        self.__name_styles = {}
        self.__type_styles = {}
        self.__screenflow_styles = create_default_styles()
        self.register_declaration_parser(
            'background-color',
            background_color_parser)
        self.register_declaration_parser('padding', padding_parser)
        self.register_declaration_parser('font-size', font_size_parser)
        self.register_declaration_parser('font-family', font_family_parser)
        self.register_declaration_parser('color', color_parser)

    def register_declaration_parser(self, name, parser):
        """
        :param name:
        :param parser:
        """
        # TODO : Check for conflict.
        self.__declaration_parser[name] = parser

    def __get_selector_styles(self, tls):
        """
        :param tls:
        :returns:
        """
        if tls.startswith('#'):
            return get_styles(self.__name_styles, tls)
        elif tls.startswith('.'):
            return get_styles(self.__type_styles, tls)
        return self.__screenflow_styles

    def load(self, file):
        """Loads and parses the given CSS file.

        :param file: CSS file to load.
        """
        parser = tinycss.make_parser('fonts3')
        stylesheet = parser.parse_stylesheet_file(file)
        for ruleset in stylesheet.rules:
            selector = ruleset.selector.as_css()
            path = selector.split()
            tls = path.pop(0)
            styles = self.__get_selector_styles(selector)
            style = styles.get_style(path)
            for declaration in ruleset.declarations:
                self.__parse_declaration(declaration, style)

    def __parse_declaration(self, declaration, style):
        """
        :param declaration:
        :param style:
        """
        name = declaration.name
        if name not in self.__declaration_parser.keys():
            # TODO : Log error.
            return
        parser = self.__declaration_parser[name]
        parser(declaration.value.as_css(), style)

    def __get_name_styles(self, screen):
        """
        """
        if screen.name in self.__name_styles.keys():
            styles = self.__name_styles[screen.name]
            if screen.type in self.__type_styles.keys():
                # Set type as parent.
                pass
        return None

    def __get_screen_styles(self, screen):
        """
        :param screen:
        :returns:
        """
        styles = self.__get_name_styles(self, screen.name)
        if styles is None:
            if screen.type in self.__type_styles.keys():
                return self.__type_styles[screen.type]
            return self.__screenflow_styles
        return styles

    def get_style(self, screen):
        """
        :param screen:
        :returns:
        """
        styles = self.__get_screen_styles(self, screen)
        # TODO : Check parent.
        return styles.style

    def get_font_styles(self, screen):
        """
        :param screen:
        :returns:
        """
        styles = self.__get_screen_styles(self, screen)
        # TODO : Check parent.
        return (styles.primary, styles.secondary)
