#include <stdio.h>
#include <stdlib.h>

int filtrar_positivos(int vec[], int size);
void printarray(int vec[], unsigned size);

int main() {
    unsigned size;

    printf("\nVamos fazer um array e colocar todos os seus valores positivos no início! \n");

    printf("\nTamanho do array: ");
    scanf("%u", &size);

    int* vec = malloc(size * sizeof(int));

    int elem;
    for (int i = 0; i < size; i++) {
        printf("Escreve um número para adicionar ao array: ");
        scanf("%d", &elem);
        vec[i] = elem;
    }

    int positivos = filtrar_positivos(vec, size);

    printf("O array filtrado é: ");
    printarray(vec, size);

    printf("E tem %d valores positivos!\n\n", positivos);

    return 0;
}

void printarray(int vec[], unsigned size) {
    printf("\n\nO array tem os seguintes valores: { ");
    for (int i = 0; i < size; i++) {
        if (vec[i] >= 0) printf("%d ", vec[i]);
    }
    printf("}\n\n");

    return;
}

int filtrar_positivos(int vec[], int size) {
    int index = 0;
    for (int i = 0; i < size; i++) {
        if (vec[i] > 0) {
            vec[index++] = vec[i];
        }
    }

    return index;
}