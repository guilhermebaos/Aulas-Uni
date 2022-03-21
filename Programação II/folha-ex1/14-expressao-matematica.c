#include <stdio.h>

int main(void) {
    float x;
    printf("\nEscreva um número real: ");
    scanf("%f", &x);
    printf("\n%f\n\n", 3 * x * x * x * x * x + 2 * x * x * x * x - 5 * x * x * x - x * x + 7 * x - 6);
    return 0;
}