#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
  double real;
  double imag;
} Complex;

void display(Complex);
Complex prodOf(Complex,Complex);

int main(int argc, char *argv[])
{
  Complex z0 = { atof(argv[1]), atof(argv[2]) };
  Complex z1 = { atof(argv[3]), atof(argv[4]) };

  /* 二つの複素数の表示 */
  printf("z0 = ");
  display(z0);
  printf("z1 = ");
  display(z1);
  /* 二つの複素数の積 */
  printf("z0 * z1 = ");
  display(prodOf(z0,z1));
  
  return 0;
}

void display(Complex z)
{
  char s = ( z.imag < 0 ) ? '-' : '+';

  printf("%f %c i%f\n", z.real, s, fabs(z.imag));
}

Complex prodOf(Complex z0, Complex z1)
{
  Complex z2;

  z2.real = z0.real * z1.real - z0.imag * z1.imag;
  z2.imag = z0.real * z1.imag + z0.imag * z1.real;

  return z2;
}
