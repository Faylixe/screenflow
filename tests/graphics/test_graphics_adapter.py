#!/usr/bin/python

""" Simple test suite for GraphicsAdapter class. """

import pytest
from mocks.mock_graphics_adapter import MockGraphicsAdapter


class TestGraphicsAdapter(object):
    """ Test suite for GraphicsAdapter class. """

    @pytest.fixture
    def graphics_adapter(self):
        return MockGraphicsAdapter()

    def test_create_main_surface(self, graphics_adapter):
        """ Test case for create_main_surface method. """
        pass

    def test_flip_display(self, graphics_adapter):
        """ Test case for flip_display method. """
        pass
