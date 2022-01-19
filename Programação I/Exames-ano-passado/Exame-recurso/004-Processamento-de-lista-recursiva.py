def leaf_depth(l, depth=0):
    pairs = []
    if type(l) == str:
        pairs += [(l, depth)]
    else:
        for item in l:
            pairs += leaf_depth(item, depth + 1)
    return pairs


assert leaf_depth([["a", "bc"], "d", [["ef", "gh"], "i"], "j"]) == [("a", 2), ("bc", 2), ("d", 1), ("ef", 3), ("gh", 3), ("i", 2), ("j", 1)]
assert leaf_depth("abc") == [("abc", 0)]
assert leaf_depth([]) == []
