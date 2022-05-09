#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

int palindromo(char str[]);

int main() {
    char text[MAX];

    printf("\nVamos ver se uma cadeia de caracteres é um palíndromo! \n");

    printf("\nEscreva o texto: \n\n");
    fgets(text, MAX, stdin);
    
    if (palindromo(text)) {
        printf("O texto é um palíndromo!\n\n");
    } else {
        printf("O texto não é um palíndromo :(\n\n");
    }

    return 0;
}

int palindromo(char str[]) {
    int last_index = 0;
    for (int i = 0; ; i++) {
        if (str[i] <= 0 || str[i] == '\n') {
            last_index = i-1;
            break;
        }
    }


    for (int i = 0; i < last_index / 2 ; i++) {
        if (str[i] != str[last_index - i]) {
            return 0;
        }
    }
    return 1;
}