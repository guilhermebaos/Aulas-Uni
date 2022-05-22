#include <stdio.h>

#define N 4

int identidade(int mat[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) {
                if (mat[i][j] != 1) return 0;
            } else {
                if (mat[i][j] != 0) return 0;
            }
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