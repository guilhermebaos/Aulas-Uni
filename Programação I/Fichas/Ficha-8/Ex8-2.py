def parse_nome(nome_completo: str):
    nome_lista = nome_completo.split(' ')
    if len(nome_lista) <= 2:
        return nome_lista
    for nome in nome_lista[:]:
        if nome in ['dos', 'das', 'do', 'da', 'de', 'e']:
            nome_lista.remove(nome)
    return nome_lista[0], nome_lista[1], nome_lista[-1]


print(parse_nome('Maria Miguel da Silva'))
print(parse_nome('Guilherme Botelho de Aguiar Oliveira Silva'))
a
