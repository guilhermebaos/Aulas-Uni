import random


def count_ints(numeros):
    dici = dict()
    for n in numeros:
        dici[n] = dici.get(n, 0) + 1
    return dici


print(count_ints([1, 2, 3, 1]))
print(count_ints([random.randint(0, 100) for _ in range(1000)]))
