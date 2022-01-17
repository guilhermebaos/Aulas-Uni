def remove_cpp_com(txt):
    len_txt = len(txt)

    if len_txt == 0:
        return txt

    inside_string = False
    for index, letter in enumerate(txt):
        # Se estamos dentro de uma string saimos dela, se não estamos passamos a estar
        if letter == '"':
            inside_string ^= True       # Isto alterna o valor de verdade da variável
        if not inside_string:
            if index <= len_txt - 2:
                if letter + txt[index + 1] == '//':
                    return txt[:index]
    return txt


assert remove_cpp_com("int main(void) {} // main function") == 'int main(void) {} '
assert remove_cpp_com("") == ''
assert remove_cpp_com("// main function") == ''
assert remove_cpp_com('''JHD#J//''') == 'JHD#J'
