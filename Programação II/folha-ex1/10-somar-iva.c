#include <stdio.h>

int main() {
    float valor;

    printf("Valor sem IVA? ");
    scanf("%f", &valor);

    valor *= 1.23;
    printf("Valor com IVA: %.2f \n", valor);
}