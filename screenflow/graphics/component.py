#!/usr/bin/python

"""
"""


class Component(object):
    """
    """

    def __init__(self, size):
        """Default constructor.

        :param size:
        """
        self._size = size
        self._childs = []

    def is_hit(self, position):
        """
        :param position:
        """
        return (
            (position[0] >= 0 and position[0] <= self._size[0]) and
            (position[1] >= 0 and position[0] <= self._size[1]))

    def add_child(self, child):
        """
        :param child:
        """
        self._childs.append(child)

    def render(self, drawer):
        """
        :param drawer:
        :param retunrs:
        """
        surface = drawer.create_surface(self._size)
        y = 0
        for child in self._childs:
            child_surface = child.render(drawer)
            x = (self._size[0] - child._size[0]) / 2
            y += child._size[1]
        return surface
