# Carregar o Ficheiro
with open('001-Periodic-Table.txt') as tabela:
    elementos_raw = eval(tabela.read())


# Organizar os Elementos
def organizar_elementos(elementos_todos: list):
    elementos_organizados = dict()
    for item in elementos_todos:
        if '(' in item['atomicMass']:
            end_of_certainty = item['atomicMass'].index('(')
            elementos_organizados[item['symbol']] = round(float(item['atomicMass'][:end_of_certainty]), 2)
    return elementos_organizados


# Para uma dada molécula ou átomo, devolve a sua massa molar
def massa_molar(composto: str):
    global elementos_raw
    numbers = set('0123456789')

    # Tornar os elementos legíveis pelo Python
    elementos = organizar_elementos(elementos_raw)

    # Conjunto de todos os átomos
    atomos_todos = []
    atomo = ['', '']
    for char in composto:
        # Se o character for um número, guardar junto ao respetivo elemento
        if char in numbers:
            atomo[1] += char

        # Caso contrário...
        else:
            # ... se não tiver nenhuma letra, então a letra é a primeira letra do elemento
            if len(atomo[0]) == 0:
                atomo[0] += char

            # ... se já tiver letra e a próxima letra for minúscula, então veio a segunda letra deste elemento
            elif char.islower():
                atomo[0] += char

            # ... se já letra e a próxima letra for maiúscula, então é um novo elemento
            else:
                # Guardar o átomo
                if len(atomo[1]) == 0:
                    atomo[1] += '1'
                atomos_todos += [atomo]
                atomo = [f'{char}', '']

    if len(atomo[1]) == 0:
        atomo[1] += '1'
    atomos_todos += [atomo]

    massa = 0
    for atomo in atomos_todos:
        massa += elementos[atomo[0]] * int(atomo[1])

    return massa


# Ver a Massa Molar de um Composto
print("Escreva 0 para parar o programa!")
while True:
    composto = input("\n\nEscreva o composto cuja massa molar quer ver: ")
    if composto == '0':
        break
    try:
        m = massa_molar(composto)
    except KeyError:
        print("Composto inválido!")
        m = "ERRO"
    print(f"\nA massa molar do {composto} é {m:.2f} g/mol")
