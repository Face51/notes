#include <stdio.h>

int main() {
    int a, b, x, y, gcd, lcm, temp;   // Variable declaration

    printf("Enter two positive integers: ");
    scanf("%d %d", &a, &b);

    x = a;
    y = b;

    /* Finding GCD using Euclid’s Algorithm */
    while (y != 0)
    {
        temp = y;        // store y
        y = x % y;       // remainder
        x = temp;        // shift value
    }

    gcd = x;
    lcm = (a * b) / gcd;

    printf("GCD = %d\n", gcd);
    printf("LCM = %d", lcm);

    return 0;
}
