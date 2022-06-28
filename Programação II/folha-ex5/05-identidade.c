#include <stdio.h>

#define N 4

/*
// Versão com índices
int identidade(int mat[N][N]) {
    int diagonal = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            diagonal = i == j;

            if (mat[i][j] != diagonal) return 0;
        }
    }

    return 1;
}
*/

// Versão com pointers (uso indíces para variar o pointer)
int identidade(int mat[N][N]) {
    int diagonal = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            diagonal = i == j;
            
            if (*(*(mat + i) + j) != diagonal) return 0;
        }
    }

    return 1;
}


int main() {
    int matriz[N][N] = {1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1};

    printf("\n");
    if (identidade(matriz)) {
        printf("A matriz é a matriz identidade!");
    } else {
        printf("A matriz não é a matriz identidade :(");
    }
    printf("\n");

    return 0;
}