#include <stdio.h>

int main() {
    int bilhetes;
    int num_amigos;
    
    // Ler os inteiros
    printf("\n\nInputs: \n");
    scanf("%d", &bilhetes);
    scanf("%d", &num_amigos);

    // Ler os bilhetes
    int bil_amigos[num_amigos];
    for (int i = 0; i < num_amigos; i++) {
        scanf("%d", &bil_amigos[i]);
    }
    
    // Inicializar os arrays de tamanho variável
    int bil_distribuidos[num_amigos];
    int bil_completos[num_amigos];
    for (int i = 0; i < num_amigos; i++) {
        bil_distribuidos[i] = 0;
        bil_completos[i] = 0;
    }
    
    // Distribuir os bilhetes
    int num_amigos_insatisf = num_amigos;

    // Enquanto houver amigos insatisfeitos e houver bilhetes para todos eles
    while (bilhetes > num_amigos_insatisf && num_amigos_insatisf > 0) {
        for (int i = 0; i < num_amigos; i++) {

            // Dar um bilhete a todos os insatisfeitos
            if (bil_distribuidos[i] < bil_amigos[i]) {
                bil_distribuidos[i]++;
                bilhetes--;
            }

            // Ver quantos amigos ficaram satisfeitos
            if (bil_distribuidos[i] == bil_amigos[i] && bil_completos[i] == 0) {
                bil_completos[i] = 1;
                num_amigos_insatisf--;
            }
        }
    
        printf("\nbilhetes = %d", bilhetes);
        printf("\namigos = %d\n", num_amigos_insatisf);
    }

    printf("\n\nOutputs: ");
    for (int i = 0; i < num_amigos; i++) {
        printf("\n%d", bil_distribuidos[i]);
    }

    printf("\n");
    return 0;
}