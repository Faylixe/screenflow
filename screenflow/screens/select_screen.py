# !/usr/bin/python

"""
    SelectScreen
    ============

    Description incomming.

    XML definition
    --------------

    .. code-block:: xml

        <screen name="foo" type="select">
            <message>displayed message</message>
            <option>first choice</option>
            <option>second choice</option>
            ...
        </screen>

    Callback binding
    ----------------

    Given a *screenflow* instance, with registered *foo* select screen,
    callback binding can be achieved using ``on_select`` decorator:

    .. code-block:: python

        @screenflow.foo.on_sekect
        def on_foo_select(option):
            # TODO : Callback action here.

"""

from screenflow.screens.screen import Oriented, get_longest, get_highest
from screenflow.screens.message_based_screen import MessageBasedScreen
from screenflow.constants import XML_NAME, VERTICAL, HORIZONTAL, BLACK, WHITE


class SelectScreen(MessageBasedScreen, Oriented):
    """To document.
    """

    def __init__(
            self,
            name,
            message,
            options,
            orientation=VERTICAL):
        """Default constructor.

        :param name:
        :param message:
        :param options:
        :param orientation:
        :param cell_background_color:
        :param cell_padding:
        """
        MessageBasedScreen.__init__(self, name, message)
        Oriented.__init__(self, orientation)
        self.options = options
        self.callback = None
        self.__options_surface = None

    def on_select(self, function):
        """Decorator method that registers  the given function as selection callback.

        :param function: Decorated function to use as callback.
        :returns: Given function to match decorator pattern.
        """
        self.callback = function
        return function

    def on_mouse_up(self, position):
        """Mouse up event processing. Detects collision over displayed options
        and triggers callback if any options is hit.

        :param position: Position of the mouse up event.
        """
        # TODO : Compute option collision
        pass

    def get_options_surface_size(self, options_surface_size):
        """
        :param option_width:
        :param option_height:
        :returns:
        """
        n = len(self.options)
        surface_width = options_surface_size[0]
        surface_height = options_surface_size[1]
        # TODO : Find padding.
        total_padding = self.cell_padding * (n - 1)
        if self.isVertical():
            surface_height *= n
            surface_height += total_padding
        else:
            surface_width *= n
            surface_width += total_padding
        return (surface_width, surface_height)

    def check_bounds(self, surface, parent):
        """
        """
        if surface[0] > parent[0]:
            # TODO : Warning.
            pass
        if surface[1] > parent[1]:
            # TODO : Warning.
            pass

    def get_options_surface(self, parent_surface_size):
        """
        :param parent_surface_width:
        :returns:
        """
        if self._options_surface is None:
            # TODO : Match sizer.
            text_sizer = self.font_manager.primary
            option_width = get_longest(self.options, text_sizer)
            option_height = get_highest(self.options, text_sizer)
            option_surface_size = (option_width, option_height)
            options_surface_size = self.get_options_surface_size(
                option_surface_size)
            self.check_bounds(options_surface_size, parent_surface_size)
            self.__options_surface = self.create_surface(options_surface_size)
            self.__options_surface.fill((255, 255, 255))
            current = 0
            for option in self.options:
                option_surface = self.draw_button(option, option_surface_size)
                position = None
                if self.isVertical():
                    position = (0, current)
                else:
                    position = (current, 0)
                self.__options_surface.blit(option_surface, position)
                if self.isVertical():
                    current += option_height
                else:
                    current += option_width
                # TODO : Get padding.
                current += self.cell_padding
        return self.__options_surface

    def get_final_surface(self, message_surface, options_surface):
        """
        """
        message_surface_size = message_surface.get_size()
        options_surface_size = options_surface.get_size()
        width = max(message_surface_size[0], options_surface_size[0])
        height = message_surface_size[1] + options_surface_size[1] + 20
        # TODO : Add padding.
        surface = self.create_surface((width, height))
        self.draw_background(surface)
        message_x = (width - message_surface_size[0]) / 2
        surface.blit(message_surface, (message_x, 0))
        options_x = (width - options_surface_size[0]) / 2
        # TODO : Add padding.
        options_y = message_surface_size[1] + 20
        surface.blit(options_surface, (options_x, options_y))
        return surface

    def draw(self, surface):
        """Drawing method, display centered label and options list below.

        :param surface: Surface to draw this screen into.
        """
        super(SelectScreen, self).draw(surface)
        surface_size = surface.get_size()
        message_surface = self.get_message_surface(surface_size)
        options_surface = self.get_options_surface(surface_size)
        final_surface = self.get_final_surface(message_surface, options_surface)
        self.draw_centered(surface, final_surface)

# XML tag for option parameters.
XML_OPTION = 'option'


def factory(screen_def):
    """ Static factory function for creating a select screen
    from a given XML screen definition.

    :param screen_def: Screen definition as a dictionary from XML parsing.
    :returns: Created select screen instance.
    """
    message = MessageBasedScreen.get_message(screen_def)
    if XML_OPTION not in screen_def:
        raise AttributeError('No option(s) set in screen definition')
    options = screen_def[XML_OPTION]
    if not isinstance(options, list):
        raise AttributeError('At least two options is required')
    return SelectScreen(screen_def[XML_NAME], message, options)
