#include <stdio.h>
#include <stdlib.h>

int main() {
    int* letras[26] = {0};

    int input = 0;
    while (1) {
        input = getchar();
        if (input == '\n') {
            break;
        }

        input = toupper(input);
        
        // Somar a letra à respetiva posição do array

        // Não funciona se eu usar incremento!!! Porquê?
        letras[input - 'A'] = (int) letras[input - 'A'] + 1;
    }

    for (int i = 0; i < 26; i++) {
        printf("'%c': %d \n", i + 'A', letras[i]);
    }

    return 0;
}