#!/usr/bin/python

""" To document """

import xmltodict
import pygame

from screens import configure_screenflow
from constants import XML_SCREENFLOW, XML_SCREEN, XML_TYPE
from font_manager import FontManager # TODO : Check for cyclic dep here :/

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

class ScreenFlow(FontManager):
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
        super(ScreenFlow, self).__init__()
        configure_screenflow(self)
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
        screen.set_font_manager(self)

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

    def quit(self):
        """Stops the execution of this screenflow. """
        self.running = False

    def navigate_to(self, screen):
        """Creates and returns a transition callback function.

        Created function will perform a screen transition from
        the current one to the given screen instance.

        :param screen: Screen to navigate to.
        :returns: Created callback function.
        """
        previews = (self.stack[-1].generate_preview(), screen.generate_preview())
        self.stack.append(screen)
        self.set_transition(previews, ScreenTransition.FORWARD)

    def navigate_back(self):
        """Creates and returns a transition callback function.

        Created function will perform a screen transition from
        the current one to one before in the screen stack.

        :returns: Created callback function.
        """
        if len(self.stack) == 1:
            raise NavigationException('Cannot navigate back, no more screen.')
        screen = self.stack.pop()
        previews = (self.stack[-1].generate_preview(), screen.generate_preview())
        self.set_transition(previews, ScreenTransition.FORWARD)

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
        del self.stack[:]
        self.running = True
        while self.running:
            pygame.display.flip()
            current = self.get_current_screen()
            if self.state == ScreenFlow.IN_TRANSITION:
                if not self.transition.update(self.surface):
                    self.transition = None
                    self.state = ScreenFlow.ACTIVE
                    current.on_screen_activated()
            elif self.state == ScreenFlow.ACTIVE:
                current.process_event()

    def register_factory(self, type_name, factory):
        """Registers the given factory for the given type.

        :param type_name: Type name to registered factory under.
        :param factory: Factory function used for creating associated screen type instance.
        """
        if type_name in self.factories.keys():
            raise ValueError('Screen type %s already registered' % type_name)
        self.factories[type_name] = factory

    def create_screen(self, screen_def):
        """Factory method that creates a screen from the given definition.

        :param screen_def: Screen definition as a dictionary from XML parsing.
        """
        if XML_TYPE not in screen_def.keys():
            raise AttributeError('No screen type specified.')
        screen_type = screen_def[XML_TYPE]
        if screen_type not in self.factories.keys():
            raise ValueError('Unknown screen type %s' % screen_type)
        return self.factories[screen_type](screen_def)

    def load_from_file(self, flow_file):
        """Factory function that creates a ScreenFlow instance from
        the given XML file.

        :param file: Target XML file to load screens from.
        """
        with open(flow_file, 'r') as stream:
            xml = stream.read()
            content = xmltodict.parse(xml)
            if XML_SCREENFLOW not in content.keys():
                raise AttributeError('No screenflow root element found')
            screenflow_def = content[XML_SCREENFLOW]
            if XML_SCREEN not in screenflow_def.keys():
                raise AttributeError('No screen definition found')
            screens = screenflow_def[XML_SCREEN]
            if isinstance(screens, list):
                for screen in screens:
                    self.add_screen(self.create_screen(screen))
            else:
                self.add_screen(self.create_screen(screens))
