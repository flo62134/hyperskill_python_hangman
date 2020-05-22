def get_percentage(number: float, round_digits=False):
    percentage = number * 100

    if round_digits is not False:
        percentage = round(percentage, round_digits)
    else:
        percentage = int(percentage)

    return str(percentage) + '%'
