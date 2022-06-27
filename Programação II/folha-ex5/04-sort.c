#include <stdio.h>

#define MAX 1000


int arr_input(int vec[]) {
    int input = 0, index = 0;
    printf("Escreve números inteiros para adicionar a um array, escreve -1 para terminar. \n\n");
        while (1) {
            printf("Escreve um número: ");
            scanf("%d", &input);
            if (input == -1) break;

            vec[index++] = input;
        }
    
    return index;
}

// Algoritmo de sort, que vai passando pelo array e ordena-o um par de cada vez
// Vê cada par do array e troca a ordem do par se este estiver na ordem errada

/*
// Versão com índices
void sort(int vec[], int size) {
    int desordenado = 1, temp;
    while (desordenado) {
        desordenado = 0;
        for (int i = 0; i < size; i++) {
            if (vec[i] > vec[i+1]) {
                desordenado = 1;
                temp = vec[i];
                vec[i] = vec[i + 1];
                vec[i + 1] = temp;
            }
        }
    }
}
*/

// Versão com pointers
void sort(int *vec, int size) {
    int desordenado;
    while (desordenado) {
        desordenado = 0;
        for (int *p = vec; p - vec < size - 1; p++) {
            if (*p > *(p+1)) {
                int temp = *p;

                *p = *(p+1);
                *(p+1) = temp;
                
                desordenado = 1;
            }
        }
    }

    return;
}

int main() {
    int vec[MAX];
    int size;

    size = arr_input(vec);

    sort(vec, size);
    printf("\nO array ordenado é: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", vec[i]);
    }

    printf("\n");
    return 0;
}

