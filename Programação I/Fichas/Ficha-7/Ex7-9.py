def is_isbn(code):
    len_code = len(code)
    n = 0
    for index, item in enumerate(code[:-1]):
        n += int(item) * (len_code - index)
    n += int(code[-1]) if code[-1].isdigit() else 10
    return n % 11 == 0


assert is_isbn("019510756X")
