#include <stdio.h>
#include <math.h>

int main() {
    double m, n;

    // Input values for m and n
    printf("Enter value for m: ");
    scanf("%lf", &m);
    
    printf("Enter value for n: ");
    scanf("%lf", &n);

    // Points: P1(m, -n) and P2(-m, n)
    double x1 = m,  y1 = -n;
    double x2 = -m, y2 = n;

    // Distance formula calculation
    double dx = x2 - x1; // -2m
    double dy = y2 - y1; // 2n
    
    double distance = sqrt(dx * dx + dy * dy);

    // Output the result
    printf("\nPoint 1: (%.2lf, %.2lf)\n", x1, y1);
    printf("Point 2: (%.2lf, %.2lf)\n", x2, y2);
    printf("Calculated Distance: %.4lf\n", distance);

    return 0;
}
