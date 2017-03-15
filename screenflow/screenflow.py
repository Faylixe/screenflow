#!/usr/bin/python

"""
    ScreenFlow
    ==========

    ScreenFlow class is the library entry point, which implements all the logic
    to manages event, handles screen creation, and so on.

    Screen binding
    --------------

    Each screen belonging to your screenflow can be retrieved using
    attribute binding. Let say you added a screen with name *foo* in
    a given screenflow instance, such screen could be accessed as following :

    .. code-block:: python

        screenflow.foo

    XML loading
    ------------

    ScreenFlow allows you to define your screens by using XML format
    using following convention :

    .. code-block:: xml

        <?xml version="1.0"?>
        <screenflow>
            <!-- Your screens here-->
        </screenflow>

    Where each screen is defined as following :

     .. code-block:: xml

        <screen name="screen_name" type="screen_type">
            <!-- Your screen specific parameter here -->
        </screen>

    The *name* attribute will be used for attribute binding. Checkout
    available screens documentation to know what parameter can be settled.

    Custom screen
    -------------

    You can implements your own screen by extending the Screen base class.
    Although for screenflow to recognize your screen implementation when
    parsing an XML file, you should register a factory function.

    Such factory function should match the following signature :

    .. code-block:: python

        def my_factory(screen_def):
            my_screen = ... // Create your screen instance here.
            return my_screen

    Where *screen_def* parameter is a dictionary from xmltodict parsing
    library. Then registering such function is as easy as following :

    .. code-block:: python

        screenflow = ScreenFlow()
        screenflow.register_factory('type_name', my_factory)

"""

import logging
import xmltodict
from constants import XML_SCREENFLOW, XML_SCREEN, XML_TYPE
from font_manager import FontManager
from screens import configure_screenflow
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
        self._previews = previews
        self._side = side
        self._speed = side * speed
        self._position = 0
        if side == ScreenTransition.FORWARD:
            self._position = previews[0].get_size()[0]

    def update(self, surface):
        """Performs a transition iteration over internal screen previews.

        :param surface: Surface to draw transition in.
        :returns: True is the transition worked, False if already finished.
        """
        self._position += self._speed
        size = surface.get_size()[0]
        if self._position < 0 or self._position > size:
            return False
        surface.blit(self._previews[0], (self._position - size, 0))
        surface.blit(self._previews[1], (self._position, 0))
        return True


class ScreenFlow(object):
    """ To document. """

    # Constant that indicates this flow is in creation mode.
    CREATING = -1

    # Constant that indicates this flow is in transition between two screens.
    IN_TRANSITION = 0

    # Constant that indicates this flow is active and a screen is displayed.
    ACTIVE = 1

    def __init__(self, graphics_adapter, surface=None):
        """Default constructor.

        Using by default a fullscreen window instance if a target surface
        is not given.

        :param graphics_adapter:
        :param surface: Optional surface this flow will be rendered into.
        """
        self._screens = {}
        self._factories = {}
        self._style_factory = StyleFactory()
        self._graphics_adapter = graphics_adapter
        self._font_manager = FontManager()
        configure_screenflow(self)
        self._running = False
        self._stack = []
        self._state = ScreenFlow.CREATING
        self._surface = surface
        self._transition = None

    @property
    def surface(self):
        """Surface property getter. If current surface is None,
        it creates a fullscreen surface.

        :returns: Target surface.
        """
        if self._surface is None:
            logger.info('Main surface not specified')
            self._surface = self._graphics_adapter.create_main_surface()
        return self._surface

    def add_screen(self, screen):
        """Adds the given screen to this screen flow.

        :param screen: Screen to add to this flow.
        """
        self._screens[screen.name] = screen
        screen.drawer = self._graphics_adapter.drawer
        screen.event_manager = self._graphics_adapter.event_manager
        screen.configure_styles(self._style_factory)

    def __getattr__(self, name):
        """Attribute access overloading, allow to access
        flow screens by name indexing.

        :param name: Name of the attribute to retrieve.
        :returns: Screen instance denoted by the given name.
        """
        if name in self._screens.keys():
            return self._screens[name]
        raise AttributeError('Unknown screen %s' % name)

    def set_transition(self, previews, side):
        """Sets this flow as in transition using given previews and side.

        :param previews: Screen previews to use in built transition.
        :param side: Transition side.
        """
        self._transition = ScreenTransition(previews, side)
        self._state = ScreenFlow.IN_TRANSITION

    def quit(self):
        """Stops the execution of this screenflow. """
        self._running = False

    def navigate_to(self, screen):
        """Creates and returns a transition callback function.

        Created function will perform a screen transition from
        the current one to the given screen instance.

        :param screen: Screen to navigate to.
        :returns: Created callback function.
        """
        size = self.surface.get_size()
        previews = (
            self._graphics_adapter.drawer.copy(surface),
            screen.generate_preview(size))
        self._stack.append(screen)
        self.set_transition(previews, ScreenTransition.FORWARD)

    def navigate_back(self):
        """Creates and returns a transition callback function.

        Created function will perform a screen transition from
        the current one to one before in the screen stack.

        :returns: Created callback function.
        """
        size = self.surface.get_size()
        if len(self._stack) <= 1:
            raise NavigationException('Cannot navigate back, no more screen.')
        self._stack.pop()
        previews = (self.get_current_screen().generate_preview(size),
                    self._graphics_adapter.drawer.copy(surface))
        self.set_transition(previews, ScreenTransition.BACKWARD)

    def get_current_screen(self):
        """Current screen access method.

        :returns: Current screen displayed.
        """
        if len(self._stack) == 0:
            raise IndexError('Screen stack is empty')
        return self._stack[-1]

    def draw(self):
        """ Draws the current screen into the delegate surface."""
        self.get_current_screen().draw(self._surface)

    def run(self, start_screen):
        """Starts this screen flow and maintains
        a main loop over it until application is killed
        or quit() callback is reached.
        """
        self._stack.append(start_screen)
        self.draw()
        self._running = True
        self._state = ScreenFlow.ACTIVE
        while self._running:
            self._graphics_adapter.flip_display()
            current = self.get_current_screen()
            if self._state == ScreenFlow.IN_TRANSITION:
                if not self._transition.update(self._surface):
                    self._transition = None
                    self._state = ScreenFlow.ACTIVE
                    self.draw()
                    current.on_screen_activated()
            elif self._state == ScreenFlow.ACTIVE:
                self._running = current.process_event()

    def register_factory(self, type_name, factory):
        """Registers the given factory for the given type.

        :param type_name: Type name to registered factory under.
        :param factory: Factory function used for creating associated type.
        """
        if type_name in self._factories.keys():
            raise ValueError('Screen type %s already registered' % type_name)
        self._factories[type_name] = factory

    def create_screen(self, screen_def):
        """Factory method that creates a screen from the given definition.

        :param screen_def: Screen definition as a dictionary from XML parsing.
        """
        if XML_TYPE not in screen_def.keys():
            raise AttributeError('No screen type specified.')
        screen_type = screen_def[XML_TYPE]
        if screen_type not in self._factories.keys():
            raise ValueError('Unknown screen type %s' % screen_type)
        return self._factories[screen_type](screen_def)

    def load_style(self, css_file):
        """Loads and configures this screenflow with the given CSS file.

        :param css_file: CSS file to load.
        """
        self._style_factory.load(css_file)

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
