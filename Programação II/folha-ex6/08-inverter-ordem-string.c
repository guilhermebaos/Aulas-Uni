#include <stdio.h>
#include <string.h>

#define MAX 1000

void inverter(char *str) {
    int size = strlen(str);

    // Meio da string
    char *mid = str + size / 2;
    for(char *p = str; p < mid; p++) {
        char temp = *p;

        // Elemento na posição p e na posição str + (size - 1) - (indíce de p) trocam
        *p = *(str + (size - 1) - (p - str));
        *(str + (size - 1) - (p - str)) = temp;
    }

    return;
}

int main() {
    char str[MAX];

    printf("\n\nEscreva uma string para a inverter! \n");
    fgets(str, MAX, stdin);

    inverter(str);
    printf("\n\nString Invertida: ");
    printf("\n%s\n\n", str);

    return 0;
}