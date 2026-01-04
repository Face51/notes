#include <stdio.h>

int main() {
    int a[10], b[10];
    int n1, n2, i, j;   // Variable declaration

    printf("Enter number of elements in set A: ");
    scanf("%d", &n1);
    printf("Enter elements of set A: ");
    for(i = 0; i < n1; i++)
        scanf("%d", &a[i]);

    printf("Enter number of elements in set B: ");
    scanf("%d", &n2);
    printf("Enter elements of set B: ");
    for(i = 0; i < n2; i++)
        scanf("%d", &b[i]);

    printf("Intersection: ");
    for(i = 0; i < n1; i++) {
        for(j = 0; j < n2; j++) {
            if(a[i] == b[j]) {
                printf("%d ", a[i]);
                break;
            }
        }
    }

    return 0;
}
