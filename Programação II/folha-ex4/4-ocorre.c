#include <stdio.h>
#include <stdlib.h>

int ocorre(int vec[], unsigned size, int value);

int main() {
    unsigned size;
    int value = 1;

    printf("\nVamos fazer um array e verificar se um certo elemento está nele contido! \n");

    printf("\nTamanho do array: ");
    scanf("%u", &size);

    int* vec = malloc(size * sizeof(int));

    int elem;
    for (int i = 0; i < size; i++) {
        printf("Escreve um número para adicionar ao array: ");
        scanf("%d", &elem);
        vec[i] = elem;
    }

    while (value) {
        printf("\nQue valor queres procurar? Escreve 0 para terminar");
        scanf("%d", &value);

        if (ocorre(vec, size, value)) {
            printf("Valor encontrado!\n\n");
        } else {
            printf("Valor não encontrado!\n\n");
        }
    }

    return 0;
}


int ocorre(int vec[], unsigned size, int value) {
    for (int i = 0; i < size; i++) {
        if (vec[i] == value) return 1;
    }

    return 0;
}