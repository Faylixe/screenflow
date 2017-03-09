# !/usr/bin/python

"""
    ``MessageScreen``
    =================

    ``MessageScreen`` is the most basic screen implementation that just aims
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

    Given a ``screenflow`` instance, with registered ``foo`` message screen,
    callback binding can be achieve using ``on_touch`` decorator:

    .. code-block:: python

        @screeflow.foo.on_touch
        def on_foo_touch():
            # TODO : Callback action here.

"""

import logging
from math import floor
from screenflow.screens import Screen
from screenflow.constants import XML_NAME

# Configure logger.
logging.basicConfig()
logger = logging.getLogger(__name__)


def split_line(line, sizer, surface_width):
    """Splits the given line into chunks that matches the given surface_width
    regarding of the given font in order to avoid text overflow.

    :param line: Line to split.
    :param sizer: Function that computes rendering size for a given text.
    :param surface_width: Width of the surface line will be rendered.
    :returns: List of chunks that matches the surface_width if possible.
    """
    splits = []
    queue = [line]
    while len(queue) > 0:
        current = queue.pop(0)
        line_width, _ = sizer(current)
        if line_width >= surface_width:
            tokens = line.split()
            tokens_size = len(tokens)
            if tokens_size == 1:
                logging.warning('Cannot split "%s" to avoid overflow', line)
                splits.append(current)
            else:
                middle = int(floor(len(tokens) / 2))
                queue.append(' '.join(tokens[:middle]))
                queue.append(' '.join(tokens[middle:]))
        else:
            splits.append(current)
    return splits


class Message(object):
    """Message object provides normalization process in order
    to avoid text overflow in a standard surface rendering.
    """

    def __init__(self, message):
        """Default constructor.

        :param message: Raw message instance to use.
        """
        self.text = (' '.join(message.split())).split('\n')
        self._lines = []
        self._last_width = 0

    def should_update(self, surface_width):
        """Indicates if the normalization process should be done again.
        Such predicate return True if any of those two case match :

        - Internal line collection is empty.
        - Target surface width changed.

        :param surface_width: Width of the surface line will be rendered.
        :returns: True if lines should be recomputed, False otherwise.
        """
        return len(self._lines) == 0 or surface_width != self._last_width

    def lines(self, sizer, surface_width):
        """Property binding of _lines attributes that computes if required text
        normalization to avoid text overflow.

        :param sizer: Function that computes rendering size for a given text.
        :param surface_width: Width of the surface line will be rendered.
        :returns: Lines to display.
        """
        if self.should_update(surface_width):
            del self._lines[:]
            for line in self.text:
                line_width, _ = sizer(line)
                if line_width >= surface_width:
                    self._lines += split_line(line, sizer, surface_width)
                else:
                    self._lines.append(line)
            self._last_width = surface_width
        return self._lines


class MessageScreen(Screen):
    """ MessageScreen aims to only display a text message, and allows
    transition on touch event.
    """

    def __init__(self, name, message):
        """Default constructor.

        :param message: Message displayed into the screen.
        """
        super(MessageScreen, self).__init__(name)
        self.message = Message(message)
        self.callback = None

    def on_touch(self, function):
        """Decorator method that registers the given function as screen touch callback.

        :param function: Decorated function to use as callback.
        :returns: Given function to match decorator pattern.
        """
        self.callback = function
        return function

    def on_mouse_up(self, position):
        """Mouse up event processor. Calls the delegate callback function if any.

        :param position: Position of the mouse up event.
        """
        if self.callback is not None:
            self.callback()

    def draw(self, surface):
        """Drawing method, display centered text.

        :param surface: Surface to draw this screen into.
        """
        super(MessageScreen, self).draw(surface)
        surface_width, _ = self.get_surface_size(surface)
        text_sizer = self.font_manager.primary
        lines = self.message.lines(text_sizer, surface_width)
        y = self.padding[1]
        # TODO : Compute max size for centering ?
        for line in lines:
            text_surface_width, text_surface_height = text_sizer(line)
            text_surface_start = (surface_width - text_surface_width) / 2
            x = (self.padding[0] + text_surface_start)
            self.font_manager.draw_primary_text(line, surface, (x, y))
            y += text_surface_height


# XML tag for message parameter.
XML_MESSAGE = 'message'


def factory(screen_def):
    """Static factory function for creating a message screen from

    :param screen_def: Screen definition as a dictionary from XML parsing.
    :returns: Created message screen instance.
    """
    if XML_MESSAGE not in screen_def:
        raise AttributeError('No message set in screen definition')
    return MessageScreen(screen_def[XML_NAME], screen_def[XML_MESSAGE])
