#include <stdio.h>
#include <string.h>

#define MAX 1000

/*
// Solução com dois contadores e com indíces
int anagramas(char str1[MAX], char str2[MAX]) {
    int contador1[128] = {0};
    int contador2[128] = {0};

    int len;
    int len1 = strlen(str1);
    int len2 = strlen(str2);

    // Ver se os comprimentos são iguais
    if (len1 != len2) {
        return 0;
    } else {
        len = len1;
    }

    // Criar os contadores associados a cada palavra
    for (int i = 0; i < len; i++) {
        contador1[(int) str1[i]]++;
        contador2[(int) str2[i]]++;
    }

    // Ver se os contadores são iguais
    for (int i = 0; i < 128; i++) {
        if (contador1[i] != contador2[i]) return 0;
    }
    return 1;
}
*/

// Solução com um contador e com pointers
int anagramas(char *str1, char *str2) {
    int contador[128] = {0};

    for (char *p1 = str1; ; p1++) {
        if (*p1 == '\0') break;

        contador[(int) *p1]++;
    }

    for (char *p2 = str2; ; p2++) {
        if (*p2 == '\0') break;

        contador[(int) *p2]--;
    }

    for (int *pc = contador; pc - contador < 128; pc++) {
        if (*pc != 0) return 0;
    }

    return 1;
}

int main() {
    char str1[MAX];
    char str2[MAX];

    printf("\n\nEscreve duas strings com caracteres ASCII e vê se são anagramas!\n");

    printf("\nPrimeira string: ");
    fgets(str1, MAX, stdin);

    printf("\nSegunda string: ");
    fgets(str2, MAX, stdin);

    if (anagramas(str1, str2)) {
        printf("\n\nAs strings são anagramas uma da outra!\n");
    } else {
        printf("\n\nAs strings não são anagramas uma da outra :(\n");
    }

    return 0;
}