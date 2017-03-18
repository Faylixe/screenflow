#!/usr/bin/python

""" Simple test suite for Drawer class. """

import pytest
from tests.mocks.mock_drawer import MockDrawer

# Test surface size.
TEST_SIZE = (50, 50)


class TestDrawer(object):
    """ Test suite for Drawer class. """

    @pytest.fixture
    def drawer(self):
        return MockDrawer()

    def test_create_surface(self, drawer):
        """ Test case for create_surface method. """
        surface = drawer.create_surface(TEST_SIZE)
        size = surface.get_size()
        assert size[0] == TEST_SIZE[0]
        assert size[1] == TEST_SIZE[1]

    def test_fill_surface(self, drawer):
        """ Test case for fill_surface method. """
        surface = drawer.create_surface(TEST_SIZE)

    def test_blit_surface(self, drawer):
        """ Test case for blit_surface method. """
        surface = drawer.create_surface(TEST_SIZE)
        pass

    def test_get_text_surface(self, drawer):
        """ Test case for get_text_surface method. """
        pass
        # surface = drawer.get_text_surface('foo', None)
