#include <stdio.h>
#include <string.h>

#define MAX 1000

/*
// Versão com índices
void eliminar(char str[], char ch) {
    int len = strlen(str);
    int remover = 0;

    for (int i = 0; i < len; i++) {
        if (str[i] == ch) {
            remover = 1;
        }

        if (remover) {
            str[i] = str[i + 1];
        }
    }

    return;
}
*/

// Versão com pointers
void eliminar(char *str, char ch) {
    int remover = 0;
    for (char *p = str; ; p++) {
        // Sobreescrever o caracter atual com o seguinte
        if (remover) {
            *(p) = *(p+1);
        }

        // Tentar encontrar o caracter que queremos eliminar
        if (*p == '\0') {
            break;
        } else if (*p == ch && !remover) {
            remover = 1;
            *(p) = *(p+1);
        }
    }

    return;
}

int main() {
    char string[MAX];
    char remover;

    printf("\nEscreve uma string e escolhe um caracter para remover dessa string, caso exista!");

    printf("\n\nEscreve uma string: ");
    fgets(string, MAX, stdin);

    printf("\nEscreve um caracter para remover da string: ");
    scanf("%c", &remover);

    eliminar(string, remover);
    printf("\nNova string: %s\n\n", string);

    return 0;
}