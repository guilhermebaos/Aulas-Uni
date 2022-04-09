#include <stdio.h>

int bissexto(int);
int prox_bissexto(int);

int main(void) {
    int ano;

    while (1) {
        printf("\nEscreva um ano e veja quando é o próximo ano bissexto: ");
        scanf("%d", &ano);
        if (ano == 0) {
            break;
        }

        // Se o ano for bissexto, devolve o próprio ano
        if (bissexto(ano)) {
            printf("O ano %d já é bissexto!\n", ano);

        // Se o ano não for bissexto, devolve o próximo ano bissexto
        } else {
            ano = prox_bissexto(ano);
            printf("O próximo ano bissexto é %d!\n", ano);
        }
    }

    return 0;
}

int bissexto(int n) {
    if (n % 400 == 0) {
        return 1;
    } else if (n % 100 == 0) {
        return 0;
    } else if (n % 4 == 0) {
        return 1;
    } else {
        return 0;
    }
}

int prox_bissexto(int n) {
    while (!bissexto(n)) {
        n += 1;
    }
    return n;
};