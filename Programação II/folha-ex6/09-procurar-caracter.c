#include <stdio.h>
#include <string.h>

#define MAX 1000

char *procurar(char *str, char ch) {
    for (char *p = str; *p > 0; p++) {
        // Encontramos o caracter
        if (*p == ch) {
            return p;
        }
    }

    // Não encontramos o caracter
    return NULL;
}


int main() {
    char str[MAX];
    char ch;

    printf("\n\nEscreva uma string para depois procurar se lá existe um caracter! \n");
    fgets(str, MAX, stdin);
    
    printf("\nEscreva um caracter para procurar na string: ");
    scanf("%c",&ch);

    char *res = procurar(str, ch);

    printf("\n\n");
    if (res != NULL) {
        printf("O caracter foi encontrado e está no endereço %p", res);
    } else {
        printf("O caracter não foi encontrado!");
    }
    printf("\n\n");

    return 0;
}