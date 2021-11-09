def most_frequent_pattern(l: list):
    unique = list(set(l))
    frequencies = [l.count(item) for item in unique]

    return unique[frequencies.index(max(frequencies))]


print(most_frequent_pattern([(1, 2), (0, 0), (1, 0), (2, 1), (2, 0), (1, 2), (0, 2), (0, 0), (1, 2), (1, 1), (1, 1)]))
print(most_frequent_pattern([(0, 0), (0, 2), (2, 2), (2, 0), (2, 2), (1, 0), (0, 0), (2, 2), (0, 2), (1, 2), (0, 1)]))
print(most_frequent_pattern([(1, 0, 0), (0, 1, 1), (0, 0, 0), (0, 1, 1), (0, 0, 0), (1, 1, 0), (0, 1, 1), (1, 1, 1), (1, 0, 1), (1, 1, 0)]))
