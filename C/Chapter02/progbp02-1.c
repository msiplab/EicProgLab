/* 補足説明    
 * 
 * GCC 8 では、符号付き整数の計算過程におけるオーバーフロー（wrapping)の誤りが
 * 回避されています。
 * 
 * オーバーフローを再現するためには以下のようにコンパイルしてください。
 * 
 * $ gcc -fwrapv -fwrapv-pointer progbp02-1.c 
 * 
 * オーバーフローをコンパイル時にチェックするには以下のようにコンパイルしてください。
 * 
 * $ gcc -fsanitize=signed-integer-overflow progbp02-3.c
 * 
 * 【参考サイト】
 *  
 *  URL: https://gcc.gnu.org/gcc-8/changes.html
 */
#include <stdio.h>

int main()
{
  int i= 2000000000;
  signed int si = 2000000000;
  unsigned int ui = 2000000000u;

  printf("int(d): %d \n", (i+i)/2+i ); 
  printf("int(u): %u \n", (i+i)/2+i );
  printf("signed int(d): %d \n", (si+si)/2+si );
  printf("signed int(u): %u \n", (si+si)/2+si );
  printf("unsigned int(d): %d \n", (ui+ui)/2+ui );
  printf("unsigned int(u): %u \n", (ui+ui)/2+ui );
  
  return 0;
}
