# !/usr/bin/python

"""
    ListScreen
    ==========

    XML Definition

    .. code-block:: xml

        <screen name="foo" type="list">
            <label>displayed label</label>
        </screen>
"""

import logging
from math import floor
from screenflow.screens import Screen
from screenflow.constants import XML_NAME

# Configure logger.
logging.basicConfig()
logger = logging.getLogger(__name__)


class ListScreen(Screen):
    """To document.
    """

    # 
    HORIZONTAL = 0

    #
    VERTICAL = 1

    def __init__(self, name, orientation=ListScreen.VERTICAL):
        """Default constructor.

        :param name:
        """
        super(MessageScreen, self).__init__(name)
        self.orientation = orientation
        self.provider = None
        self.renderer = None
        self._data = None
        self._surfaces = []

    @property
    def data(self):
        """
        :returns:
        """
        if self._data is None:
            if self.provider is None:
                raise AttributeError('Data provider not settled')
            self._data = self.provider()
        return self._data

    def provider(self, function):
        """Decorator method that registers the given function as data provider.

        :param function: Decorated function to use as data provider.
        :returns: Given function to match decorator pattern.
        """
        self.provider = function
        return function

    def renderer(self, function):
        """Decorator method that registers the given function as data renderer.

        :param function: Decorated function to use as data renderer.
        :returns: Given function to match decorator pattern.
        """
        self.renderer = function
        return function

    def get_item_surface(self, i):
        """
        """
        if len(self._surfaces) < i:
            self._surfaces[i] = None
        if self._surfaces[i] is None:
            self._surfaces[i] = None
        return self._surfaces[i]

    def draw(self, surface):
        """Drawing method, display centered text.

        :param surface: Surface to draw this screen into.
        """
        super(MessageScreen, self).draw(surface)
        # TODO : Draw up scroller.
        item_size = None
        container_size = None
        n = container_size[self.orientation] / item_size[self.orientation]
        for i in range(n):
            item_surface = get_item_surface(item_size)
            self.renderer(None, item_surface)
        # TODO : Drawp down scroller.