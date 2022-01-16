def calc_luhn_digit(code):
    n = 0
    len_code = len(code)
    for index, item in enumerate(code):
        index = len_code - index
        item = int(item)
        if index % 2 == 0:
            n += item
        else:
            n += item * 2 if item * 2 <= 9 else item * 2 - 9
    return 9 * n % 10


assert calc_luhn_digit('12345') == 5
