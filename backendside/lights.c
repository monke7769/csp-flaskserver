// Mini project by: Shuban Pal
// Showcase section: The backend

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string.h>

const int BITS_IN_BYTE = 8; // Constant integer for bits in a byte

void print_bulb(int bit); // Define function print bulb

int main(void) // Function main
{
    char message[100]; // Prompt for message
    scanf("%[^\n]%*c", message);
    for (int i = 0; i < strlen(message); i++) // Parsing through input
    {
        int decimal = (int) message[i]; // Define ASCII version of parsed character
        if (decimal == 0) // If decimal version is 0
        {
            print_bulb(0); // Input 0 into print_bulb function
        }
        else if (decimal != 0) // If it is not 0
        {
            int bits[BITS_IN_BYTE] = {0}; // Declare an array of size 8 (to store all our bits)
            for (int j = BITS_IN_BYTE - 1; j >= 0; j--) // Parse bits from 7, decrease it by 1 each time
            {
                bits[j] = decimal % 2; // Position in array is remainder of decimal version of ASCII (1 or 0)
                decimal = floor(decimal / 2); // Decimal is changed to the floor of the decimal / 2
            }
            for (int j = 0; j < BITS_IN_BYTE; j++) // For every bit in array bits
            {
                print_bulb(bits[j]); // Print bulb for every bit
            }

            printf("\n"); // Print new line for new set of 8 bulbs
        }
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
