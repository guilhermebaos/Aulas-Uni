#include <stdio.h>

int gcd(int, int);

int main(void) {
    int a, b, c, iter;

    printf("\nEscreva um número: ");
    scanf("%d", &a);

    printf("Escreva outro número: ");
    scanf("%d", &b);

    if (b > a) {
        c = a;
        a = b;
        b = c;
    }

    printf("\n");
    iter = gcd(a, b);
    printf("\n\nForam necessáiras %d iterações!\n\n", iter - 1);
}

int gcd(int a, int b) {
    if (b == 0) {
        printf("%d", a);
        return 1;
    } else {
        printf("gcd(%d, %d) = ", a, b);
        return 1 + gcd(b, a % b);
    }
}