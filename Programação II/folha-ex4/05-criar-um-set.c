#include <stdio.h>
#include <stdlib.h>

void printarray(int vec[], unsigned size);
int ocorre(int vec[], unsigned size, int value);

int main() {
    unsigned size;

    printf("\nVamos fazer um set em C a partir de um array! \n");

    printf("\nNúmero de valores que vais escrever: ");
    scanf("%u", &size);

    int* vec = malloc(size * sizeof(int));

    int elem;
    for (int i = 0; i < size; i++) {
        printf("Escreve um número inteiro positivo para adicionar ao array: ");
        scanf("%d", &elem);

        if (!ocorre(vec, size, elem)) {
            vec[i] = elem;
        } else {
            vec[i] = -1;
        }
    }

    printarray(vec, size);

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


int ocorre(int vec[], unsigned size, int value) {
    for (int i = 0; i < size; i++) {
        if (vec[i] == value) return 1;
    }

    return 0;
}