#!/usr/bin/python

"""
    ScreenFlow
    ==========

    Screen binding
    --------------

    XML loading
    ------------

    Custom screen
    -------------

"""

import logging
import xmltodict
from pygame import time, FULLSCREEN, HWSURFACE, DOUBLEBUF
from pygame.display import set_mode, flip, Info
from screens import configure_screenflow
from constants import XML_SCREENFLOW, XML_SCREEN, XML_TYPE
from font_manager import FontManager
from style_factory import StyleFactory

# Configure logger.
logging.basicConfig()
logger = logging.getLogger(__name__)


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
        self.__previews = previews
        self.__side = side
        self.__speed = side * speed
        self.__position = 0
        if side == ScreenTransition.FORWARD:
            self.__position = previews[0].get_size()[0]

    def update(self, surface):
        """Performs a transition iteration over internal screen previews.

        :param surface: Surface to draw transition in.
        :returns: True is the transition worked, False if already finished.
        """
        self.__position += self.__speed
        size = surface.get_size()[0]
        if self.__position < 0 or self.__position > size:
            return False
        surface.blit(self.__previews[0], (self.__position - size, 0))
        surface.blit(self.__previews[1], (self.__position, 0))
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
        self.__screens = {}
        self.__factories = {}
        self.__style_factory = StyleFactory()
        self.__font_manager = FontManager()
        configure_screenflow(self)
        self.__running = False
        self.__stack = []
        self.__state = ScreenFlow.CREATING
        self.__surface = surface
        self.__transition = None

    @property
    def surface(self):
        """Surface property getter. If current surface is None,
        it creates a fullscreen surface.

        :returns: Target surface.
        """
        if self.__surface is None:
            logger.info('Target surface not specified')
            logger.info('Creating surface')
            info = Info()
            resolution = (info.current_w, info.current_h)
            flags = FULLSCREEN | HWSURFACE | DOUBLEBUF
            logger.info('Creating surface (%s, %s)' % resolution)
            self.__surface = set_mode(resolution, flags)
        return self._surface

    def add_screen(self, screen):
        """Adds the given screen to this screen flow.

        :param screen: Screen to add to this flow.
        """
        self.__screens[screen.name] = screen
        screen.font_manager = self.__font_manager
        screen.configure_screen_styles(self.__style_factory)

    def __getattr__(self, name):
        """Attribute access overloading, allow to access
        flow screens by name indexing.

        :param name: Name of the attribute to retrieve.
        :returns:
        :raise AttributeError:
        """
        if name in self.__screens.keys():
            return self.__screens[name]
        raise AttributeError('Unknown screen %s' % name)

    def set_transition(self, previews, side):
        """Sets this flow as in transition using given previews and side.

        :param previews: Screen previews to use in built transition.
        :param side: Transition side.
        """
        self.__transition = ScreenTransition(previews, side)
        self.__state = ScreenFlow.IN_TRANSITION

    def quit(self):
        """Stops the execution of this screenflow. """
        self.__running = False

    def navigate_to(self, screen):
        """Creates and returns a transition callback function.

        Created function will perform a screen transition from
        the current one to the given screen instance.

        :param screen: Screen to navigate to.
        :returns: Created callback function.
        """
        size = self.surface.get_size()
        previews = (
            self.surface.copy(),
            screen.generate_preview(size))
        self.__stack.append(screen)
        self.set_transition(previews, ScreenTransition.FORWARD)

    def navigate_back(self):
        """Creates and returns a transition callback function.

        Created function will perform a screen transition from
        the current one to one before in the screen stack.

        :returns: Created callback function.
        """
        size = self.surface.get_size()
        if len(self.__stack) <= 1:
            raise NavigationException('Cannot navigate back, no more screen.')
        self.__stack.pop()
        previews = (self.get_current_screen().generate_preview(size),
                    self.surface.copy())
        self.set_transition(previews, ScreenTransition.BACKWARD)

    def get_current_screen(self):
        """Current screen access method.

        :returns: Current screen displayed.
        """
        if len(self.__stack) == 0:
            raise IndexError('Screen stack is empty')
        return self.__stack[-1]

    def draw(self):
        """ Draws the current screen into the delegate surface."""
        self.get_current_screen().draw(self.__surface)

    def run(self, start_screen):
        """Starts this screen flow and maintains
        a main loop over it until application is killed
        or quit() callback is reached.
        """
        self.__stack.append(start_screen)
        self.draw()
        self.__running = True
        self.__state = ScreenFlow.ACTIVE
        while self.__running:
            flip()
            current = self.get_current_screen()
            if self.__state == ScreenFlow.IN_TRANSITION:
                if not self.__transition.update(self.__surface):
                    self.__transition = None
                    self.__state = ScreenFlow.ACTIVE
                    self.draw()
                    current.on_screen_activated()
            elif self.__state == ScreenFlow.ACTIVE:
                self.__running = current.process_event()

    def register_factory(self, type_name, factory):
        """Registers the given factory for the given type.

        :param type_name: Type name to registered factory under.
        :param factory: Factory function used for creating associated type.
        """
        if type_name in self.__factories.keys():
            raise ValueError('Screen type %s already registered' % type_name)
        self.__factories[type_name] = factory

    def create_screen(self, screen_def):
        """Factory method that creates a screen from the given definition.

        :param screen_def: Screen definition as a dictionary from XML parsing.
        """
        if XML_TYPE not in screen_def.keys():
            raise AttributeError('No screen type specified.')
        screen_type = screen_def[XML_TYPE]
        if screen_type not in self.__factories.keys():
            raise ValueError('Unknown screen type %s' % screen_type)
        return self.__factories[screen_type](screen_def)

    def load_style(self, css_file):
        """Loads and configures this screenflow with the given CSS file.

        :param css_file: CSS file to load.
        """
        self.__style_factory.load(css_file)

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
