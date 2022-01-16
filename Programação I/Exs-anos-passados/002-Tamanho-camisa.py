def tamanho_camisa(peso: int, altura: int):
    peso_index = 0 if peso < 65 else 1 if peso < 75 else 2 if peso < 85 else 3
    altura_index = 0 if altura < 165 else 1 if altura < 175 else 2 if altura < 180 else 3 if altura < 185 else 4

    tabela = [
        ['S', 'S', 'M', 'L', 'XL'],
        ['M', 'M', 'M', 'L', 'XL'],
        ['L', 'L', 'L', 'L', 'XL'],
        ['XL', 'XL', 'XL', 'XL', 'XL']
    ]
    return tabela[peso_index][altura_index]


print(tamanho_camisa(65, 175))
print(tamanho_camisa(75, 175))
