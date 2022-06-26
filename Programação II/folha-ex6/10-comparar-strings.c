#include <stdio.h>
#include <string.h>

#define MAX 1000

int comparar(char *str1, char *str2) {
    for (char *p1 = str1; ; p1++) {
        if (*p1 != *(str2 + (p1 - str1))) {
            return 0;
        }

        if (*p1 == '\0') {
            break;
        }
    }

    return 1;
}


int main() {
    char str1[MAX], str2[MAX];

    printf("\n\nEscreva duas strings para ver se são iguais! \n");

    printf("\nPrimeira string: ");
    fgets(str1, MAX, stdin);

    printf("\nSegunda string: ");
    fgets(str2, MAX, stdin);

    int res = comparar(str1, str2);
    printf("\n\n");
    if (res == 1) {
        printf("As strings são iguais!");
    } else {
        printf("As strings NÃO são iguais!");
    }
    printf("\n\n");

    return 0;
}

/*
Versão normal:

int comparar(char *str1, char *str2) {
    int len1 = strlen(str1), len2 = strlen(str2);
    if (len1 != len2) {
        return 0;
    }

    for (int i = 0; i < len1; i++) {
        if (*(str1 + i) != *(str2 + i)) {
            return 0;
        }
    }

    return 1;
}
*/