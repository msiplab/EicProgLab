#include <stdio.h>

int main()
{
  float a = 6144.0f;
  float b = 0.007080078125f;
  float c;
  double d;
 
  c = a + b;
  d = (double)a + (double)b;

  printf("a = %21.18e\n",a);
  printf("b = %21.18e\n",b);
  printf("c = %21.18e\n",c);
  printf("d = %21.18e\n",d);
  
  return 0;
}
