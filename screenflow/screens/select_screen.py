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
            <cellpadding>20</cellpadding> <!-- optional -->
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

from screenflow.screens.screens import get_longest, get_highest
from screenflow.screens.message_based_screen import MessageBasedScreen
from screenflow.constants import XML_NAME, VERTICAL, HORIZONTAL


class SelectScreen(MessageBasedScreen, Oriented):
    """To document.
    """

    def __init__(
            self,
            name,
            message,
            options,
            orientation=VERTICAL,
            cell_background_color=BLACK,
            cell_padding=10):
        """Default constructor.

        :param name:
        :param message:
        :param options:
        :param orientation:
        :param cell_background_color:
        :param cell_padding:
        """
        super(SelectScreen, self).__init__(
            name=name,
            message=message,
            orientation=orientation)
        self.options = options
        self.cell_background_color = 
        self.cell_padding = cell_padding
        self.callback = None
        self._options_surface = None

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

    def get_option_surface(self, option, size):
        """
        :param option:
        :param size:
        """
        option_surface = self.create_surface(size)
        option_surface.fill(self.cell_background_color)
        # TODO : Draw option text.
        return option_surface

    def get_options_surface_size(self, option_width, option_height):
        """
        :param option_width:
        :param option_height:
        :returns:
        """
        n = len(self.options)
        surface_width = option_width
        surface_height = option_height
        total_padding = self.cell_padding * (n - 2)
        if self.isVertical():
            surface_height *= n
            surface_height += total_padding
        else:
            surface_width *= n
            surface_width += total_padding
        return (surface_width, surface_height)

    def get_options_surface(self, parent_surface_width):
        """
        :param parent_surface_width:
        :returns:
        """
        if self._options_surface is None:
            text_sizer = self.font_manager.primary
            option_width = get_longest(self.options, text_sizer)
            option_height = get_highest(self.options, text_sizer)
            option_surface_size = (option_width, option_height)
            options_surface_size = self.get_options_surface_size(
                option_surface_size)
            if options_surface_size[0] > parent_surface_width:
                # TODO : Warning.
                pass
            self._options_surface = self.create_surface(options_surface_size)
            for option in self.options:
                option_surface = self.get_option_surface(
                    option,
                    option_surface_size)
                # TODO : Blit to surface.
        return self._options_surface

    def draw(self, surface):
        """Drawing method, display centered label and options list below.

        :param surface: Surface to draw this screen into.
        """
        super(SelectScreen, self).draw(surface)
        surface_width, surface_height = surface.get_size()
        message_surface = self.get_message_surface(surface_width)
        options_surface = self.get_options_surface(surface_width)


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
    label = screen_def[XML_LABEL]
    options = screen_def[XML_OPTION]
    if not isinstance(options, list):
        raise AttributeError('At least two options is required')
    # TODO : Parse optional padding
    return SelectScreen(screen_def[XML_NAME], message, options)
