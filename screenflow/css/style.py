#!/usr/bin/env python
# coding: utf-8

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
        self._parent = None
        self._style = None
        self._primary = None
        self._secondary = None
        self._other = {}

    @property
    def parent(self):
        """
        :returns:
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        :param parent:
        """
        self._parent = parent
        if self._style is not None:
            self._style.parent = self._parent._style
        if self._primary is not None:
            self._primary.parent = self._parent._primary
        if self._secondary is not None:
            self._secondary.parent = self._parent.secondary
        # TODO : Process other ?

    @property
    def primary(self):
        """
        :returns:
        """
        if self._primary is None:
            return self._parent.primary
        return self._primary

    @primary.setter
    def primary(self, value):
        """
        :param value:
        """
        self._primary = value

    @property
    def secondary(self):
        """
        :returns:
        """
        return self._secondary

    @secondary.setter
    def secondary(self, value):
        """
        :param value:
        """
        self._secondary = value


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
        self._parent = None
        self._background_color = None
        self._padding = None

    @property
    def background_color(self):
        """Property getter for background color attribute.

        :returns: Background color to use.
        """
        if self._background_color is None:
            return self._parent.background_color
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Property setter for background color attribute.

        :param background_color: Background color to use.
        """
        self._background_color = background_color

    @property
    def padding(self):
        """Property getter for padding attribute.

        :returns: Padding to use.
        """
        if self._padding is None:
            return self._parent.padding
        return self._padding

    @padding.setter
    def padding(self, padding):
        """Property setter for padding attribute.

        :param padding: Padding to use.
        """
        self._padding = padding


class FontStyle(Style):
    """
        Style that manages font related properties.
    """

    def __init__(self):
        """ Default constructor. """
        Style.__init__(self, ('color', 'font-size', 'font-family'))
        self._parent = None
        self._size = None
        self._name = None
        self._color = None

    @property
    def color(self):
        """Property getter for color attribute.

        :returns: Text color to use.
        """
        if self._color is None:
            return self._parent.color
        return self._color

    @color.setter
    def color(self, color):
        """Property setter for color attribute.

        :param color: Text color to use.
        """
        self._color = color

    @property
    def name(self):
        """Property getter for color attribute.

        :returns: Text color to use.
        """
        if self._name is None:
            return self._parent.name
        return self._name

    @name.setter
    def name(self, name):
        """Property setter for name attribute.

        :param name: Text name to use.
        """
        self._name = name

    @property
    def size(self):
        """Property getter for size attribute.

        :returns: Text size to use.
        """
        if self._size is None:
            return self._parent.size
        return self._size

    @size.setter
    def size(self, size):
        """Property setter for size attribute.

        :param size: Text size to use.
        """
        self._size = size


class ButtonStyle(FontStyle, BasicStyle):
    """
    """

    def __init__(self):
        """ Default constructor """
        BasicStyle.__init__(self)
        FontStyle.__init__(self)
