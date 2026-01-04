#include <stdio.h>

int main() {
    int a[10], b[10], u[20];
    int n1, n2, i, j, k, found;   // Variable declaration

    k = 0;

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

    for(i = 0; i < n1; i++)
        u[k++] = a[i];

    for(i = 0; i < n2; i++) {
        found = 0;
        for(j = 0; j < n1; j++) {
            if(b[i] == a[j]) {
                found = 1;
                break;
            }
        }
        if(found == 0)
            u[k++] = b[i];
    }

    printf("Union: ");
    for(i = 0; i < k; i++)
        printf("%d ", u[i]);

    return 0;
}
