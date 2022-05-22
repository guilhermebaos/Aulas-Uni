#include <stdio.h>

double serie_log(double, int);

int main() {
    double x;
    int n;

    printf("Escreva um número para ver o seu logarítmo natural: ");
    scanf("%lf", &x);

    printf("Qual deve ser a maior potência a utilizar na aproximação: ");
    scanf("%d", &n);

    printf("\nO resultado de log(%.4lf) é aproximadamente %.4lf\n", x, serie_log(x, n));

    return 0;
}


double serie_log(double x, int n) {
    double resultado = 0;
    double y = x - 1;
    double y_pot = y;

    // Calcular o valor de log(x) = log(y + 1)
    int sinal = 1;
    
    for (int i = 1; i <= n; i++) {
        resultado += sinal * y_pot / i;

        sinal = -sinal;
        y_pot *= y;
    }

    return resultado;
}