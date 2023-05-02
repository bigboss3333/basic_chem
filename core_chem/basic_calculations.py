from mendeleev import element


def get_density(mass: float, volume: float) -> float:
    """Given the mass of an object returns the density

    :param volume: Volume of object
    :param mass: Mass of object to calculate density
    :return:  of object
    """
    density = mass / volume
    return density


def calculate_percent_composition_elemental(
    number_of_moles: int, element_id: str, compound: dict
) -> float:
    """Calculates the percent composition of an element =


    :param compound: Dictionary of isotopes in a compound element:number_of_element
    :param number_of_moles: the number of moles of the element in one mole of the compound
    :param element_id: element to obtain percentage of in compound
    :return: percent composition
    """

    # test2 = compound.items()
    # test1=compound.values()
    # compound_ids = compound.keys()
    # compound_elements = element(compound_ids)
    compound_mass = 0.0
    for elem, num in compound.items():
        compound_mass += element(elem).mass * num
    return (number_of_moles * element(element_id).mass / compound_mass) * 100


def calculate_percent_yield(actual_yield, theoretical_yield):
    """Calculates the percent yield of a reaction

    :param actual_yield: quantity of a product that is obtained from a chemical reaction
    :param theoretical_yield: quantity of a product obtained from the complete conversion of the limiting
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

    if (
        sum(
            i is not None
            for i in [
                molarity_of_starting_solution,
                volume_of_starting_solution_liter,
                molarity_of_end_solution,
                volume_of_end_solution_liter,
            ]
        )
        == 1
    ):
        raise ValueError("Only one optional input can be None")

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
    else:
        raise ValueError("At least one value should be None for this calculation")
    return substance_dilution
