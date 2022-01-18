def most_frequent_duo(l):
    actors_and_movies = dict()
    for movie in l:
        actors_and_movies[movie[0]] = actors_and_movies.get(movie[0], set()) | {movie[1]}

    actors = list(actors_and_movies.keys())
    duos_lens = dict()
    for index1, actor1 in enumerate(actors):
        for index2, actor2 in enumerate(actors[index1 + 1:]):
            duos_lens[len(actors_and_movies[actor1] & actors_and_movies[actor2])] = (actor1, actor2)

    n = max(int(x) for x in duos_lens.keys())
    return duos_lens[n] + (n,)


print(most_frequent_duo([
("John", "Night of the living dead"),
("John", "Summer days"),
("John", "Winter days"),
("John", "Whatever"),
("Sally", "Night of the living dead"),
("Sally", "Summer days"),
("Sally", "XPTO"),
("Sally", "XYZ"),
("James", "Winter days"),
("James", "Summer days"),
("James", "XPTO"),
("James", "XYZ")
]))
