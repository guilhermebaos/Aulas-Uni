#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

int palindromo(char str[]);
int mystrlen(char str[]);

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

// Returns the last valid index for a string, defining the end of the string as '\n', '\0' or EOF
int mystrlen(char str[]) {
    int str_len = 0;
    for (int i = 0; ; i++) {
        if (str[i] <= 0 || str[i] == '\n') {
            str_len = i;
            break;
        }
    }

    return str_len;
}

int palindromo(char str[]) {
    int str_len = mystrlen(str);

    if (str_len == 0) {
        return 0;
    }

    for (int i = 0; i < str_len / 2 ; i++) {
        if (str[i] != str[str_len - i]) {
            return 0;
        }
    }
    return 1;
}