#include <stdio.h>

/*
int main() {
    int num1, num2, num3, maior_num;

    printf("\nEscreve três números inteiros e vê qual deles é maior!");

    printf("\n\nPrimeiro número: ");
    scanf("%d", &num1);
    
    printf("Segundo número: ");
    scanf("%d", &num2);

    printf("Terceiro número: ");
    scanf("%d", &num3);

    if (num1 > num2 && num1 > num3) {
        maior_num = num1;
    } else if (num2 > num3) {
        maior_num = num2;
    } else {
        maior_num = num3;
    }

    printf("\nO maior número é %d\n\n", maior_num);
}
*/

// Código para o Codex
int main() {
    int a, b, c, res;

    scanf("%d %d %d", &a, &b, &c);
    if (a > b && a > c) {
        res = a;
    } else if (b > c) {
        res = b;
    } else {
        res = c;
    }

    printf("%d\n", res);
}
