#include <stdio.h>
#include <stdlib.h>
#include <math.h>

main(int argc,char *argv[])
{
  double x = atof(argv[1]);
  printf("%f%c\n", sqrt(fabs(x)),
	 (x<0) ? 'i' : '\0');
}
