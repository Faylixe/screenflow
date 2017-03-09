# !/usr/bin/python

""" To document """

import logging
from math import floor
from screenflow.screens import Screen
from screenflow.constants import XML_NAME

# Configure logger.
logging.basicConfig()
logger = logging.getLogger(__name__)


def split_line(line, font, surface_width):
    """Splits the given line into chunks that matches the given surface_width
    regarding of the given font in order to avoid text overflow.

    :param line: Line to split.
    :param font: Font used to render line.
    :param surface_width: Width of the surface line will be rendered.
    :returns: List of chunks that matches the surface_width if possible.
    """
    splits = []
    queue = [line]
    while len(queue) > 0:
        current = queue.pop(0)
        line_width, _ = font.size(current)
        if line_width >= surface_width:
            tokens = line.split()
            tokens_size = len(tokens)
            if tokens_size == 0:
                logging.warning('Empty line detected')
            elif tokens_size == 1:
                logging.warning('Cannot split "%s" to avoid overflow', line)
                splits.append(current)
            else:
                middle = int(floor(len(tokens) / 2))
                queue.append(tokens[:middle])
                queue.append(tokens[middle:])
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

        :param surface_width: Width of the target surface line will be rendered.
        :returns: True if lines should be recomputed, False otherwise.
        """
        return len(self._lines) == 0 or surface_width != self._last_width

    def lines(self, font, surface_width):
        """Property binding of _lines attributes that computes if required text
        normalization to avoid text overflow.

        :param font: Font used to render line.
        :param surface_width: Width of the surface line will be rendered.
        :returns: Lines to display.
        """
        if self.should_update(surface_width):
            del self._lines[:]
            for line in self.text:
                line_width, _ = font.size(line)
                if line_width >= surface_width:
                    self._lines += split_line(line, font, surface_width)
                else:
                    self._lines.append(line)
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
        font = self.primary_font.font
        surface_width, _ = self.get_surface_size(surface)
        lines = self.message.lines(font, surface_width)
        y = self.padding[1]
        # TODO : Compute max size for centering ?
        for line in lines:
            text_surface = font.render(line, 1, self.primary_color, None)
            text_surface_width, text_surface_height = text_surface.get_size()
            text_surface_start = (surface_width - text_surface_width) / 2
            x = (self.padding[0] + text_surface_start)
            surface.blit(text_surface, (x, y))
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
