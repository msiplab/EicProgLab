#include <stdio.h>
#include <stdlib.h>

int main()
{
    int iDigit;
    char c;
    unsigned short digit = (1u)<<15; 
    unsigned short dec = 0u;

    printf("16ビットの2進数を入力して下さい：");
    for (iDigit=15; iDigit>=0; iDigit--) {

        if ( (c = getchar()) == '1' )
              dec += digit;
        else if ( c != '0' ) {
              printf("0, 1 以外の値が入力されました。\n");
              exit(EXIT_SUCCESS);
        }
        digit = digit>>1;

    }
    printf("\n\t10進数の値は %u です。\n", dec);
}
