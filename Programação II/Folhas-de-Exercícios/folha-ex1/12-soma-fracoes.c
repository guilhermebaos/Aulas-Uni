#include <stdio.h>

int main() {
    int num1, den1, num2, den2;
    int num_res, den_res;

    printf("\nSoma de duas frações!");

    printf("\n\nPrimeiro numerador: ");
    scanf("%d", &num1);
    
    printf("Primeiro denominador: ");
    scanf("%d", &den1);

    printf("\nSegundo numerador: ");
    scanf("%d", &num2);

    printf("Segundo denominador: ");
    scanf("%d", &den2);

    num_res = num1 * den2 + num2 * den1;
    den_res = den1 * den2;
    printf("\n\nResultado: %d/%d + %d/%d = %d/%d", num1, den1, num2, den2, num_res, den_res);

    printf("\n\n");
    return 0;
}