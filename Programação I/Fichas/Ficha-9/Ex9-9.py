import json

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


iteracoes = {1: 0}

with open('iteracoes.txt', 'w') as file:
    json.dump(iteracoes, file)


while True:
    n = int(input('Quantos Números quer verificar? '))

    if n == 0:
        break

    with open('iteracoes.txt', 'r') as file:
        iteracoes = json.load(file)

    ultima_it = max(list(map(int, iteracoes.keys())))
    for num in range(ultima_it + 1, n + ultima_it + 1):
        iteracoes[num] = it_collatz(num)

    with open('iteracoes.txt', 'w') as file:
        json.dump(iteracoes, file)


print(iteracoes)
