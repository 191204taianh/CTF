#include <stdio.h>
#include <stdlib.h>

int main() {
    char hex[20];
    long decimal;
    
    // Prompt user for input
    printf("Enter a hexadecimal number: ");
    scanf("%s", hex);
    
    // Convert hex to decimal
    decimal = strtol(hex, NULL, 16);
    
    // Print the result
    printf("Decimal equivalent: %ld\n", decimal);
    
    return 0;
}
