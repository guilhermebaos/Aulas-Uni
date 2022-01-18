def max_cycle_length(l):
    len_l = len(l)

    # Set of all lengths found
    all_lens = set()
    for n in range(len_l):
        length = 0
        x = n

        # Do a cycle and save its length
        while True:
            x = l[x]
            length += 1
            if x == n:
                break
        all_lens.add(length)

    return max(all_lens)


assert max_cycle_length([0, 3, 1, 6, 2, 4, 5, 9, 7, 8]) == 6
