# !/usr/bin/python

"""
    MessageScreen
    =============

    *MessageScreen* is the most basic screen implementation that just aims
    to display a message to the user and trigger callback when a mouse event
    occurs at any position in the screen.

    XML definition
    ---------------

    .. code-block:: xml

        <screen name="foo" type="message">
            <message>displayed message</message>
        </screen>

    Callback binding
    ----------------

    Given a *screenflow* instance, with registered *foo* message screen,
    callback binding can be achieved using ``on_touch`` decorator:

    .. code-block:: python

        @screenflow.foo.on_touch
        def on_foo_touch():
            # TODO : Callback action here.

"""

import logging
from math import floor
from pygame import Surface
from screenflow.screens.message_based_screen import MessageBasedScreen
from screenflow.constants import XML_NAME

# Configure logger.
logging.basicConfig()
logger = logging.getLogger(__name__)


class MessageScreen(MessageBasedScreen):
    """ MessageScreen aims to only display a text message, and allows
    transition on touch event.
    """

    def __init__(self, name, message):
        """Default constructor.

        :param message: Message displayed into the screen.
        """
        MessageBasedScreen.__init__(self, name, message)
        self.callback = None

    def on_touch(self, function):
        """Decorator method that registers the given function as screen touch callback.

        :param function: Decorated function to use as callback.
        :returns: Given function to match decorator pattern.
        """
        self.callback = function
        return function

    def on_mouse_up(self, position):
        """Mouse up event processing. Calls the delegate callback function if any.

        :param position: Position of the mouse up event.
        """
        if self.callback is not None:
            self.callback()

    def draw(self, surface):
        """Drawing method, display centered text.

        :param surface: Surface to draw this screen into.
        """
        MessageBasedScreen.draw(self, surface)
        surface_size = self.get_surface_drawable_size(surface)
        message_surface = self.get_message_surface(surface_size)
        self.draw_centered(surface, message_surface)


def factory(screen_def):
    """Static factory function for creating a message screen
    from a given XML screen definition.

    :param screen_def: Screen definition as a dictionary from XML parsing.
    :returns: Created message screen instance.
    """
    message = MessageBasedScreen.get_message(screen_def)
    return MessageScreen(screen_def[XML_NAME], message)
