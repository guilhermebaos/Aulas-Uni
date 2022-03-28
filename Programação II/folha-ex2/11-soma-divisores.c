#include <stdio.h>

int soma_divisores(int n) {
    int total = 0;

    for (int div = 1; div < (n / 2 + 1); div++) {
        if (n % div == 0) {
            total += div;
        }
    }
    return total;
}

int main(void) {
    int num;

    printf("\nEscreva um número para ver a soma dos seus divisores menores que ele próprio: ");
    scanf("%d", &num);

    printf("\nA soma é %d!\n\n", soma_divisores(num));

    return 0;
}