import pickle
import math

a = ["valor de pi", math.pi]
b = ["valor de e", math.e]
c = {"pi": math.pi, "e": math.e}

with open('foo.pickle', 'wb') as file:
    pickle.dump((a, b, c), file)

print('Dump OK!')


with open('foo.pickle', 'rb') as file:
    a, b, c = pickle.load(file)

print(a)
print(b)
print(c)
