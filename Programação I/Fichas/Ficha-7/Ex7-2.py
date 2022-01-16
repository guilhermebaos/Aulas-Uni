def ocorrencias(txt, c):
    indexes = []
    for index, item in enumerate(txt):
        if item == c:
            indexes += [index]
    return indexes


assert ocorrencias('banana', 'a') == [1, 3, 5]