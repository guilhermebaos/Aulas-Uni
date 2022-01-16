def forte(passwd):
    if len(passwd) < 8:
        return False
    minuc, maiusc, alg = False, False, False
    for item in passwd:
        item_ord = ord(item)
        if 65 <= item_ord <= 90:
            minuc = True
        elif 97 <= item_ord <= 122:
            maiusc = True
        elif 48 <= 57:
            alg = True
    return minuc and maiusc and alg


assert not forte('9EwL56')
assert not forte('HXKW1393')
assert forte('ffu4G7Fghjk')



