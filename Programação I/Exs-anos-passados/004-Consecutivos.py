def consecutivos(lista: list):
    for index, item in enumerate(lista):
        if lista[index - 1] + 1 == item:
            return True
    return False


print(consecutivos([2,-10,1]))
print(consecutivos([-10,2,1]))
print(consecutivos([-10,1,2]))
