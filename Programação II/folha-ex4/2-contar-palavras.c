#include <stdio.h>

int main() {
    int palavras = 0;

    int input = 0;
    int input_anterior;
    while (input != -1) {
        input_anterior = input;
        input = getchar();
        
        // Ver se o caracter é uma letra
        if ((input_anterior != '\t' && input_anterior != '\n' && input_anterior != ' ')
            &&
            (input == '\t' || input == '\n' || input == ' ')
            ) {
            palavras++;
        }
    }

    printf("A frase contém %d palavras!\n\n", palavras);

    return 0;
}