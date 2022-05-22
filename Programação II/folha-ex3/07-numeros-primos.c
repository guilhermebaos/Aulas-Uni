#include <stdio.h>
#include <stdlib.h>

int main() {
    int limite;

    printf("\nDiga um número e veja os números primos até esse número: ");
    scanf("%d", &limite);
    
    int* primos = malloc((limite / 2 + 1) * sizeof(int));
    int teste_primo;
    int index_primo = 0;

    primos[0] = 2;
    printf("\nOs números primos até %d são: ", limite);
    for (int num = 2; num <= limite; num++) {
        teste_primo = 1;

        // Tentar dividir o número pelos números primos menores que ele
        for (int index = 0; index <= index_primo; index++) {
            if (num % primos[index] == 0) {
                teste_primo = 0;
                break;
            }
        }

        // Se o número não for divisível por nenhum número primo, então ele é primo
        if (teste_primo) {
            index_primo += 1;
            primos[index_primo] = num;
            printf("%d ", num);
        }
    }
    printf("\n");

    return 0;
}
