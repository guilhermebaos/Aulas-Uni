#include <stdio.h>

#include <stdio.h>

int soma_diagonal1(int a[50][50], int n) {
    int total = 0;

    for (int i = 0; i < n; i++) {
        total += a[i][i];
    }

    return total;
}


int soma_diagonal2(int a[50][50], int n) {
    int total = 0;

    for (int i = 0; i < n; i++) {
        total += a[i][n - i - 1];
    }

    return total;
}

int soma_coluna(int a[50][50], int n, int col) {
    int total = 0;

    for (int i = 0; i < n; i++) {
        total += a[i][col];
    }

    return total;
}

int soma_linha(int a[50][50], int n, int lin) {
    int total = 0;

    for (int i = 0; i < n; i++) {
        total += a[lin][i];
    }

    return total;
}

int magico(int a[50][50], int n) {
    int soma = soma_diagonal1(a, n);

    if (soma != soma_diagonal2(a, n)) {
        return 0;
    }

    for (int i = 0; i < n; i++) {
        if (soma != soma_coluna(a, n, i)) {
            return 0;
        } if (soma != soma_linha(a, n, i)) {
            return 0;
        }
    }

    return 1;
}

void gerar_quadrado_magico(int a[50][50], int n) {
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

        // O espaço na diagonal está preenchido, anda para baixo em vez de na diagonal
        } else {
            y = (y + 1) % n;
        }
    }
}

void print_matriz(int a[50][50], int n) {
    printf("\n{");
    for (int i = 0; i < n; i++) {
        printf("\n");
        for (int j = 0; j < n; j++) {
            printf("%d ", a[i][j]);
        }
    }
    printf("}\n");
}

int main() {
    int matriz[50][50] = {0};

    // n tem de ser um número ímpar!
    int n;
    
    printf("\n\nEscreva um número e gere um quadrado mágico dessa dimensão: ");
    scanf("%d", &n);

    gerar_quadrado_magico(matriz, n);
    print_matriz(matriz, n);
    
    if (magico(matriz, n)) {
        printf("\n\nO quadrado é mesmo mágico!\n");
    } else {
        printf("\n\nO quadrado não é mágico :( \n");
    }
}