##!/usr/bin/python

""" To document """

from screenflow.screens import Screen

class SplashScreen(Screen):
    """ To document """

    def __init__(self, delay):
        """
        :param delay:
        """
        Screen.__init__(self)
        self.delay = delay

    def on_screen_activated(self):
        """ Callback method for screen activation pre processing. """
        # TODO : Trigger timer using internal delay value.
        pass

    def draw(self, surface):
        """
        :param surface:
        """
        pass
