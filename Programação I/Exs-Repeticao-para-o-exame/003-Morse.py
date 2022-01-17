morse_code = {
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
}


def morse_number(filename):
    with open(filename, 'r') as file:
        morse = file.read().split()

    number = ''
    for digit in morse:
        number += morse_code[digit]
    return int(number)


assert morse_number("cem.txt") == 100
