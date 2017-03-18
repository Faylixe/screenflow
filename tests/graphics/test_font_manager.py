#!/usr/bin/python

""" Simple test suite for FontManager class. """

import pytest
from mocks.mock_font_manager import MockFontManager


class TestFontManager(object):
    """ Test suite for EventManager class. """

    @pytest.fixture
    def font_manager(self):
        return MockFontManager()

    def test_get(self, font_manager):
        """ FontManager access test case. """
        font = font_manager.get('arial', 20)
        assert font == font_manager.get('arial', 20)
        assert font != font_manager.get('arial', 30)
