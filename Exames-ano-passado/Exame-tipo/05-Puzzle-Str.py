def puzzle_str(puzzle: tuple):
    '''
    Código Normal, abaixo está um one-liner

    string = ''
    for index, row in enumerate(puzzle):
        row = list(map(str, row))
        string += ' '.join(row).replace('0', '_') + '\n' * (0 if index == 2 else 1)
    '''
    
    return ''.join([' '.join(list(map(str, row))).replace('0', '_') + '\n' * (0 if index == 2 else 1) for index, row in enumerate(puzzle)])


SOLUTION = ((1, 1, 1), (2, 2, 2), (3, 3, 0))
print(puzzle_str(SOLUTION))
print(puzzle_str(((0, 1, 2), (2, 1, 3), (1, 2, 3))))
