import numpy as np

massas = np.array([100.1, 101.5, 100.4, 100.7, 101.2, 102.1])


media = np.mean(massas)
desvios = np.array([x - media for x in massas])
desvios_abs = np.array([abs(x) for x in desvios])


print(media)
print(np.mean(desvios))
print(np.mean(desvios_abs))
print(np.var(massas))
print(np.std(massas))
print(np.std(massas) / (len(massas) ** 0.5))
