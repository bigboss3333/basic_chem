def get_sig_figures(values):
    figures = 10000
    for value in values:
        if value is None:
            continue
        float(value)
        greater_than_one, less_than_one = str(value).split('.')
        greater_than_one = greater_than_one.rstrip('0')
        less_than_one = less_than_one.rstrip('0')
        number_as_list_char = [*greater_than_one]
        numbers_as_list_char2 = [*less_than_one]
        figs = len(number_as_list_char)+len(numbers_as_list_char2)
        if figs < figures:
            figures = figs
    return figures