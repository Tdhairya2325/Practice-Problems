#include <stdio.h>

// Function to calculate x^n using the divide and conquer algorithm
double Exponential(double x, int n) {
    // Base case: x^n where n is 0 is always 1
    if (n == 0) {
        return 1.0;
    } else {
        // Recursively calculate x^(n/2)
        double m = Exponential(x, n / 2);
        
        // Check if n is even or odd
        if (n % 2 == 0) {
            return m * m;  
        } else {
            return m * m * x;  
        }
    }
}

int main() {
    // Example usage
    double x;
    int n;
    printf("Enter Base value:");
    scanf("%.2f",&x);fflush(stdin);
    printf("Enter the Power value:");
    scanf("%d",&n);
    // double result = ;
    
    printf("%.2f^%d = %.2f\n", x, n,Exponential(x,n));
    return 0;
}