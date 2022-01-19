def expand(x):
    str_x = str(x)
    len_x = len(str_x)
    digits = [str_x[index] for index in range(0, len_x, 2)]
    times = [str_x[index] for index in range(1, len_x, 2)]

    new_number = ''
    for d, t in zip(digits, times):
        new_number += d * int(t)
    return int(new_number)


assert expand(12341004) == 1133330000
assert expand(74839162) == 7777888966
