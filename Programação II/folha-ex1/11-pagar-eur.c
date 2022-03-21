#include <stdio.h>

int main() {
    int notas20, notas10, notas5, moedas1, valor;

    printf("Escreva o valor a pagar e descubra como pode pagar: ");
    scanf("%d", &valor);

    notas20 = valor / 20;
    valor -= 20 * notas20;

    notas10 = valor / 10;
    valor -= 10 * notas10;

    notas5 = valor / 5;
    valor -= 5 * notas5;

    moedas1 = valor;

    printf("\n Notas 20 EUR: %d \n Notas 10 EUR: %d \n Notas 5 EUR: %d \n Moedas 1 EUR: %d \n", notas20, notas10, notas5, moedas1);
}