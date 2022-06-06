#include <stdio.h>

void reduzir(int *pnum, int *pdenom) {
    int gcd, num, denom;

    num = *pnum; denom = *pdenom;
    while (1) {
        if (num == 0) {
            gcd = denom;
            break;
        } else if (denom == 0) {
            gcd = num;
            break;
        } else if (num > denom) {
            num -= num / denom * denom;
        } else {
            denom -= denom / num * num;
        }
    }

    *pnum /= gcd;
    *pdenom /= gcd;

    return;
}

int main() {
    int num, denom;

    printf("\nEscreve o numerador e o denominador e vê a sua fração reduzida!\n\n");

    printf("Numerador: ");
    scanf("%d", &num);
    printf("Denominador:");
    scanf("%d", &denom);

    reduzir(&num, &denom);
    printf("\nA fração reduzida é %d/%d!\n\n", num, denom);

    return 0;
}