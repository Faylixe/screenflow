# !/usr/bin/python

"""
    ListScreen
    ==========

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

    def __init__(self, name):
        """Default constructor.

        """
        super(MessageScreen, self).__init__(name)
        self.provider = None
        self.renderer = None

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

    def draw(self, surface):
        """Drawing method, display centered text.

        :param surface: Surface to draw this screen into.
        """
        super(MessageScreen, self).draw(surface)