def parte_texto(texto: str):
    letras, digitos, caracteres = '', '', ''
    for item in texto:
        item_ord = ord(item)
        if 65 <= item_ord <= 90 or 97 <= item_ord <= 122:
            letras += item
        elif 48 <= item_ord <= 57:
            digitos += item
        else:
            caracteres += item
    return [letras, digitos, caracteres]


assert parte_texto("Ano Letivo 2018/2019") == ['AnoLetivo', '20182019', '  /']
assert parte_texto("# 2018/2019 #") == ['', '20182019', '# / #']