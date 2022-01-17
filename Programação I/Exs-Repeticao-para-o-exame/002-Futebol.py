def futebol(scores):
    results = dict()
    for game in scores:
        team1, team2 = list(game.keys())

        if game[team1] > game[team2]:
            points1 = 3
            points2 = 0
        elif game[team1] < game[team2]:
            points1 = 0
            points2 = 3
        else:
            points1, points2 = 1, 1

        results[team1] = results.get(team1, 0) + points1
        results[team2] = results.get(team2, 0) + points2

    return results


assert futebol([{"Vitória SC": 2, "Boavista": 1}, {"Gil Vicente": 1, "Rio Ave": 1},
                {"Famalicão": 3, "Sporting": 2}, {"FC Porto": 0, "Benfica": 0},
                {"Tondela": 2, "Santa Clara": 3}]) == {'Vitória SC': 3, 'Boavista': 0, 'Gil Vicente': 1, 'Rio Ave': 1,
                                                       'Famalicão': 3,
                                                       'Sporting': 0, 'FC Porto': 1, 'Benfica': 1, 'Santa Clara': 3,
                                                       'Tondela': 0}
