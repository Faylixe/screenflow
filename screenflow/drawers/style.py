#!/usr/bin/python

"""
    To document.
"""

from pygame.font import SysFont


class FontStyle(object):
    """
    """

    def __init__(self, parent):
        """Default constructor.

        :param parent:
        """
        self.parent = parent
        self._size = None
        self._name = None
        self._color = None

    @property
    def color():
        """Property getter for color attribute.

        :returns: Text color to use.
        """
        if self._color is None:
            return self.parent.color
        return self._color

    @xolor.setter
    def color(self, color):
        """Property setter for color attribute.

        :param color: Text color to use.
        """
        self._color = color

    @property
    def name():
        """Property getter for color attribute.

        :returns: Text color to use.
        """
        if self._name is None:
            return self.parent.name
        return self._name

    @name.setter
    def name(self, name):
        """Property setter for name attribute.

        :param name: Text name to use.
        """
        self._name = name

    @property
    def size():
        """Property getter for size attribute.

        :returns: Text size to use.
        """
        if self._size is None:
            return self.parent.size
        return self._size

    @size.setter
    def size(self, size):
        """Property setter for size attribute.

        :param size: Text size to use.
        """
        self._size = size


class Style(object):
    """
    """

    def __init__(self, parent):
        """Default constructor.

        :param parent:
        """
        self.parent = parent
        self._primary = None
        self._secondary = None

    @property
    def background_color(self):
        """Property getter for background_color attribute.

        :returns: Background color to use.
        """
        if self._background_color is None:
            return self.parent.background_color
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Property setter for background_color attribute.

        :param background_color: Background color to use.
        """
        self._background_color = background_color

    @property
    def padding(self):
        """Property getter for padding attribute.

        :returns: Screen padding to use.
        """
        if self._padding is None:
            return self.parent.padding
        return self._padding

    @padding.setter
    def padding(self, padding):
        """Property setter for padding attribute.

        :param padding: Screen padding to use.
        """
        self._padding = padding
