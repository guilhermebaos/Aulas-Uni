def ppt(l1, l2):
    PEDRA, PAPEL, TESOURA = 'pedra', 'papel', 'tesoura'

    points1, points2 = 0, 0
    for play1, play2 in zip(l1, l2):
        if play1 == play2:
            continue
        win2 = PEDRA if play1 == TESOURA else PAPEL if play1 == PEDRA else TESOURA

        if play2 == win2:
            points2 += 1
        else:
            points1 += 1

    return points1, points2


assert ppt(['papel', 'papel', 'papel', 'tesoura'], ['tesoura', 'papel', 'pedra', 'pedra']) == (1, 2)
