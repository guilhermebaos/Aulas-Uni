#include <stdio.h>

int main(void) {
    float x;
    printf("\nEscreva um número real: ");
    scanf("%f", &x);
    printf("\n%f\n\n", ((((3 * x + 2) * x - 5) * x - 1) * x + 7) * x - 6);
    return 0;
}