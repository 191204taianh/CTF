#include <stdio.h>

int main() {
    int decimal;
    
    // Prompt user for input
    printf("Enter a decimal number: ");
    scanf("%d", &decimal);
    
    // Print the hexadecimal equivalent
    printf("Hexadecimal equivalent: %X\n", decimal);
    
    return 0;
}