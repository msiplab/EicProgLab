#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
  double real;
  double imag;
} Complex;

void display(Complex*);

int main(int argc, char *argv[])
{
  Complex z;

  z.real = atof(argv[1]);
  z.imag = atof(argv[2]);
  display(&z);
  
  return 0;
}

void display(Complex* pz)
{
  char s = ( pz->imag < 0 ) ? '-' : '+';

  printf("%f %c i%f\n", pz->real, s, fabs(pz->imag));
}
