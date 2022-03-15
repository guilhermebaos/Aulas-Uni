#include <stdio.h>

#define PI 3.14159

int main() {
    float raio, volume;

    printf("Escreva o raio da esfera e vê o seu volume: ");
    scanf("%f", &raio);
    volume = 1.0 * 4 / 3 * PI * raio*raio*raio;

    printf("\n\nA esfera tem volume %.2f \n", volume);
}