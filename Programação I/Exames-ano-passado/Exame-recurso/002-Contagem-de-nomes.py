import string


def count_names(text):
    words = text.split()

    names = set()
    for w in words:
        if len(w) >= 2 and w[0] in string.ascii_uppercase:
            is_name = True
            for letter in w[1:]:
                # Check that every letter is lowercase
                is_name &= letter in string.ascii_lowercase

            if is_name:
                names.add(w)
    return len(names)


assert count_names('I saw Sally and Wendy last wednesday and Sally had just broken up with Dallas and I went OMG OMG OMG') == 3
