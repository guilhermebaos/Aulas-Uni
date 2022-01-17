import json
import math

a = ["valor de pi", math.pi]
b = ["valor de e", math.e]
c = {"pi": math.pi, "e": math.e}


with open('json.txt', 'w') as file:
    json.dump((a, b, c), file)

print('Dump OK!')


with open('json.txt', 'r') as file:
    a, b, c = json.load(file)

print(a)
print(b)
print(c)

