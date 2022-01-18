# Converts a puzzle string to a list
def puzzle_to_list(s):
    lines = s.split('\n')[1:-1]
    return [list(l) for l in lines]


# Converts a list to a puzzle string
def list_to_puzzle(l):
    return '\n' + '\n'.join(''.join(line) for line in l) + '\n'


# Gets the positions of a certain element
def get_positions(s, c):
    s = puzzle_to_list(s)

    positions = []
    for y, line in enumerate(s):
        for x, item in enumerate(line):
            if item == c:
                positions += [(y, x)]
    return positions


# Extra Function: Find out if a car is horizontal or not
def is_horizontal(car_positions):
    p1, p2 = car_positions
    if p1[0] == p2[0]:
        return True
    return False


# Extra Function: Return puzzle dimensions
def puzzle_dim(puzzle_list):
    return len(puzzle_list), len(puzzle_list[0])


# Extra Function: Return all coordinates adjacent to this one
def nearby_coordinates(coord, max_y, max_x):
    nearby = []

    # The tuples contain: (y, x, move_to)
    if coord[0] > 0:
        nearby += [(coord[0] - 1, coord[1], 'D')]
    if coord[0] < max_y:
        nearby += [(coord[0] + 1, coord[1], 'U')]
    if coord[1] > 0:
        nearby += [(coord[0], coord[1] - 1, 'R')]
    if coord[1] < max_x:
        nearby += [(coord[0], coord[1] + 1, 'L')]
    return nearby


# Gets all possible moves that can be executed in a certain puzzle state
def possible_moves(s):
    empty_spaces = get_positions(s, ' ')

    s_list = puzzle_to_list(s)
    height, width = puzzle_dim(s_list)

    all_moves = []
    # For every empty space, check al nearby spaces
    for space in empty_spaces:
        nearby = nearby_coordinates(space, height - 1, width - 1)
        for near_y, near_x, move in nearby:
            item = s_list[near_y][near_x]

            # Check if the car can move into this space
            if item != ' ':
                car_coords = get_positions(s, item)
                car_horizontal = is_horizontal(car_coords)

                if move in ['L', 'R'] and car_horizontal:
                    all_moves += [(item, move)]
                elif move in ['U', 'D'] and not car_horizontal:
                    all_moves += [(item, move)]
    return all_moves


def move_car(s, c, d):
    car_coords = get_positions(s, c)
    s_list = puzzle_to_list(s)

    # Move the car up or down
    top = car_coords[0]
    bottom = car_coords[1]
    if d == 'U':
        s_list[bottom[0]][bottom[1]] = ' '
        s_list[top[0] - 1][top[1]] = c
    elif d == 'D':
        s_list[top[0]][top[1]] = ' '
        s_list[bottom[0] + 1][bottom[1]] = c

    # Move the car left or right
    left = car_coords[0]
    right = car_coords[1]
    if d == 'L':
        s_list[right[0]][right[1]] = ' '
        s_list[left[0]][left[1] - 1] = c
    elif d == 'R':
        s_list[left[0]][left[1]] = ' '
        s_list[right[0]][right[1] + 1] = c

    return list_to_puzzle(s_list)


def move_cars(p, moves):
    for m in moves:
        p = move_car(p, m[0], m[1])
    return p


def is_solution(s):
    x_car_coords = get_positions(s, 'X')
    height, width = puzzle_dim(puzzle_to_list(s))

    # Check if the X car is next to the right side of the puzzle
    for pos in x_car_coords:
        if pos[1] == width - 1:
            return True
    return False


def puzzle_solve(s):
    visited = set()

    check_next = [(s, [])]
    while True:
        # Get the current path and state
        current_state, path = check_next.pop()

        # If we've been here, skip checking this board state
        if current_state in visited:
            continue
        visited.add(current_state)

        # Check if we have a solution!
        if is_solution(current_state):
            return path

        # Try every possible move from here
        moves = possible_moves(current_state)
        for m in moves:
            check_next += [(move_cars(current_state, [m]), path + [m])]
