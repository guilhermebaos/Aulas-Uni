def altern(x):
    str_x = str(x)
    len_x = len(str_x)

    # Separate even and odd indexed characters
    even = [int(str_x[index]) for index in range(0, len_x, 2)]
    odd = [int(str_x[index]) for index in range(1, len_x, 2)]

    # Check all even characters are getting bigger
    for index, item in enumerate(even[:-1]):

        # Otherwise immediately return False
        if item > even[index + 1]:
            return False

    # Check all odd characters are getting smaller
    for index, item in enumerate(odd[:-1]):

        # Otherwise immediately return False
        if item < odd[index + 1]:
            return False

    return True


assert altern(1927273544535371)
assert not altern(1927243544535371)
