#include <stdio.h>

#define MAX 1000

/*
// Versão con índices
int ordenada(int vec[], int size) {
    for (int i = 0; i < size - 1; i++) {
        if (vec[i] > vec[i + 1]) return 0;
    }

    return 1;
}
*/

// Versão com pointers
int ordenada(int *vec, int size) {
    for (int *p = vec; p - vec < size-1; p++) {
        if (*p > *(p + 1))   return 0;
    }

    return 1;
}

int main() {
    int vec[MAX];
    int input = 0, index = 0;

    printf("\nEscreve números inteiros para adicionar a um array, escreve -1 para terminar. \n\n");
    while (1) {
        printf("Escreve um número: ");
        scanf("%d", &input);
        if (input == -1) break;

        vec[index++] = input;
    }

    if (ordenada(vec, index)) {
        printf("A lista está ordenada por ordem crescente!\n");
    } else {
        printf("A lista não está por ordem crescente! :(\n");
    }
}