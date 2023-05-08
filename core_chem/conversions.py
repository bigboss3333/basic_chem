"""Chemistry Conversion Functions"""


def convert_fahrenheit_to_celsius(degrees_in_fahrenheit: float) -> float:
    """Converts from Fahrenheit to Celsius

    :param degrees_in_fahrenheit: value of degrees in F
    :return: degrees in celsius
    """
    return (degrees_in_fahrenheit - 32) * (5 / 9)


def convert_celsius_to_fahrenheit(degrees_in_celsius: float) -> float:
    """Converts from Celsius to Fahrenheit

    :param degrees_in_celsius:
    :return:
    """
    return (degrees_in_celsius * (9 / 5)) + 32


def convert_celsius_to_kelvins(celsius: float) -> float:
    """Converts from celsius to kelvins

    :param celsius: degrees in celsius
    :return: degrees in kelvins
    """
    return celsius + 273.15


def convert_nanometer_to_picometer(nanometer):
    """Converts nanometers to picometers by multiplying by 1000

    :param nanometer:
    :return: picometer
    """
    return nanometer * 1000


def convert_kilogram_to_milligram(kilogram):
    """convert kilogram to milligram

    :param kilogram:
    :return: milligram
    """
    return kilogram * 1000000
