def pares_modk(x: int, k: int):
    x = str(x)
    if len(x) % 2 == 1:
        x = '0' + x

    nums = [x[2 * n: 2 * n + 2] for n in range(int(len(x) / 2))]
    nums = list(map(int, nums))

    for n in nums:
        if n % k != 0:
            return False
    return True


print(pares_modk(8125296, 4))
