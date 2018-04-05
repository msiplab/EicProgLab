#include <stdio.h>
#include <stdlib.h>
#include <math.h>
/*
 * コンパイルは端末上で
 *
 * $ gcc -Wall progex06-3.c -lm -o progex06-3
 * 
 */

int main(int argc,char *argv[])
{
  double x = atof(argv[1]);
  printf("%f%c\n", sqrt(fabs(x)),
	 (x<0) ? 'i' : '\0');
}
