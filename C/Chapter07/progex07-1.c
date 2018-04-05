#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void display(double[]);

main(int argc, char *argv[])
{
  double z[2];
  z[0] = atof(argv[1]);
  z[1] = atof(argv[2]);
  display(z);
}

void display(double z[])
{
   char s = ( z[1] < 0 ) ? '-' : '+';
   printf("%f %c i%f\n", z[0], s, fabs(z[1]));
}
