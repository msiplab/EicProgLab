#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
  double real;
  double imag;
} Complex;

void display(Complex);

main(int argc, char *argv[])
{
  Complex z;

  z.real = atof(argv[1]);
  z.imag = atof(argv[2]);
  display(z);
}

void display(Complex z)
{
  char s = ( z.imag < 0 ) ? '-' : '+';

  printf("%f %c i%f\n", z.real, s, fabs(z.imag));
}
