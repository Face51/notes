#include <stdio.h>

int main() {
    int a, b;   // Variable declaration

    printf("Enter two positive integers: ");
    scanf("%d %d", &a, &b);

    while(a != b) {
        if(a > b)
            a = a - b;
        else
            b = b - a;
    }

    printf("GCD = %d", a);
    return 0;
}
