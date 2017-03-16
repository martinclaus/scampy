"""Test basic package setup.

Test functionality provided by the __init__ file of the package.
"""

from unittest import TestCase

import scampy


class TestPackage(TestCase):
    """Test basic package functionality."""

    def test_version_number(self):
        """Test return value of get_version function."""
        self.assertEqual(scampy.get_version(), (0, 0, 1))

    def test_version_string(self):
        """Test composed version string."""
        self.assertEqual(scampy.get_version_string(), "0.0.1")
