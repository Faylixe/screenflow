##!/usr/bin/python

"""
    SelectScreen
    ============

    Description incomming.

    XML definition
    --------------

    .. code-block:: xml

        <screen name="foo" type="select">
            <label>displayed label</label>
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

from screenflow.screens import Screen
from screenflow.constants import XML_NAME


class SelectScreen(Screen):
    """To document.
    """

    def __init__(self, name, label, options):
        """Default constructor.

        :param name:
        :param label:
        :param options:
        """
        super(SelectScreen, self).__init__(name)
        self.label = label
        self.options = options
        self.callback = None

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

    def draw_option(self, surface, bounds, option):
        """
        """
        pass

    def draw(self, surface):
        """Drawing method, display centered label and options list below.

        :param surface: Surface to draw this screen into.
        """
        super(SelectScreen, self).draw(surface)
        # TODO : Draw label (using message screen ?)
        x = 0
        y = 0
        for option in self.options:
            # TODO : Draw option
            bounds = (x, y)
            # TODO : Add size to bound..
            # TODO : Update y
            self.draw_option(surface, bounds, option)

# XML tag for label parameter.
XML_LABEL = 'label'

# XML tag for option parameters.
XML_OPTION = 'option'


def factory(screen_def):
    """ Static factory function for creating a select screen
    from a given XML screen definition.

    :param screen_def: Screen definition as a dictionary from XML parsing.
    :returns: Created select screen instance.
    """
    if XML_LABEL not in screen_def:
        raise AttributeError('No label set in screen definition')
    if XML_OPTION not in screen_def:
        raise AttributeError('No option(s) set in screen definition')
    label = screen_def[XML_LABEL]
    options = screen_def[XML_OPTION]
    if not isinstance(options, list):
        raise AttributeError('At least two options is required')
    return SelectScreen(screen_def[XML_NAME], label, options)
