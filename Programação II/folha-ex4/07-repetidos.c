#include <stdio.h>
#include <stdlib.h>

int repetidos(int vec[], unsigned size);

int main() {
    unsigned size;

    printf("\nVamos fazer um array e verificar se há elemtnso repetidos nele! \n");

    printf("\nTamanho do array: ");
    scanf("%u", &size);

    int* vec = malloc(size * sizeof(int));

    int elem;
    for (int i = 0; i < size; i++) {
        printf("Escreve um número para adicionar ao array: ");
        scanf("%d", &elem);
        vec[i] = elem;
    }

    if (repetidos(vec, size)) {
        printf("\nHá valores repetidos!\n\n");
    } else {
        printf("\nNão há valores repetidos!\n\n");
    }

    return 0;
}


int repetidos(int vec[], unsigned size) {
    // Para cada elemento na posição i ...
    for (int i = 0; i < size; i++) {

        // ... verifica se há um elemento que vez de pois dele que é igual
        for (int j = i + 1; j < size; j++) {
            if (vec[j] == vec[i]) {
                return 1;
            }
        }
    }

    return 0;
}