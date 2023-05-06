"""Get details about elements in the periodic table"""
import argparse

from mendeleev import element, Element


def parse_args() -> argparse.Namespace:
    """Argument parser for the element property getter.

    :return: arguments namespace
    """
    parser = argparse.ArgumentParser(
        prog="element_properties.py",
        description="Given an element ID provides details about the element",
        epilog="https://github.com/bigboss3333/basic_chem",
    )
    parser.add_argument(
        "-i",
        "--element_id",
        help="Element ID in string form.",
        required=True,
    )
    parser.add_argument(
        "-m", "--mass", help="Boolean argument for mass", action="store_true"
    )
    parser.add_argument(
        "-e",
        "--electrons",
        help="Boolean argument for number of electrons",
        action="store_true",
    )
    parser.add_argument(
        "-b",
        "--boiling_point",
        help="Boolean argument for boiling point in Kelvins",
        action="store_true",
    )
    return parser.parse_args()


def get_element_mass(element_object: Element) -> float:
    """Returns the mass of the element object

    :param element_object:
    :return: element's mass
    """
    return element_object.mass


def get_element_electron(element_object: Element) -> int:
    """Returns the number of electrons for the element object

    :param element_object:
    :return: element's electron
    """
    return element_object.electrons


def get_element_boiling_point(element_object: Element) -> float:
    """Returns the boiling point in Kelvins for the element object

    :param element_object:
    :return: element's electron
    """
    return element_object.boiling_point


def main():
    """Main function for element_properties"""
    args = parse_args()
    user_element_request = element(args.element_id)
    if args.mass:
        print(get_element_mass(user_element_request))
    if args.electrons:
        print(get_element_electron(user_element_request))
    if args.boiling_point:
        print(get_element_boiling_point(user_element_request))


if __name__ == "__main__":
    main()
