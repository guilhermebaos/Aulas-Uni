def conta_hashtags(string: str):
    hashtags_index = []
    for index, item in enumerate(string):
        if item == '#':
            hashtags_index += [index]

    words = []
    for index in range(len(hashtags_index)):
        start = hashtags_index[index]
        try:
            end = hashtags_index[index + 1]
            new_word = string[start:end]
        except IndexError:
            new_word = string[start:]
        if new_word not in words:
            words += [new_word]
    return len(words)


assert conta_hashtags("#christmas#2019#newyear") == 3
assert conta_hashtags("#christmas#2019#newyear#new#year#christmas") == 5
