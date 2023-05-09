"""Basic Chemistry Calculations"""
from mendeleev import element

from core_chem import AVAGADROS_NUMBER, get_sig_figures, round_to_sig_figs


def get_density(mass: float, volume: float) -> float:
    """Given the mass of an object returns the density

    :param volume: Volume of object
    :param mass: Mass of object to calculate density
    :return:  of object
    """
    density = mass / volume
    sig_figs = get_sig_figures([mass, volume])
    return round_to_sig_figs(density, sig_figs)


def get_occupied_volume(mass: float, density: float) -> float:
    """Given the mass of an object and density returns the volume displaced

    :param mass: mass of object
    :param density: density of object to calculate volume displaced    :return:  by object
    """
    return density * mass


def calculate_percent_composition_elemental(
    number_of_moles: int, element_id: str, compound: dict
) -> float:
    """Calculates the percent composition of an element


    :param compound: Dictionary of isotopes in a compound element:number_of_element
    :param number_of_moles: the number of moles of the element in one mole of the compound
    :param element_id: element to obtain percentage of in compound
    :return: percent composition
    """

    compound_mass = 0.0
    for elem, num in compound.items():
        compound_mass += element(elem).mass * num
    return (number_of_moles * element(element_id).mass / compound_mass) * 100


def calculate_mass_elemental_compound(number_of_moles: int, compound: dict) -> float:
    """Calculates the mass of an elemental compound.


    :param compound: Dictionary of isotopes in a compound element:number_of_element
    :param number_of_moles: the number of moles of the element in one mole of the compound
    :return: mass in grams
    """

    compound_mass = 0.0
    for elem, num in compound.items():
        compound_mass += element(elem).mass * num
    return compound_mass * number_of_moles


def calculate_moles_of_compound_from_mass(mass: float, compound: dict):
    """calculate moles of compound from mass

    :param mass: mass in grams
    :param compound: The elemental compound
    :return: moles of compound
    """
    return mass / calculate_mass_elemental_compound(1, compound)


def calculate_atoms_of_compound_from_mass(mass: float, compound: dict):
    """calculate atoms of compound from mass

    :param mass: mass in grams
    :param compound: The elemental compound
    :return: moles of compound
    """
    moles_of_compound = mass / calculate_mass_elemental_compound(1, compound)

    return moles_of_compound * AVAGADROS_NUMBER


def calculate_moles_of_compound_from_molecules(molecules: float, compound: dict):
    """calculate atoms of compound from mass

    :param molecules: molecules
    :param compound: The elemental compound
    :return: moles of compound
    """
    moles = molecules / AVAGADROS_NUMBER
    return calculate_mass_elemental_compound(moles, compound)


def calculate_percent_yield(actual_yield, theoretical_yield):
    """Calculates the percent yield of a reaction

    :param actual_yield: quantity of a product that is obtained from a chemical reaction
    :param theoretical_yield: quantity of a product obtained from the complete
           conversion of the limiting
    reactant in a chemical reaction
    :return: percent yield of reaction
    """
    return (actual_yield / theoretical_yield) * 100


def calculate_molarity(moles_of_solute: int, liters_of_solute: float) -> float:
    """Calculates the molarity of a solute

    :param moles_of_solute:
    :param liters_of_solute:
    :return: molarity of solute
    """
    return moles_of_solute / liters_of_solute


def calculate_substance_dilution(
    molarity_of_starting_solution=None,
    volume_of_starting_solution_liter=None,
    molarity_of_end_solution=None,
    volume_of_end_solution_liter=None,
) -> float:
    """Calculates the dilution of a substance.

    :param molarity_of_starting_solution: value in Moles
    :param volume_of_starting_solution_liter: value in liters
    :param molarity_of_end_solution: value in Moles
    :param volume_of_end_solution_liter: value in liters
    :return: substance dilution
    """
    params = [
        molarity_of_starting_solution,
        volume_of_starting_solution_liter,
        molarity_of_end_solution,
        volume_of_end_solution_liter,
    ]
    if len([i for i in params if i is None]) != 1:
        raise ValueError("Only one optional input can be None")
    substance_dilution = None
    if molarity_of_starting_solution is None:
        substance_dilution = (
            molarity_of_end_solution * volume_of_end_solution_liter
        ) / volume_of_starting_solution_liter
    elif volume_of_starting_solution_liter is None:
        substance_dilution = (
            molarity_of_end_solution * volume_of_end_solution_liter
        ) / molarity_of_starting_solution
    elif molarity_of_end_solution is None:
        substance_dilution = volume_of_end_solution_liter / (
            molarity_of_starting_solution * volume_of_starting_solution_liter
        )
    elif volume_of_end_solution_liter is None:
        substance_dilution = molarity_of_end_solution / (
            molarity_of_starting_solution * volume_of_starting_solution_liter
        )
    return substance_dilution
