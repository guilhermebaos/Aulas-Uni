#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

int strongpass(char str[]);
int mystrlen(char str[]);

int main() {
    char text[MAX];

    printf("\nVamos ver se uma cadeia de caracteres é uma palavra passe forte! \n");

    printf("\nEscreva o texto: \n\n");
    fgets(text, MAX, stdin);
    
    if (strongpass(text)) {
        printf("O texto é uma palavra passe forte!\n\n");
    } else {
        printf("O texto não é uma palavra passe forte :(\n\n");
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

int strongpass(char str[]) {
    int str_len = mystrlen(str);

    if (str_len < 6) {
        return 0;
    }

    int maiuscula = 0, minuscula = 0, digito = 0;
    for (int i = 0; i < str_len; i++) {
        if ('a' <= str[i] && str[i] <= 'z') {
            minuscula = 1;
        } else if ('A' <= str[i] && str[i] <= 'Z') {
            maiuscula = 1;
        } else if ('0' <= str[i] <= '9') {
            digito = 1;
        }
    }
    return minuscula && maiuscula && digito;
}