#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

void capitalizar(char str[]);

int main() {
    char text[MAX];

    printf("\nVamos passar uma cadeia de caracteres para maiúsculas! \n");

    printf("\nEscreva o texto: \n");
    fgets(text, MAX, stdin);

    capitalizar(text);
    printf("\nCapitalizado, o texto fica: \n");
    puts(text);

    return 0;
}

void capitalizar(char str[]) {
    char item = str[0];
    
    int index = 0;
    while (item != '\0') {
        str[index++] = toupper(item);
        item = str[index];
    }
}