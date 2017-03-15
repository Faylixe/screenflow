#!/usr/bin/python

"""

"""


class GraphicsAdapter(object):
    """
    """

    def __init__(self, drawer, event_manager):
        """Default constructor.

        :param drawer:
        :param event_manager:
        """
        self.drawer = drawer
        self.event_manager = event_manager
        self._font_manager = None

    @property
    def font_manager(self):
        """Property getter for font manager attribute. If font manager instance is not
        settled, then an exception will be raised when trying to access.

        :returns: Font manager instance if any, raise a exception otherwise.
        """
        return self.drawer.font_manager

    @font_manager.setter
    def font_manager(self, font_manager):
        """Property setter for font manager attribute.

        :param font_manager: Font manager instance to use.
        """
        self.drawer.font_manager = font_manager

    def create_main_surface(self):
        """Factory method for creating top level container surface.

        :returns: New surface object, that acts as main container.
        """
        raise NotImplementedError()

    def flip_display(self):
        """ Updates display refreshing drawn components. """
        raise NotImplementedError()
