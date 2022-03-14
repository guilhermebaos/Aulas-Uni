#include <stdio.h>

int main() {
    float l, w, h, r;

    printf("Vamos calcular o volume de um Paralelepípedo!\n\n");

    printf("Escreva o comprimento do Paralelepípedo: ");
    scanf("%f", &l);
    
    printf("Escreva a largura do Paralelepípedo: ");
    scanf("%f", &w);
    
    printf("Escreva a altura do Paralelepípedo: ");
    scanf("%f", &h);

    r = l * w * h;
    printf("\nO volume do Paralelepipedo é %.2f \n", r);
}