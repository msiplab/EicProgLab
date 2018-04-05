#include <stdio.h>

int main()
{
  char a = 100;
  char b = 3;
  int c;
  double d;

  c = a * b;
  printf("a * b = %3d\n", c);

  c = a / b;
  printf("a / b = %3d\n", c);

  d = a / b;
  printf("a / b = %10.6f\n", d);

  d = (double)a / b;
  printf("a / b = %10.6f\n", d);
}
