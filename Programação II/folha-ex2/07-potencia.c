#include <stdio.h>

/* Devolve o valor de x^n */
float power(float x, int n) {
    float total = 1;
    for (int i = 1; i <= n; i++) {
        total *= x;
    }

    return total;
}

int main(void) {
    float num, res;
    int exp;

    printf("\nEscreva a base da potência: ");
    scanf("%f", &num);

    printf("Escreve o expoente da potência: ");
    scanf("%d", &exp);

    res = power(num, exp);
    printf("\nO valor de %.2f^%d é %.2f\n\n", num, exp, res);

    return 0;
}