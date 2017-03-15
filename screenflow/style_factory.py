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

        @css_property_parser('property_name')
        def my_parser(value, style):
            // Set your target style attribute here.

    Where _value_ is the CSS value parsed for your declaration, and _style_ the
    associated Style instance to set declaration value in. The @css_property_parser
    ensure that the target property is supported by the given style object.

"""

import logging
import tinycss
from webcolors import hex_to_rgb, name_to_rgb
from style import Styles, BasicStyle, FontStyle, ButtonStyle
from constants import BLACK, WHITE, GRAY

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
    """Simple sugar function that retrieves a Styles instance from a given
    map using the given selector, creating it if not existing.

    :param map: Map to retrieve Styles from.
    :param selector: Selector to retrieve Styles for.
    :returns: Associated Styles instance for the given selector.
    """
    key = selector[1:]
    if key not in map.keys():
        map[key] = Styles()
    return map[key]


def css_property_parser(property):
    """Function decorator that validates CSS property support for a target
    style instance. If such property is not supported an AttributeError is
    raised.

    :param property: Target CSS property to check support.
    :returns: Decorated function.
    """
    def decorator(parser):
        def wrapper(*args, **kwargs):
            value = args[0]
            style = args[1]
            if not style.support(property):
                raise AttributeError('Property %s not supported' % property)
            parser(value, style)
        return wrapper
    return decorator


@css_property_parser('background-color')
def background_color_parser(value, style):
    """Parser function for CSS background-color property. Color will be
    evaluated through webcolors helper function.

    :param value: Background color value read.
    :param style: Target style to set background color attribute to.
    """
    style.background_color = get_color(value)


@css_property_parser('padding')
def padding_parser(value, style):
    """Parser function for CSS padding property. If the given value is not a
    integer then it will be ignored.

    :param value: Padding value read.
    :param style: Target style to set padding attribute to.
    """
    style.padding = int(value)


@css_property_parser('font-size')
def font_size_parser(value, style):
    """Parser function for CSS font-size property. If the given value is not a
    integer then it will be ignored.

    :param value: Font size value read.
    :param style: Target style to set font size attribute to.
    """
    style.size = int(value)


@css_property_parser('font-family')
def font_family_parser(value, style):
    """Parser function for CSS font-family property.

    :param value: Font family value read.
    :param style: Target style to set font name attribute to.
    """
    style.name = value


@css_property_parser('color')
def color_parser(value, style):
    """Parser function for CSS color property.

    :param value: Color value read.
    :param style: Target style to set color attribute to.
    """
    style.color = get_color(value)

# Default style properties.
DEFAULT_FONT = 'arial'
DEFAULT_PRIMARY_SIZE = 15
DEFAULT_SECONDARY_SIZE = 10
DEFAULT_PADDING = 20


def create_default_styles():
    """Factory method that creates a default styles instance.

    :returns: Created default style instance.
    """
    styles = Styles()
    styles.style = BasicStyle()
    styles.style.background_color = WHITE
    styles.style.padding = DEFAULT_PADDING
    styles.primary = FontStyle()
    styles.primary.name = DEFAULT_FONT
    styles.primary.size = DEFAULT_PRIMARY_SIZE
    styles.primary.color = BLACK
    styles.secondary = FontStyle()
    styles.secondary.name = DEFAULT_FONT
    styles.secondary.size = DEFAULT_SECONDARY_SIZE
    styles.secondary.color = GRAY
    styles.button = ButtonStyle()
    styles.button.background_color = BLACK
    styles.button.padding = 20
    styles.button.name = DEFAULT_FONT
    styles.button.size = DEFAULT_PRIMARY_SIZE
    styles.button.color = WHITE
    return styles


class StyleFactory(object):
    """To document.
    """

    def __init__(self):
        """ Default constructor. """
        self._declaration_parser = {}
        self._name_styles = {}
        self._type_styles = {}
        self._screenflow_styles = create_default_styles()
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
        self._declaration_parser[name] = parser

    def _get_selector_styles(self, tls):
        """
        :param tls:
        :returns:
        """
        if tls.startswith('#'):
            return get_styles(self._name_styles, tls)
        elif tls.startswith('.'):
            styles = get_styles(self._type_styles, tls)
            styles.parent = self._screenflow_styles
            return styles
        return self._screenflow_styles

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
            styles = self._get_selector_styles(selector)
            style = styles.get_style(path)
            for declaration in ruleset.declarations:
                self._parse_declaration(declaration, style)

    def _parse_declaration(self, declaration, style):
        """
        :param declaration:
        :param style:
        """
        name = declaration.name
        if name not in self._declaration_parser.keys():
            # TODO : Log error.
            return
        parser = self._declaration_parser[name]
        try:
            parser(declaration.value.as_css(), style)
        except Exception as e:
            logging.warn(
                '[%s:%s] %s' % (
                    declaration.line,
                    declaration.column,
                    str(e)))

    def _get_name_styles(self, screen):
        """
        """
        if screen.name in self._name_styles.keys():
            styles = self._name_styles[screen.name]
            if styles.parent is None:
                if screen.type in self._type_styles.keys():
                    styles.parent = self._type_styles[screen.type]
                else:
                    styles.parent = self._screenflow_styles
        return None

    def _get_screen_styles(self, screen):
        """
        :param screen:
        :returns:
        """
        styles = self._get_name_styles(screen)
        if styles is None:
            if screen.type in self._type_styles.keys():
                return self._type_styles[screen.type]
            return self._screenflow_styles
        return styles

    def get_style(self, screen):
        """
        :param screen:
        :returns:
        """
        styles = self._get_screen_styles(screen)
        # TODO : Check parent.
        return styles.style

    def get_font_styles(self, screen):
        """
        :param screen:
        :returns:
        """
        styles = self._get_screen_styles(screen)
        # TODO : Check parent.
        return (styles.primary, styles.secondary)

    def get_button_style(self, screen):
        """
        :param screen:
        :returns:
        """
        styles = self._get_screen_styles(screen)
        # TODO : Check parent.
        return styles.button
