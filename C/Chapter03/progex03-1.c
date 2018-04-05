#include <stdio.h>

main()
{
  float a = 0.10f; /* (1.1001100110011001100110 x 2^(-4))_2 */
  float b = 10.0f;  
  double c;
  double d;
 
  c = (double)a * (double)b;
  d = c - 1.0f;

  printf("a = %21.16e\n",a);
  printf("b = %21.16e\n",b);
  printf("c = %21.16e\n",c);
  printf("d = %21.16e\n",d);
}
