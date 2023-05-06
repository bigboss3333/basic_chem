"""Test suit for basic calculations"""
from unittest import TestCase

from core_chem.basic_calculations import (
    calculate_substance_dilution,
    calculate_molarity,
    calculate_percent_yield,
    calculate_percent_composition_elemental,
    calculate_mass_elemental_compound,
)


class TestBasicCalculation(TestCase):
    """Class for testing basic calculations"""

    def test_calculate_substance_dilution(self):
        """Calculates substance dilution"""
        result = calculate_substance_dilution(
            molarity_of_starting_solution=5,
            molarity_of_end_solution=1,
            volume_of_end_solution_liter=1,
        )
        self.assertEqual(result, 0.2)
        with self.assertRaises(ValueError):
            calculate_substance_dilution(
                molarity_of_starting_solution=5,
                volume_of_starting_solution_liter=1,
                molarity_of_end_solution=1,
                volume_of_end_solution_liter=1,
            )
        result = calculate_substance_dilution(
            molarity_of_starting_solution=5,
            volume_of_starting_solution_liter=1,
            molarity_of_end_solution=1,
        )
        self.assertEqual(result, 0.2)
        result = calculate_substance_dilution(
            volume_of_starting_solution_liter=1,
            molarity_of_end_solution=1,
            volume_of_end_solution_liter=1,
        )
        self.assertEqual(result, 1.0)
        result = calculate_substance_dilution(
            molarity_of_starting_solution=5,
            volume_of_starting_solution_liter=1,
            volume_of_end_solution_liter=1,
        )
        self.assertEqual(result, 0.2)

    def test_calculate_molarity(self):
        """tests calculate molarity

        :return: Nothing
        """
        self.assertEqual(calculate_molarity(5, 1.5), 3.3333333333333335)

    def test_calculate_percent_yield(self):
        """tests calculate percent yield

        :return: Nothing
        """
        self.assertEqual(calculate_percent_yield(1, 12), 8.333333333333332)

    def test_calculate_percent_composition_elemental(self):
        """tests calculate percent composition elemental

        :return: Nothing
        """
        test_compound = {"Cl": 1}
        result = calculate_percent_composition_elemental(1, "Cl", test_compound)
        self.assertEqual(result, 100.0)

    def test_calculate_mass_elemental_compound(self):
        glucose = {"C": 6, "H": 12, "O": 6}
        # Calculate 1 moles of glucose
        mass = calculate_mass_elemental_compound(1, glucose)
        self.assertEqual(mass, 180.156)
        # Calculate 2 moles of glucose
        mass = calculate_mass_elemental_compound(2, glucose)
        self.assertEqual(mass, 360.312)
