#include <stdio.h>
#include <stdlib.h>

void range(int vec[], unsigned size, int start, int step);

int main() {
    unsigned size;
    int start, step;

    // Inputs
    printf("\nVamos fazer um array com uma progressão aritmética! \n");

    printf("\nEscreva o tamanho do array: ");
    scanf("%u", &size);

    printf("\nEscreva o 1º valor: ");
    scanf("%d", &start);

    printf("\nEscreva o tamanho do incremento: ");
    scanf("%d", &step);


    // Criar o array
    int* vec = malloc(size * sizeof(int));

    range(vec, size, start, step);

    // Fazer print do array
    printf("\n\nO array tem os seguintes valores: { ");
    for (int i = 0; i < size; i++) {
        printf("%d ", vec[i]);
    }
    printf("}\n\n");

    return 0;
}


void range(int vec[], unsigned size, int start, int step) {
    for (int i = 0; i < size; i++) {
        vec[i] = start + i * step;
    }

    return;
}