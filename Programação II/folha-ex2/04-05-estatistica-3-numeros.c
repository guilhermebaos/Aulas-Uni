#include <stdio.h>

int main(void) {
    int num1, num2, num3;
    int max, min, amp, med;

    printf("Escreva o 1º valor: ");
    scanf("%d", &num1);
    printf("Escreva o 2º valor: ");
    scanf("%d", &num2);
    printf("Escreva o 3º valor: ");
    scanf("%d", &num3);

    if (num1 >= num2 && num1 >= num3) {
        max = num1;
    } else if (num2 >= num3) {
        max = num2;
    } else {
        max = num3;
    }

    if (num1 <= num2 && num1 <= num3) {
        min = num1;
    } else if (num2 <= num3) {
        min = num2;
    } else {
        min = num3;
    }

    amp = max - min;
    med = num1 + num2 + num3 - max - min;

    printf("\n\nO valor máximo é %d", max);
    printf("\nO valor mínimo é %d", min);
    printf("\nA mediana é %d", med);
    printf("\nA amplitude é %d\n\n", amp);
}