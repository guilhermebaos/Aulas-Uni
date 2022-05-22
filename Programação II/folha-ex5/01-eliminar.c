#include <stdio.h>
#include <string.h>

#define MAX 1000

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

int main() {
    char string[MAX];
    char remover;

    printf("Escreve uma string e escolhe um caracter para remover dessa string, caso exista!\n\n");

    printf("\nEscreve uma string: ");
    fgets(string, MAX, stdin);

    printf("\nEscreve um caracter para remover da string: ");
    scanf("%c", &remover);

    eliminar(string, remover);
    printf("\n%s", string);

    return 0;
}