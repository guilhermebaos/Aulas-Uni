#include <stdio.h>

#define N 4

int soma_diagonal1(int matriz[N][N]) {
    int total = 0;

    for (int i = 0; i < N; i++) {
        total += matriz[i][i];
    }

    return total;
}


int soma_diagonal2(int matriz[N][N]) {
    int total = 0;

    for (int i = 0; i < N; i++) {
        total += matriz[i][N - 1 - i];
    }

    return total;
}

int main() {
    int matriz[N][N] = {1, 0, 0, 4, 0, 1, 3, 0, 0, 3, 1, 0, 0, 0, 0, 1};

    int diagonal1 = soma_diagonal1(matriz);
    int diagonal2 = soma_diagonal2(matriz);

    printf("\n\nA soma da diagonal principal é %d", diagonal1);
    printf("\nA soma da diagonal secundária é %d\n\n", diagonal2);

    return 0;
}