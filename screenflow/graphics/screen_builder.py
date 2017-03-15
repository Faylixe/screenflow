#!/usr/bin/python

"""
"""

def find(collection, sizer, axis):
    """
    :param collection:
    :param sizer:
    :param axis:
    :returns:
    """
    best = max(collection, key=lambda x: sizer(x)[axis])
    return sizer(best)[axis]


def get_longest(collection, sizer):
    """
    :param collection:
    :param sizer:
    :returns:
    """
    return find(collection, sizer, 0)


def get_highest(collection, sizer):
    """
    :param collection:
    :param sizer:
    :returns:
    """
    return find(collection, sizer, 1)

class Component(object):
    """
    """

    def __init__(self):
        """Default constructor.
        """
        self._size = None
        self._childs = []

    def is_hit(self, position):
        """
        :param position:
        """
        return (
            (position[0] >= 0 and position[0] <= self._size[0]) and
            (position[1] >= 0 and position[0] <= self._size[1]))


class ScreenRenderBuilder(object):
    """
    """

    def __init__(self, parent=None):
        """
        :param parent:
        """
        self._parent = parent
        self._size = None
        self._childs = []
        self.padding = 0
        self.orientation = VERTICAL

    def build(self, drawer):
        """Rendering method that creates a surface with built component size.

        :param drawer: Drawer instance to use for rendering surface.
        :returns: Created rendering surface.
        """
        surface = drawer.create_surface(self._size)
        y = 0
        for child in self._childs:
            child_surface = child.build(drawer)
            x = (self._size[0] - child._size[0]) / 2
            drawer.blit(surface, child_surface, (x, y))
            y += child._size[1] + self.padding
        return surface

    def _is_terminal(self):
        """
        """
        return len(self._childs) == 0

    def __enter__(self):
        """
        """
        return self

    def __exit__(self):
        """
        """
        if self._is_terminal():
            pass
        else:
            largest = max(self._childs, key=lambda c: c._size[0])
            highest = max(self._childs, key=lambda c: c._size[1])
            self._size = (largest._size[0}, highest._size[1])

    def child():
        """
        :returns:
        """
        return ScreenRenderBuilder(self)
