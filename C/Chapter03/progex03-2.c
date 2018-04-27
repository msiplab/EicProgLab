#include <stdio.h>

int main()
{
  float a = 1234567.0f;
  float b = 7654321.0f;
  float c;
  double d;
 
  c = a * b;
  d = (double)a * (double)b;

  printf("a = %10.7e\n",a);
  printf("b = %10.7e\n",b);
  printf("c = %18.15e\n",c);
  printf("d = %18.15e\n",d);
  
  return 0;
}
