#include <stdio.h>

// Vamos usar o método Babilónico,
// que é um caso particular do método de Newton
int main() {
    float x, a;

    printf("\nEscreva um número e veja a sua raiz quadrada aproximada: ");
    scanf("%f", &a);

    x = a / 2;

    for (int i = 1; i <= 10; i++) {
        x = (1.0 / 2) * (x + (a / x));
        printf("A %dª aproximação é: %.4f\n", i, x);
    }
}