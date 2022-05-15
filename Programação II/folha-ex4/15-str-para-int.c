#include <stdio.h>
#include <string.h>

#define MAX 1000

int strtoint(char str[]);
int mypow10(int n);

int main() {
    char text[MAX];

    printf("\nVamos converter uma cadeia de caracteres só com dígitos para um inteiro! \n");

    printf("\nEscreva o texto: \n\n");
    fgets(text, MAX, stdin);
    
    int num = strtoint(text);

    printf("\nAqui está o número inteiro: %d\n\n", num);

    return 0;
}

// Return 10^n
int mypow10(int n) {
    if (n == 0) {
        return 1;
    }

    int total = 10;
    for (int i = 1; i < n; i++) {
        total *= 10;
    }

    return total;
}

int strtoint(char str[]) {
    int str_len = strlen(str) - 1;

    if (str_len == 0) {
        return 0;
    }
    
    int num = 0;
    for (int i = 0; i < str_len; i++) {
        num += mypow10(str_len - i - 1) * (str[i] - '0');
    }

    return num;
}