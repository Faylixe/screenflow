#!/usr/bin/python

""" Mock implementation for graphics adapter. """

from screenflow.graphics.graphics_adapter import GraphicsAdapter
from mock_surface import MockSurface
from mock_drawer import MockDrawer
from mock_font_manager import MockFontManager
from mock_event_manager import MockEventManager


class MockGraphicsAdapter(GraphicsAdapter):
    """ GraphicsAdapter mock. """

    def __init__(self):
        """ Default constructor. """
        GraphicsAdapter.__init__(self, MockDrawer(), MockEventManager())

    def create_main_surface(self):
        """Factory method for creating top level container surface.

        :returns: New surface object, that acts as main container.
        """
        return MockSurface()

    def flip_display(self):
        """ Do nothing. """
        pass
