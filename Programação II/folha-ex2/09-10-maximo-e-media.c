#include <stdio.h>

int main(void) {
    float num, max, soma;
    int len_num = 1, ler = 1;

    printf("\nEscreva um número, escreva 0 para terminar: ");
    scanf("%f", &num);
    if (num == 0) {
        /* Ver se vamos ler valores ou se terminamos imediatamente */
        ler = 0;
    }

    max = num;
    soma = num;
    while (ler) {
        printf("Escreva um número, escreva 0 para terminar: ");
        scanf("%f", &num);

        /* Se o número for 0, terminar imediatamente */
        if (num == 0) {
            break;
        }

        /* Atualizar a soma e o número de valores que já lemos */
        soma += num;
        len_num++;
        if (num > max) {
            max = num;
        }
    }

    printf("\n\nA soma dos valores escritos é %.2f\n", soma);
    printf("A média dos valores escritos é %.2f\n", soma / len_num);
    printf("O maior valor escrito é %.2f\n\n", max);

    return 0;
}