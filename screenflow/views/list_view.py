
class ItemViewRenderer(object):
    """ Item view rendering class. """

    def __init__(self):
        """Default constructor. """
        pass

    def render(self, item, surface):
        """

        :param item:
        :param surface:
        """

    def get_expected_item_size(self, parent_size):
        """Computes and returns expected item size relative to the given parent one.

        :param parent_size: Size of the parent surface.
        :returns:
        """
        pass

""" """
PRELOAD_FACTOR = 1

class ListView(object):
    """A ListView is a graphical component that aims to display a list of item.
    It uses recycler pattern to avoid creating useless surface for each item.
    """

    def __init__(self, surface, renderer):
        """Default constructor.

        :param surface:
        :param renderer:
        """
        self.surface = surface
        self.items = []
        list_size = surface.get_size()
        item_size = renderer.get_expected_item_size(list_size)
        self.visible_view = int(floor(list_size / item_size)) + (PRELOAD_FACTOR * 2)
        self.views = [pygame.Surface(item_size) for _ in range(self.visible_view)]
        self.current_position = 0

    def on_model_change(self, model):
        """

        :param model:
        """
        for item in model:
            pass