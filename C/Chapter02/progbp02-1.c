#include <stdio.h>

int main()
{
  char c='\xFF'; /* 11111111 */
  signed char sc='\xFF'; /* 11111111 */
  unsigned char uc='\xFF'; /* 11111111 */

  printf("char: %d\n",  c );
  printf("signed char: %d\n",  sc );
  printf("unsigned char: %d\n", uc );
}
