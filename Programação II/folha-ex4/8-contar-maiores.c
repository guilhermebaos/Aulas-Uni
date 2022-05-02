#include <stdio.h>
#include <stdlib.h>

int contar_maiores(int vec[], unsigned size, int value);

int main() {
    unsigned size;
    int value = 1;

    printf("\nVamos fazer um array e ver quantos elementos do array são maiores que X! \n");

    printf("\nTamanho do array: ");
    scanf("%u", &size);

    int* vec = malloc(size * sizeof(int));

    int elem;
    for (int i = 0; i < size; i++) {
        printf("Escreve um número para adicionar ao array: ");
        scanf("%d", &elem);
        vec[i] = elem;
    }

    printf("\nEscolhe o valor de X: ");
    scanf("%d", &value);
    
    printf("\n\nHá %d valores maiores que %d\n\n", contar_maiores(vec, size, value), value);

    return 0;
}


int contar_maiores(int vec[], unsigned size, int value) {
    int maiores = 0;
    for (int i = 0; i < size; i++) {
        if (vec[i] > value) maiores++;
    }

    return maiores;
}