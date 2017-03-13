# !/usr/bin/python

"""
    MessageBasedScreen
    =============

    A MessageBasedScreen is an abstract Screen implementation
    that aims to provide message header features with automatic
    layouting.

    Subclass should use get_message_surface() method to get a
    surface that exposes text message.
"""

import logging
from math import floor
from screenflow.screens import Screen
from screenflow.screens.screen import get_longest, get_highest
from screenflow.constants import XML_NAME

# Configure logger.
logging.basicConfig()
logger = logging.getLogger(__name__)

# XML tag for message parameter.
XML_MESSAGE = 'message'


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
            tokens = current.split()
            tokens_size = len(tokens)
            if tokens_size == 1:
                logging.warning('Cannot split "%s" to avoid overflow', line)
                splits.append(current)
            else:
                middle = int(floor(len(tokens) / 2))
                subqueue = []
                subqueue.append(' '.join(tokens[:middle]))
                subqueue.append(' '.join(tokens[middle:]))
                queue = subqueue + queue
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
        self.__lines = []
        self.__last_width = 0

    def should_update(self, surface_width):
        """Indicates if the normalization process should be done again.
        Such predicate return True if any of those two case match :

        - Internal line collection is empty.
        - Target surface width changed.

        :param surface_width: Width of the surface line will be rendered.
        :returns: True if lines should be recomputed, False otherwise.
        """
        return len(self._lines) == 0 or surface_width != self.__last_width

    def lines(self, sizer, surface_width):
        """Property binding of _lines attributes that computes if required text
        normalization to avoid text overflow.

        :param sizer: Function that computes rendering size for a given text.
        :param surface_width: Width of the surface line will be rendered.
        :returns: Lines to display.
        """
        if self.should_update(surface_width):
            del self.__lines[:]
            for line in self.text:
                line_width, _ = sizer(line)
                if line_width >= surface_width:
                    self.__lines += split_line(line, sizer, surface_width)
                else:
                    self.__lines.append(line)
            self.__last_width = surface_width
        return self.__lines


class MessageBasedScreen(Screen):
    """ MessageScreen aims to only display a text message, and allows
    transition on touch event.
    """

    def __init__(self, name, message):
        """Default constructor.

        :param name:
        :param message: Message displayed into the screen.
        """
        Screen.__init__(self, name)
        self.message = Message(message)
        self.__last_width = 0
        self.__message_surface = None

    def get_message_surface(self, parent_surface_size):
        """Factory method that creates a surface with this screen message.
        Created surface is cached in order to avoid duplicate computation.

        :param parent_surface_width: Width of the target parent surface.
        :returns: Created surface.
        """
        size_updated = self.__last_width != parent_surface_size[0]
        if self.__message_surface is None or size_updated:
            self.__last_width = parent_surface_size[0]
            # TODO : Refactor sizer concept.
            text_sizer = self.font_manager.primary
            lines = self.message.lines(text_sizer, parent_surface_size[0])
            line_width = get_longest(lines, text_sizer)
            line_height = get_highest(lines, text_sizer)
            size = (line_width, len(lines) * line_height)
            self.__message_surface = self.create_surface(size)
            # TODO : Consider using property ?
            self.draw_background(self.__message_surface)
            y = 0
            for line in lines:
                text_surface_width, _ = text_sizer(line)
                x = (line_width - text_surface_width) / 2
                self.line_surface = self.draw_primary_text(line)
                self.__message_surface.blit(self.line_surface, (x, y))
                y += line_height
        return self.__message_surface

    @staticmethod
    def get_message(screen_def):
        """Static factory function for parsing a message
        attribute for a given XML definition.

        :param screen_def: Screen definition as a dictionary from XML parsing.
        :returns: Parsed message instance.
        """
        if XML_MESSAGE not in screen_def:
            raise AttributeError('No message set in screen definition')
        return screen_def[XML_MESSAGE]
