#include <stdio.h>
#include <stdlib.h>

main()
{
  int iDigit;
  unsigned short mask = 1u; 
  unsigned short dec;

  printf("65535までの正の整数を入力して下さい：");
  scanf("%hu",&dec);
  printf("\n\t2進数の値は ");
  for (iDigit=15; iDigit>=0; iDigit--) {
    putchar( (char)((dec>>iDigit)&mask) + '0' );
  }
  printf(" です。\n");
}
