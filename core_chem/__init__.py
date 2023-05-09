"""Core calculations for basic chemistry applications"""
from typing import Any
import scipy.constants

AVAGADROS_NUMBER = scipy.constants.physical_constants["Avogadro constant"][0]


def get_sig_figures(values: list[Any]) -> int:
    """Returns the number of significant figures in a float

    :param values:
    :return: Returns the number of significant figures in a float
    """
    fig_list = []
    for value in values:
        try:
            # See if it is a float
            greater_than_one, less_than_one = str(value).split(".")
        except ValueError:
            # Otherwise we set up for an integer
            greater_than_one = str(value).rstrip("0")
            less_than_one = ""
        # Convert to a list of chars
        greater_than_one_figure_list = [*greater_than_one]
        less_than_one_figure_list = [*less_than_one]
        # If this number is a fraction of a whole then mark
        # it 0 significant figures and remove leading zeros
        if greater_than_one == "0":
            # If the onse place is a single 0 digit there are no
            # significant figures greater than one
            greater_than_one_figure_list = []
            # Remove 0 after the decimal but before the first non-zero digit
            less_than_one_figure_list = remove_leading_zeros(less_than_one_figure_list)
        fig_list.append(
            len(greater_than_one_figure_list) + len(less_than_one_figure_list)
        )
    return min(fig_list)


def round_to_sig_figs(value_to_round: float, number_sig_figs: int) -> float:
    """Rounds a value to a specific number of significant figures

    :param value_to_round: Input value that needs to be rounded
    :param number_sig_figs:  Number of significant figures to which to round
    :return: rounded value to a specified sig fig
    """
    return float(format(value_to_round, f".{number_sig_figs}g"))


def remove_leading_zeros(less_than_one_figure_list) -> list:
    """removes leading zeros from a list of figures
        i.e. [0,0,0,0,0,0,0,1,2,0,0,3,4]
                Becomes;
            [1,2,0,0,3,4]

    :param less_than_one_figure_list:
    :return: list of significant figures
    """
    all_zero = True
    sig_figs_without_leading_zero = []
    # If there are no significant digitd in the ones place
    #   we need to remove leading zeros
    for digit in less_than_one_figure_list:
        # Only add zeros that occur after the first non-zero digit
        if digit != "0":
            all_zero = False
        if not all_zero:
            sig_figs_without_leading_zero.append(digit)
    return sig_figs_without_leading_zero
