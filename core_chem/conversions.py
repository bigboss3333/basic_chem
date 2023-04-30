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
    return celsius + 273.15
