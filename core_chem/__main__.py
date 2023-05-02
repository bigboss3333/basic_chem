from core_chem import get_sig_figures
from core_chem.basic_calculations import get_density, calculate_percent_composition_elemental, calculate_percent_yield, \
    calculate_molarity, calculate_substance_dilution
from core_chem.boyles_law import calculate_boyles_law
from core_chem.conversions import convert_fahrenheit_to_celsius, convert_celsius_to_fahrenheit, \
    convert_celsius_to_kelvins


def main():
    print(get_density(mass=0.123, volume=12.0))
    celsius = convert_fahrenheit_to_celsius(degrees_in_fahrenheit=32.0)
    print(convert_celsius_to_fahrenheit(celsius))
    print(convert_celsius_to_kelvins(celsius))
    number_of_moles = 1
    element_id = 'Si'
    compound_id = {'Si': 1, 'O': 2}
    print(calculate_percent_composition_elemental(number_of_moles, element_id, compound_id))
    print(calculate_percent_yield(actual_yield=0.434, theoretical_yield=0.6345))
    print(calculate_molarity(moles_of_solute=1, liters_of_solute=12.1))
    print(calculate_substance_dilution(molarity_of_starting_solution=5,
                                       molarity_of_end_solution=1,
                                       volume_of_end_solution_liter=1))
    print(calculate_boyles_law(pressure_one=100.000, volume_one=80.02, pressure_two=None, volume_two=20.1))
    print(get_sig_figures([1.999, 1.09]))


if __name__ == '__main__':
    main()
