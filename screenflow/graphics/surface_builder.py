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


class SurfaceBuilder(object):
    """
    """

    def __init__(self, surface_factory, item_sizer):
        """
        """
        self._surface_factory = surface_factory
        self._item_sizer = item_sizer

    def get_item_size(self, item):
        """
        """
        pass

    def get_size(self, collection):
        """
        """
        pass

    def build(self):
        """
        """
        size = self.get_size()
        surface = self._surface_factory(size)
        return surface


class CollectionSurfaceBuilder(SurfaceBuilder):
    """
    """
    pass


class MultiSurfaceBuilder(SurfaceBuilder):
    """
    """
    pass