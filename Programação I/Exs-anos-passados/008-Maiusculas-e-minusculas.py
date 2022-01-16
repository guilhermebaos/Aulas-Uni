def maiusc_minusc(string: str):
    points = sum(1 if 65 <= ord(x) <= 90 else -1 if 97 <= ord(x) <= 122 else 0 for x in string)
    return 1 if points > 0 else -1 if points < 0 else 0


assert maiusc_minusc("Ano 2019") == -1
assert maiusc_minusc("ANO Novo!!!") == 1
assert maiusc_minusc("NOvo!!!") == 0
