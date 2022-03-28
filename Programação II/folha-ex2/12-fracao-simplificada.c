#include <stdio.h>

int gcd(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}

int main(void) {
    int num, den, div;

    printf("\nEscreva o numerador: ");
    scanf("%d", &num);

    printf("Escreva o denominador: ");
    scanf("%d", &den);

    div = gcd(num, den);
    printf("A função simplificada é: %d/%d\n\n", num / div, den / div);
}