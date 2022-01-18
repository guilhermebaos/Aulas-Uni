prev_states = []
SOLUTION = ((1, 1, 1), (2, 2, 2), (3, 3, 0))


def puzzle_str(puzzle: tuple):
    '''
    Código Normal, abaixo está um one-liner

    string = ''
    for index, row in enumerate(puzzle):
        row = list(map(str, row))
        string += ' '.join(row).replace('0', '_') + '\n' * (0 if index == 2 else 1)
    '''

    return ''.join([' '.join(list(map(str, row))).replace('0', '_') + '\n' * (0 if index == 2 else 1) for index, row in
                    enumerate(puzzle)])


def get_empty_entry(p: tuple):
    for y, row in enumerate(p):
        for x, item in enumerate(row):
            if item == 0:
                return y, x


def puzzle_to_list(p: tuple):
    p_list = []
    for item in p:
        p_list += [list(item)]
    return p_list


# Para adicionar items a tuplos temos de começar com uma lista, porquê?
def list_to_puzzle(l: list):
    p_tuple = []
    for item in l:
        p_tuple += [tuple(x for x in item)]
    return tuple(p_tuple)


def puzzle_move(p: tuple, direction: str):
    # Coordenadas do vazio
    y, x = get_empty_entry(p)

    # Efeito do movimento recebido
    delta_x = -1 if direction == 'L' else 1 if direction == 'R' else 0
    delta_y = -1 if direction == 'U' else 1 if direction == 'D' else 0

    end_y = y + delta_y
    end_x = x + delta_x

    # Se o vazio fosse sair do puzzle, devolver o puzzle em igual estado
    if (not (0 <= end_y <= 2)) or (not (0 <= end_x <= 2)):
        return p

    # Trocar de posição o vazio e o elemento para onde ele iria
    p_list = puzzle_to_list(p)
    save = p_list[end_y][end_x]

    p_list[end_y][end_x] = 0
    p_list[y][x] = save

    p = list_to_puzzle(p_list)
    return p


def puzzle_moves(p: tuple, moves: list):
    q = p[:]
    for m in moves:
        q = puzzle_move(q, m)
    return q


def puzzle_solve_iter(p: tuple, move_list=()):
    global SOLUTION, prev_states

    if p in prev_states:
        return
    prev_states += [p]
    move_list = list(move_list)

    # Ver os movimentos possíveis
    y, x = get_empty_entry(p)
    moves = ['U' if y > 0 else False,
             'D' if y < 2 else False,
             'L' if x > 0 else False,
             'R' if x < 2 else False]
    moves = [m for m in moves if m]

    # Executar o DFS
    to_execute = []
    for m in moves:
        next_p = puzzle_move(p, m)
        if next_p == SOLUTION:
            return move_list + [m]
        to_execute += [[next_p, move_list[:] + [m]]]
    return to_execute


def puzzle_solve(p: tuple):
    global prev_states
    prev_states = []

    execute = [[p, []]]
    while True:
        execute_next = []
        for args in execute:
            output = puzzle_solve_iter(args[0], args[1])

            if not output:
                continue

            # Check if we have a solution
            try:
                try:
                    output[0][1]
                except IndexError:
                    return output
            except TypeError:
                return output
            execute_next += output
        execute = execute_next[:]

p = ((3, 3, 2), (1, 1, 0), (2, 2, 1))
print(puzzle_moves(p, puzzle_solve(p)) == SOLUTION)
p = ((0, 1, 1), (3, 3, 2), (2, 2, 1))
print(puzzle_moves(p, puzzle_solve(p)) == SOLUTION)
p = ((1, 1, 2), (3, 1, 3), (0, 2, 2))
print(puzzle_moves(p, puzzle_solve(p)) == SOLUTION)
p = ((2, 3, 1), (2, 1, 2), (3, 1, 0))
print(puzzle_moves(p, puzzle_solve(p)) == SOLUTION)
p = ((1, 2, 3), (0, 1, 2), (3, 1, 2))
print(puzzle_moves(p, puzzle_solve(p)) == SOLUTION)
p = ((2, 3, 0), (1, 2, 2), (1, 1, 3))
print(puzzle_moves(p, puzzle_solve(p)) == SOLUTION)
p = ((2, 1, 1), (0, 2, 3), (2, 3, 1))
print(puzzle_moves(p, puzzle_solve(p)) == SOLUTION)
p = ((0, 2, 1), (3, 2, 2), (3, 1, 1))
print(puzzle_moves(p, puzzle_solve(p)) == SOLUTION)
p = ((0, 2, 3), (2, 1, 2), (1, 1, 3))
print(puzzle_moves(p, puzzle_solve(p)) == SOLUTION)
p = ((1, 2, 2), (2, 3, 1), (0, 3, 1))
print(puzzle_moves(p, puzzle_solve(p)) == SOLUTION)
