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


class Styles(object):
    """
    """

    def __init__(self):
        """
        :param parent:
        """
        self.__parent = None
        self.__style = None
        self.__primary = None
        self.__secondary = None
        self.__other = {}

    @property
    def parent(self):
        """
        :returns:
        """
        return self.__parent

    @parent.setter
    def parent(self, parent):
        """
        :param parent:
        """
        self.__parent = parent
        if self.__style is not None:
            self.__style.parent = self.__parent.__style
        if self.__primary is not None:
            self.__primary.parent = self.__parent.__primary
        if self.__secondary is not None:
            self.__secondary.parent = self.__parent.secondary
        # TODO : Process other ?

    @property
    def primary(self):
        """
        :returns:
        """
        if self.__primary is None:
            return self.__parent.primary
        return self.__primary

    @primary.setter
    def primary(self, value):
        """
        :param value:
        """
        self.__primary = value

    @property
    def secondary(self):
        """
        :returns:
        """
        return self.__secondary

    @secondary.setter
    def secondary(self, value):
        """
        :param value:
        """
        self.__secondary = value


class Style(object):
    """
        Base class for any Style implementation, that manages CSS property support.
    """

    def __init__(self, supported):
        """Default constructor.

        :param supported: Collection of CSS property supported by this style.
        """
        self._supported = supported

    def support(self, property):
        """Indicates if the given property is supported by this style instance.

        :param property: Property to check support for.
        :returns: True is the given property is supported, False otherwise.
        """
        return property in self._supported


class BasicStyle(Style):
    """
        Basic style implementation that only support background-color and
        padding properties. Used as screenflow selector style.
    """

    def __init__(self):
        """ Default constructor. """
        Style.__init__(self, ('background-color', 'padding'))
        self.__parent = None
        self.__background_color = None
        self.__padding = None

    @property
    def background_color(self):
        """Property getter for background color attribute.

        :returns: Background color to use.
        """
        if self.__background_color is None:
            return self.__parent.background_color
        return self.__background_color

    @background_color.setter
    def background_color(self, background_color):
        """Property setter for background color attribute.

        :param background_color: Background color to use.
        """
        self.__background_color = background_color

    @property
    def padding(self):
        """Property getter for padding attribute.

        :returns: Padding to use.
        """
        if self_._padding is None:
            return self.__parent.padding
        return self.__padding

    @padding.setter
    def padding(self, padding):
        """Property setter for padding attribute.

        :param padding: Padding to use.
        """
        self.__padding = padding


class FontStyle(Style):
    """
        Style that manages font related properties.
    """

    def __init__(self):
        """ Default constructor. """
        Style.__init__(self, ('color', 'font-size', 'font-family'))
        self.__parent = None
        self.__size = None
        self.__name = None
        self.__color = None

    @property
    def color(self):
        """Property getter for color attribute.

        :returns: Text color to use.
        """
        if self.__color is None:
            return self.__parent.color
        return self.__color

    @color.setter
    def color(self, color):
        """Property setter for color attribute.

        :param color: Text color to use.
        """
        self.__color = color

    @property
    def name(self):
        """Property getter for color attribute.

        :returns: Text color to use.
        """
        if self.__name is None:
            return self.__parent.name
        return self.__name

    @name.setter
    def name(self, name):
        """Property setter for name attribute.

        :param name: Text name to use.
        """
        self.__name = name

    @property
    def size(self):
        """Property getter for size attribute.

        :returns: Text size to use.
        """
        if self.__size is None:
            return self.__parent.size
        return self.__size

    @size.setter
    def size(self, size):
        """Property setter for size attribute.

        :param size: Text size to use.
        """
        self.__size = size


class ButtonStyle(FontStyle, BasicStyle):
    """
    """

    def __init__(self):
        """ Default constructor """
        BasicStyle.__init__(self)
        FontStyle.__init__(self)
