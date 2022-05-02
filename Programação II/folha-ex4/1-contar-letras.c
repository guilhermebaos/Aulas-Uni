#include <stdio.h>

int main() {
    int letras = 0;

    int input = 0;
    while (input != '\n') {
        input = getchar();
        
        // Ver se o caracter é uma letra
        if (('A' <= input && input <= 'Z') || ('a' <= input && input <= 'z')) {
            letras++;
        }
    }

    printf("A frase contém %d letras!\n\n", letras);

    return 0;
}