def it_collatz(i):
    count = 0
    while True:
        if i == 1:
            return count
        elif i % 2 == 0:
            i //= 2
        else:
            i = 3 * i + 1
        count += 1


print(it_collatz(1))
print(it_collatz(7))
print({i: it_collatz(i) for i in range(1, 1000)})
