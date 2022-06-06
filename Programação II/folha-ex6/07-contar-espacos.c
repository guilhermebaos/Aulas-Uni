#include <stdio.h>

#define MAX 1000

int contar_espacos(char *str) {
    int total = 0;
    while (1) {
        if (*str <= 0) break;

        if (*str == ' ')  total++;

        str++;
    }

    return total;
}

int main() {
    char str[MAX];
    
    printf("\n\nEscreve texto e vê quantos espaços da forma ' ' tem!\n\n");
    fgets(str, MAX-1, stdin);

    int espacos = contar_espacos(str);
    printf("\n\nA string tem %d espaços\n\n", espacos);

    return 0;
}