##!/usr/bin/python

"""
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