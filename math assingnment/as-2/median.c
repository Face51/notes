#include <stdio.h>

// Function Declarations 
void inputArray(float [], int);
void sortArray(float [], int);
float findMedian(float [], int);

int main() {
    int n;
    float arr[100], median;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    // Input array elements
    inputArray(arr, n);

    // Sort the array
    sortArray(arr, n);

    // Calculate median
    median = findMedian(arr, n);

    printf("\nMedian = %.2f\n", median);

    return 0;
}

// Function to input array elements
void inputArray(float arr[], int n) {
    int i;
    printf("Enter %d numbers:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%f", &arr[i]);
    }
}

// Function to sort array in ascending order
void sortArray(float arr[], int n) {
    int i, j;
    float temp;
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

// Function to find median
float findMedian(float arr[], int n) {
    float median;
    if (n % 2 == 0)
        median = (arr[n/2 - 1] + arr[n/2]) / 2.0;
    else
        median = arr[n/2];

    return median;
}
