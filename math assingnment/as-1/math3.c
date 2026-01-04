#include <stdio.h>

int main() {
    int a, b, temp;   // Declare variables

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    // Swapping using a temporary variable
    temp = a;
    a = b;
    b = temp;

    printf("After swapping: a = %d, b = %d", a, b);
    return 0;
}
