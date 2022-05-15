#include <stdio.h>
#include <string.h>

#define MAX 1000

int minicalc(char str[]);

int main() {
    char text[MAX];

    printf("\nVamos executar uma operação (+, -, *) entre dois dígitos! \n");

    printf("\nEscreva o texto: \n\n");
    fgets(text, MAX, stdin);
    
    int num = minicalc(text);

    printf("\nAqui está o resultado: %d\n\n", num);

    return 0;
}

int minicalc(char str[]) {
    int lop = str[0] - '0';
    int rop = str[2] - '0';

    int operador = str[1];

    if (operador == '+') {
        return lop + rop;
    } else if (operador == '-') {
        return lop - rop;
    } else if (operador == '*') {
        return lop * rop;
    }

    return -1;
}