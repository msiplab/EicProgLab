#include <stdio.h>
#include <stdlib.h>

void display(double[], int);
double sqrdnorm(double*, int);

main(int argc, char *argv[])
{
  double vector[] 
	= { atof(argv[1]), atof(argv[2]) };
  int nElements = 2;

  display(vector, nElements);
  printf("\t norm^2 = %f", 
	sqrdnorm(&vector[0], nElements));
}

void display( double v[] , int nElements) {

  int iElement;

  for (iElement=0; iElement<nElements; iElement++)
    printf("%f\n",v[iElement]);
}

double sqrdnorm( double *v , int nElements) {

  int iElement;
  double sn = 0.0;

  for (iElement=0; iElement<nElements; iElement++)
    sn += v[iElement] * v[iElement];

  return sn;
}
