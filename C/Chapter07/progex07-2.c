#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
  double real;
  double imag;
} Complex;

main(int argc, char *argv[])
{
  Complex z;
  char s;
  z.real = atof(argv[1]);
  z.imag = atof(argv[2]);

  s = ( z.imag < 0 ) ? '-' : '+';
  printf("%f %c i%f\n", z.real, s, fabs(z.imag));
}
