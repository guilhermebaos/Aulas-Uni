import numpy as np

total = 0
for k in range(100_000):
    passo = (np.random.random() > 0.5) * 2 - 1
    total += passo
    if abs(passo) != 1:
        print("Erro:", passo)

print(total)