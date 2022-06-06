#include <stdio.h>

#define MAX 1000

void store_zeros(int vec[]) {
    int n = MAX;
    for(int *p = vec; n > 0; n--) {
        *p = 0;
        p++;
    }

   return;
}

void print_arr(int vec[]) {
    printf("\n\nO array é: { ");
    for (int i = 0; i < MAX; i++ ) {
        printf("%d ", vec[i]);
    }
    printf("}\n\n");

    return;
}

int main() {
    int vec[MAX];

    store_zeros(vec);
    print_arr(vec);

    printf("\n\nOs zeros foram guardados com sucesso!\n\n");

    return 0;
}