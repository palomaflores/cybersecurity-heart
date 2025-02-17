#include <stdio.h>
#include <string.h>

void printHeart(char *str) {
    int n = strlen(str);
    int i, j;

    for (i = n / 2; i <= n; i += 2) {
        for (j = 1; j < n - i; j += 2)
            printf(" ");
        for (j = 1; j <= i; j++)
            printf("%c", str[j % n]);
        for (j = 1; j <= n - i; j++)
            printf(" ");
        for (j = 1; j <= i; j++)
            printf("%c", str[j % n]);
        printf("\n");
    }

    for (i = n; i >= 1; i--) {
        for (j = i; j < n; j++)
            printf(" ");
        for (j = 1; j <= (i * 2) - 1; j++)
            printf("%c", str[j % n]);
        printf("\n");
    }
}

int main() {
    char str[] = " i love cybersecurity";
    printHeart(str);
    return 0;
}
