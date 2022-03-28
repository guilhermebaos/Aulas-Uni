#include <stdio.h>

int main() {
    int n, fac;

    printf("Escreva um número inteiro e veja os seus fatores primos: ");
    scanf("%d", &n);

    fac = 2;
    printf("\nFatores primos de %d: ", n);
    while (n > 1) {
        if (n % fac == 0) {
            n /= fac;
            printf("%d ", fac);
        } else {
            fac += 1;
        }
    }
    printf("\n");
}