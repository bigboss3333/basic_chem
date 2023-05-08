"""Tests Boyle's Law"""
from unittest import TestCase

from core_chem.boyles_law import calculate_boyles_law


class TestBoylesLaw(TestCase):
    """Tests Boyle's Law"""

    def testfunction(self):
        """Tests Boyle's Law"""
        with self.assertRaises(ValueError):
            calculate_boyles_law(1, 2, None, None)
        self.assertEqual(calculate_boyles_law(1, 2, 3, None), 0.6666666666666666)
        self.assertEqual(calculate_boyles_law(1, 2, None, 4), 0.5)
        self.assertEqual(calculate_boyles_law(1, None, 3, 4), 12)
        self.assertEqual(calculate_boyles_law(None, 2, 3, 4), 6.0)
