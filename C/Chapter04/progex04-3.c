#include <stdio.h>
#include <stdlib.h>
char bin[17]; /* 外部変数 */

void dec2bin16(unsigned short);
unsigned short bin2dec16(void);

int main()
{
  unsigned short dec;
  char mode;
  
  /* 入力部 */
  do {
    /* 表示部省略 */
    printf("(1) Decimal to binary\n");
    printf("(2) Binary to decimal\n");
    printf("\t Select Mode: ");
    mode = (char)getchar();
    if ( mode=='q' || mode=='Q' )
      exit(EXIT_SUCCESS);
  } while( mode!='1' && mode!='2' );

  /* 処理および出力部 */
  switch(mode) {
  case '1': /* 10進数→2進数変換 */
    printf("Input decimal value: ");
    scanf("%hu",&dec);
    dec2bin16(dec);
    printf("   Binary value：%s \n", bin);
    break; 
  case '2': /* 2進数→10進数変換 */
    printf("Input binary value in 16 bits: ");
    scanf("%s",bin);			
    dec = bin2dec16();
    printf("   Decimal value：%u \n", dec);
    break;
  default:
    exit(EXIT_FAILURE);
  }
}

/* 10進数→2進数変換 */
void dec2bin16(unsigned short dec) {
  int iDigit;
  unsigned short mask=1u;
  
  for(iDigit=0; iDigit<16; iDigit++) {
    bin[15-iDigit] = (char)((dec&mask) + '0');
    dec = dec>>1;
  }
}

/* 2進数→10進数変換 */
unsigned short bin2dec16(void) {
  int iDigit;
  unsigned short digit=1u, dec=0u;
  
  for(iDigit=0; iDigit<16; iDigit++) {
    if ( bin[15-iDigit] == '1' )
      dec = dec + digit;
    digit = digit<<1;		
  }
  return dec;
}
