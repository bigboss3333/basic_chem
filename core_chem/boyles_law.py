"""Boyle's Law Calculations"""


def calculate_boyles_law(
    pressure_one=None, volume_one=None, pressure_two=None, volume_two=None
) -> float:
    """When temperature is constant: P1V1 = P2V2. This function takes any three of these values and
    provides the 4th unknown value.


    :param pressure_one: Initial pressure
    :param volume_one: Initial volume
    :param pressure_two: Subsequent pressure
    :param volume_two: Subsequent volume
    :return: Unknown value
    """
    params = [pressure_one, volume_one, pressure_two, volume_two]
    if len([i for i in params if i is None]) != 1:
        raise ValueError("Only one optional input can be None")
    result = None
    if pressure_one is None:
        result = (pressure_two * volume_two) / volume_one
    elif volume_one is None:
        result = (pressure_two * volume_two) / pressure_one
    elif pressure_two is None:
        result = (pressure_one * volume_one) / volume_two
    elif volume_two is None:
        result = (pressure_one * volume_one) / pressure_two
    return result
