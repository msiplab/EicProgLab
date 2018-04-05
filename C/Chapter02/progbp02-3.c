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
}
