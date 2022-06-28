#include <stdio.h>

#define N 50


int soma_diagonal1(int a[N][N], int n) {
    int total = 0;

    for (int i = 0; i < n; i++) {
        total += a[i][i];
    }

    return total;
}


int soma_diagonal2(int a[N][N], int n) {
    int total = 0;

    for (int i = 0; i < n; i++) {
        total += a[i][n - 1 - i];
    }

    return total;
}

int soma_coluna(int a[N][N], int n, int col) {
    int total = 0;

    for (int i = 0; i < n; i++) {
        total += a[i][col];
    }

    return total;
}

int soma_linha(int a[N][N], int n, int lin) {
    int total = 0;

    for (int i = 0; i < n; i++) {
        total += a[lin][i];
    }

    return total;
}

int magico(int a[N][N], int n) {
    int soma = soma_diagonal1(a, n);

    if (soma != soma_diagonal2(a, n)) {
        return 0;
    }

    for (int i = 0; i < n; i++) {
        if ((soma != soma_coluna(a, n, i)) || (soma != soma_linha(a, n, i))) return 0;
    }

    return 1;
}

void gerar_quadrado_magico(int a[N][N], int n) {
    // Coordenadas do número,
    // o eixo xx é da esquerda para a direita
    // o eixo yy é de cima para baixo
    int x = n / 2;
    int y = 0;

    int new_x, new_y;
    for (int num = 1; num <= n * n; num++) {
        a[y][x] = num;

        // Anda na diagonal e dá a volta ao quadrado
        new_x = (x + 1) % n;
        new_y = (y - 1 + n) % n;

        // Anda mesmo na diagonal
        if (a[new_y][new_x] == 0) {
            x = new_x;
            y = new_y;
        }

        // O espaço na diagonal está preenchido, anda para baixo em vez de na diagonal
        else {
            y = (y + 1) % n;
        }
    }
}

/*
// Aceder a uma matriz com índices
void print_matriz(int a[N][N], int n) {
    printf("\n\n{");
    for (int i = 0; i < n; i++) {
        printf("\n");
        for (int j = 0; j < n; j++) {
            printf("%3d ", a[i][j]);
        }
    }
    printf("\n}\n\n");
}
*/

// Aceder a uma matriz com pointers
void print_matriz(int a[N][N], int n) {
    printf("\n\n{");
    for (int i = 0; i < n; i++) {
        printf("\n");
        for (int j = 0; j < n; j++) {
            // Desta forma estamos a usar a matriz a como int**
            printf("%3d ", *(*(a + i) + j));

            // Desta forma estamos a usar a matriz a como int*
            // printf("%3d ", *(((int*) a + i*N)+j));
        }
    }
    printf("\n}\n\n");
}

int main() {
    int matriz[N][N] = {0};

    // n tem de ser um número ímpar!
    int n;
    
    printf("\n\nEscreva um número ímapar menor que %d e gere um quadrado mágico dessa dimensão: ", N);
    scanf("%d", &n);

    gerar_quadrado_magico(matriz, n);
    print_matriz(matriz, n);
    
    if (magico(matriz, n)) {
        printf("\n\nO quadrado é mesmo mágico!\n");
    } else {
        printf("\n\nO quadrado não é mágico :( \n");
    }
}