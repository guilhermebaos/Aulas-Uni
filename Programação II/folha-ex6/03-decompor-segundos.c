#include <stdio.h>

void decompor(int total_seg, int *horas, int *mins, int *segs) {
    *horas = total_seg / 3600;
    total_seg -= *horas * 3600;

    *mins = total_seg / 60;
    total_seg -= *mins * 60;

    *segs = total_seg;
}

int main() {
    int total_segs;
    int horas, mins, segs;

    printf("\nQuantos segundos queres converter em horas e minutos? ");
    scanf("%d", &total_segs);

    decompor(total_segs, &horas, &mins, &segs);

    printf("\n\n%ds = %dh %dmin %ds\n", total_segs, horas, mins, segs);

    return 0;
}