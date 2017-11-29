# -*- coding: utf-8 -*-

from .context import hebrew_fonts_converter

import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_bwhebb_to_hebrew_conversion(self):
        result = hebrew_fonts_converter.ConvertString("h;".splitlines(), '1')
        self.assertEqual(result, "ה\n")

if __name__ == '__main__':
    unittest.main()
