#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
    int n;

    printf("Escreva um número e veja como se escreve em binário: ");
    scanf("%d", &n);

    int size = (int) log2(n) + 1;
    int* binary = malloc(size * sizeof(int));

    int i = size - 1;
    while (n > 0) {
        binary[i] = n % 2;
        n /= 2;
        i -= 1;
    }

    printf("\nO número %d em binário é: ", n);
    for (int digit = 0; digit < size; digit++) {
        printf("%d", binary[digit]);
    }
    printf("\n");

    return 0;
}