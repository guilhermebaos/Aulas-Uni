#include <stdio.h>

double aprox_pi(int);

int main() {
    int ordem = 10;

    printf("\nAlgumas aproximações de pi usando a fórmula de Gregory-Leibniz: \n");
    
    for (int i = 1; i <= 7; i++) {
        printf("\nA aproximação até ordem %d é %.8lf", ordem, aprox_pi(ordem));
        ordem *= 10;
    }
    printf("\n\n");

    return 0;
}


double aprox_pi(int n) {
    double pi = 0;
    int sinal = 1;

    for (int i = 0; i < n; i++) {
        pi += 4.0 * sinal / (2 * i + 1);
        sinal *= -1;
    }

    return pi;
}
