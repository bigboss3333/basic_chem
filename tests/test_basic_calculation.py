"""Test suit for basic calculations"""
from unittest import TestCase

from core_chem import get_sig_figures
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
        """test_calculate_mass_elemental_compound"""
        glucose = {"C": 6, "H": 12, "O": 6}
        # Calculate 1 moles of glucose
        mass = calculate_mass_elemental_compound(1, glucose)
        self.assertEqual(mass, 180.156)
        # Calculate 2 moles of glucose
        mass = calculate_mass_elemental_compound(2, glucose)
        self.assertEqual(mass, 360.312)

    def test_significant_figure(self):
        """Test number of significant figures"""

        # *True significant figure examples*
        # Significant if non zero
        self.assertEqual(get_sig_figures([4.5]), 2)
        self.assertEqual(get_sig_figures([122.35]), 5)
        # One or more zeros between non zero digits
        self.assertEqual(get_sig_figures([205]), 3)
        self.assertEqual(get_sig_figures([5.008]), 4)
        # One or more zeros at the end of a decimal number

        # 50. Needs to be a string because python would add 0 after . making it 50.0
        self.assertEqual(get_sig_figures(["50."]), 2)
        self.assertEqual(get_sig_figures([25.0]), 3)

        # For trailing 0 that are considered significant you must use
        #   a string or format with "%.2f"
        test = "%.2f" % 16.00
        self.assertEqual(get_sig_figures([test]), 4)

        # *Non-Significant figure examples*

        # Zeros at teh beginning of a decimal number
        self.assertEqual(get_sig_figures([0.0004]), 1)
        self.assertEqual(get_sig_figures([0.075]), 2)
        self.assertEqual(get_sig_figures([850000]), 2)
        self.assertEqual(get_sig_figures([1250000]), 3)
        sig_figs = get_sig_figures([1250000, "50."])
        formatted_results = format(125.01 + 50.0, f".{sig_figs}g")
        self.assertEqual("1.8e+02", formatted_results)
        self.assertEqual(get_sig_figures([1250000, "50."]), 2)
        # Very large numbers need to be strings because python converts to scientific notation
        self.assertEqual(get_sig_figures(["0.0000002501"]), 4)
