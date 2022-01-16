def hanoi(n: int):
    return n if n == 1 else 2 * hanoi(n - 1) + 1


print(hanoi(3))
print(hanoi(10))
