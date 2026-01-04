#include <stdio.h>

int main() {
    int a, b, temp;   // Variable declaration

    printf("Enter two positive integers: ");
    scanf("%d %d", &a, &b);

    /* Finding GCD using Euclidean algorithm */
    while (b != 0)
    {
        temp = b;     
        b = a % b;    
        a = temp;     
    }

    printf("GCD = %d", a);
    return 0;
}