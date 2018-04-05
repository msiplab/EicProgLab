#include <stdio.h>

typedef union {
  float f;
  int i;
} Number;

int main()
{
  Number n;

  n.f = 7.0f;

  printf("%f\n", n.f);
  printf("%#0x\n", n.i);
}
