#include <stdio.h>

int main() {
    int base, exp, i, result;   // Variable declaration

    result = 1;                // Initialization

    printf("Enter base and exponent: ");
    scanf("%d %d", &base, &exp);

    for(i = 1; i <= exp; i++) {
        result = result * base;
    }

    printf("Result = %d", result);
    return 0;
}
