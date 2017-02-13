#!/usr/bin/python

""" To document """

import xmltodict
import pygame

from pygame_screenflow import Screen

pygame.init()

class NavigationException(Exception):
    """ Custom exception for navigation issues. """
    pass

class ScreenTransition(object):
    """ Simple class for managing transition between two given screens. """

    # Constant for forward transition.
    FORWARD = -1

    # Constant for backward transition.
    BACKWARD = 1

    def __init__(self, previews, side, speed=5):
        """Default constructor.

        :param previews: Preview of screen to perform transition between.
        :param side: Side of the transition (FORWARD, or BACKWARD)
        :param speed: Option speed in pixel of the performed transition.
        """
        self.previews = previews
        self.side = side
        self.speed = side * speed
        self.position = 0
        if side == ScreenTransition.FORWARD:
            self.position = previews[0].get_size()[0]

    def update(self, surface):
        """Performs a transition iteration over internal screen previews.

        :param surface: Surface to draw transition in.
        :returns: True is the transition worked, False if already finished.
        """
        self.position += self.speed
        size = surface.get_size()[0]
        if self.position < 0 or self.position > size:
            return False
        surface.blit(self.previews[0], (self.position - size, 0))
        surface.blit(self.previews[1], (self.position, 0))
        return True

class ScreenFlow(object):
    """ To document. """

    # Constant that indicates this flow is in creation mode.
    CREATING = -1

    # Constant that indicates this flow is in transition between two screens.
    IN_TRANSITION = 0

    # Constant that indicates this flow is active and a screen is displayed.
    ACTIVE = 1

    def __init__(self, surface=None):
        """Default constructor.

        Using by default a fullscreen window instance if a target surface
        is not given.

        :param surface: Optional surface this flow will be rendered into.
        """
        self.screens = {}
        self.running = False
        self.stack = []
        self.state = ScreenFlow.CREATING
        self.surface = surface
        if self.surface is None:
            info = pygame.display.Info()
            resolution = (info.current_w, info.current_h)
            self.surface = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
        self.transition = None

    def add_screen(self, screen):
        """Adds the given screen to this screen flow.

        :param screen: Screen to add to this flow.
        """
        self.screens[screen.name] = screen

    def __getattr__(self, name):
        """Attribute access overloading, allow to access
        flow screens by name indexing.

        :param name: Name of the attribute to retrieve.
        :returns:
        :raise AttributeError:
        """
        if name in self.screens.keys():
            return self.screens[name]
        raise AttributeError('Unknown screen %s' % name)

    def set_transition(self, previews, side):
        """Sets this flow as in transition using given previews and side.

        :param previews: Screen previews to use in built transition.
        :param side: Transition side.
        """
        self.transition = ScreenTransition(previews, side)
        self.state = ScreenFlow.IN_TRANSITION

    def navigate_to(self, screen):
        """Creates and returns a transition callback function.

        Created function will perform a screen transition from
        the current one to the given screen instance.

        :param screen: Screen to navigate to.
        :returns: Created callback function.
        """
        def delegate():
            """ Delegate function. """
            previews = (self.stack[-1].generate_preview(), screen.generate_preview())
            self.stack.append(screen)
            self.set_transition(previews, ScreenTransition.FORWARD)
        return delegate

    def navigate_back(self):
        """Creates and returns a transition callback function.

        Created function will perform a screen transition from
        the current one to one before in the screen stack.

        :returns: Created callback function.
        """
        def delegate():
            """ Delegate function. """
            if len(self.stack) == 1:
                raise NavigationException('Cannot navigate back, no more screen.')
            screen = self.stack.pop()
            previews = (self.stack[-1].generate_preview(), screen.generate_preview())
            self.set_transition(previews, ScreenTransition.FORWARD)
        return delegate

    def get_current_screen(self):
        """Current screen access method.

        :returns: Current screen displayed.
        """
        return self.stack[-1]

    def run(self):
        """Starts this screen flow and maintains
        a main loop over it until application is killed
        or quit() callback is reached.
        """
        self.running = True
        while self.running:
            pygame.display.flip()
            current = self.get_current_screen()
            if self.state == ScreenFlow.IN_TRANSITION:
                if not self.transition.update(self.surface):
                    self.transition = None
                    self.state = ScreenFlow.ACTIVE
            elif self.state == ScreenFlow.ACTIVE:
                current.process_event()

    def quit(self):
        """ Creates and returns a callback function for stopping the application.

        :returns: Created callback function.
        """
        def delegate():
            """ Delegate function. """
            self.running = False
        return delegate

    def load_from_file(self, flow_file):
        """Factory function that creates a ScreenFlow instance from
        the given XML file.

        :param file:
        :returns:
        """
        screenflow = ScreenFlow()
        with open(flow_file, 'r') as stream:
            xml = stream.read()
            # TODO : Perform xml validation through schema.
            content = xmltodict.parse(xml)
            screens = content['screenflow']['screen']
            if isinstance(screens, list):
                for screen in screens:
                    self.add_screen(Screen.create(screen))
            else:
                self.add_screen(Screen.create(screens))
        return screenflow
