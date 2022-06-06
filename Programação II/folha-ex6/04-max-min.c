#include <stdio.h>

#define MAX 1000

void max_min(int vec[], int size, int *pmax, int *pmin) {
    int max = vec[0], min = vec[0];

    for (int i = 0; i < size; i++) {
        if (vec[i] > max) {
            max = vec[i];
        } else if (vec[i] < min) {
            min = vec[i];
        }
    }

    *pmax = max;
    *pmin = min;

    return;
}

int arr_input(int vec[]) {
    int input = 0, index = 0;
    printf("\n\nEscreve números inteiros para adicionar a um array, escreve -1 para terminar. \n\n");
        while (1) {
            printf("Escreve um número: ");
            scanf("%d", &input);
            if (input == -1) break;

            vec[index++] = input;
        }
    
    return index;
}

int main() {
    int vec[MAX];
    int max, min;

    printf("\n\nEscreve números inteiros e vê o seu máximo e mínimo!");

    int size = arr_input(vec);
    max_min(vec, size, &max, &min);

    printf("\nO máximo é %d \nO mínimo é %d\n\n", max, min);

    return 0;
}