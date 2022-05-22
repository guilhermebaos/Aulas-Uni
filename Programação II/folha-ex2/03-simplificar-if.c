#include <stdio.h>

int main(void) {
    int idade, adolescente;
    printf("\nEscreve a tua idade: ");
    scanf("%d", &idade);
    if (idade >= 13 && idade <= 19) {
        adolescente = 1;
    } else {
        adolescente = 0;
    }

    if (adolescente) {
        printf("\nÉs adolescente!\n\n");
    }
}