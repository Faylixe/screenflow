# !/usr/bin/python

""" To document """

import logging

from math import floor

from screenflow.screens import Screen
from screenflow.constants import XML_NAME

# Configure logger.
logging.basicConfig()
logger = logging.getLogger(__name__)


class Message(object):
    """ To document. """

    def __init__(self):
        """
        """
        self.text = None
        self.max_line_width = 0
        self.max_line_height = 0

    def normalize_line(self, line, font, surface_width):
        """
        """
        line_width, line_height = font.size(line)
        self.max_line_height = max(self.max_line_height, line_height)
        if line_width >= surface_width:
            tokens = line.split()
            tokens_size = len(tokens)
            if tokens_size == 0:
                logging.warning('Empty line detected')
            elif tokens_size == 1:
                logging.warning(
                    'Cannot split line to avoid text overflow : %s', line)
            else:
                middle = int(floor(len(tokens) / 2))
                return (tokens[:middle], tokens[middle:])
        return line

    def normalize(self, message, font, surface_width):
        """

        :param message:
        :param font:
        :param surface_width:
        :returns:
        """
        self.text = message
        while True:
            normalization_buffer = []
            update_performed = False
            for line in self.text:
                first, second = self.normalize_line(line)
                normalization_buffer.append(first)
                if second is not None:
                    normalization_buffer.append(second)
            normalized = buffer
            if not update_performed:
                break


class MessageScreen(Screen):
    """MessageScreen class. A MessageScreen aims to only display
    a text message, and allows transition on touch event.
    """

    def __init__(self, name, message):
        """Default constructor.

        :param message: Message displayed into the screen.
        """
        super(MessageScreen, self).__init__(name)
        self.raw_message = (' '.join(message.split())).split('\n')
        self.message = Message()
        self.callback = None

    def on_touch(self, function):
        """Decorator method that registers the given function
        as screen touch callback.

        :param function: Decorated function to use as callback.
        """
        self.callback = function
        return function

    def on_mouse_up(self, position):
        """Mouse up event processor. Calls the delegate
        callback function is any.

        :param position: Position of the mouse up event.
        """
        if self.callback is not None:
            self.callback()

    def draw(self, surface):
        """ Drawing method, display centered text.

        :param surface: Surface to draw this screen into.
        """
        super(MessageScreen, self).draw(surface)
        font = self.get_primary_font()
        if self.message.text is None:
            surface_width, surface_height = self.get_surface_size()
            self.message = Message()
            self.message.normalize(self.message, font, surface_width)
        full_surface_size = surface.get_size()
        x = (full_surface_size[0] - self.message.max_line_width) / 2
        y = (full_surface_size[1] - self.message.max_line_height) / 2
        for line in self.message.text:
            text_surface = font.render(line, 1, self.primary_color, None)
            text_surface_width, _ = text_surface.get_size()
            text_surface_start = x + \
                ((self.message.max_line_width - text_surface_width) / 2)
            surface.blit(text_surface, (text_surface_start, y))
            y += self.message.max_line_height


# XML tag for message parameter.
XML_MESSAGE = 'message'


def factory(screen_def):
    """Static factory function for creating a message screen from

    :param screen_def: Screen definition as a dictionary from XML parsing.
    """
    if XML_MESSAGE not in screen_def:
        raise AttributeError('No message set in screen definition')
    return MessageScreen(screen_def[XML_NAME], screen_def[XML_MESSAGE])
