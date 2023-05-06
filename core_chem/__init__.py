"""Core calculations for basic chemistry applications"""
from typing import Any
import scipy.constants

AVAGADROS_NUMBER = scipy.constants.physical_constants["Avogadro constant"][0]


def get_sig_figures(values: list[Any]) -> int:
    """Returns the number of significant figures in a float

    :param values:
    :return: Returns the number of significant figures in a float
    """
    # TODO a lot of yucky code here that requires clean up
    figures = 10000
    for value in values:
        if value is None:
            continue
        try:
            greater_than_one, less_than_one = str(value).split(".")
        except ValueError:
            greater_than_one = str(value).rstrip("0")
            less_than_one = ""
        number_as_list_char = [*greater_than_one]
        if greater_than_one == "0":
            number_as_list_char = []
        numbers_as_list_char2 = [*less_than_one]
        all_zero = True
        new_list = []
        if len(number_as_list_char) == 0:
            for digit in numbers_as_list_char2:
                if digit != "0":
                    all_zero = False
                if not all_zero:
                    new_list.append(digit)
        else:
            new_list = numbers_as_list_char2
        figs = len(number_as_list_char) + len(new_list)
        if figs < figures:
            figures = figs
    return figures
