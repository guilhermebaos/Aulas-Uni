#include <stdio.h>

int maximum_of_three(int num1, int num2, int num3) {
    int max;
    if (num1 >= num2 && num1 >= num3) {
        max = num1;
    } else if (num2 >= num3) {
        max = num2;
    } else {
        max = num3;
    }

    return max;
}

int minimum_of_three(int num1, int num2, int num3) {
    int min;
    if (num1 <= num2 && num1 <= num3) {
        min = num1;
    } else if (num2 <= num3) {
        min = num2;
    } else {
        min = num3;
    }

    return min;
}

int median_of_three(int num1, int num2, int num3, int max, int min) {
    return num1 + num2 + num3 - max - min;
}

int main(void) {
    int num1, num2, num3;
    int max, min, amp, med;

    printf("\nEscreva o 1º valor: ");
    scanf("%d", &num1);
    printf("Escreva o 2º valor: ");
    scanf("%d", &num2);
    printf("Escreva o 3º valor: ");
    scanf("%d", &num3);

    max = maximum_of_three(num1, num2, num3);
    min = minimum_of_three(num1, num2, num3);
    med = median_of_three(num1, num2, num3);

    amp = max - min;

    printf("\n\nO valor máximo é %d", max);
    printf("\nO valor mínimo é %d", min);
    printf("\nA mediana é %d", med);
    printf("\nA amplitude é %d\n\n", amp);
}
