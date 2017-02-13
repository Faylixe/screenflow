##!/usr/bin/python

""" To document """

from pygame_screenflow import Screen

class InputScreen(Screen):
    """To document.
    """

    def __init__(self, label, input_type='text'):
        """Default constructor.

        :param label:
        :param input_type:
        """
        Screen.__init__(self)
        self.label = label
        self.input_type = input_type

