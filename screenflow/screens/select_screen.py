##!/usr/bin/python

""" To document """

from screenflow.screens import Screen

class SelectScreen(Screen):
    """To document.
    """

    def __init__(self, label, options):
        """Default constructor.

        :param label:
        :param options:
        """
        Screen.__init__(self)
        self.label = label
        self.options = options

