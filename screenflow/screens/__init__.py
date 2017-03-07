#!/usr/bin/python

""" This package exposes all screens implementation available. """

from screen import Screen
from message_screen import MessageScreen, factory as message_screen_factory
from input_screen import InputScreen
from select_screen import SelectScreen

__author__ = "Felix Voituret"

def configure_screenflow(screenflow):
    """Registers all basic screen factory to the given screenflow instance.abs

    :param screenflow: Screenflow to register factory to.
    """
    screenflow.register_factory('message', message_screen_factory)
    screenflow.register_factory('select', None)
    screenflow.register_factory('input', None)
