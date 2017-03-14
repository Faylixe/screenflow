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
        """
        pass

    def get_style(self, path):
        """
        """
    

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
