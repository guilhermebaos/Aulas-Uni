#include <stdio.h>

#define MAX 1000

int desordem(int vec[], int size) {
    int pares = 0;
    for (int i = 0; i < size - 1; i++) {
        if (vec[i] > vec[i + 1]) pares++;
    }

    return pares;
}

int main() {
    int vec[MAX];
    int input = 0, index = 0;

    printf("Escreve números inteiros para adicionar a um array, escreve -1 para terminar. \n\n");
    while (1) {
        printf("Escreve um número: ");
        scanf("%d", &input);
        if (input == -1) break;

        vec[index++] = input;
    }

    int valor = desordem(vec, index);
    printf("\nO nível da desordem é %d\n!", valor);
}