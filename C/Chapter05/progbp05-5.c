#include <stdio.h>

void display( double[] , int);
void accvec(double*,double*,int);

int main() {
 double a[] = { 1.0, 2.0 };
 double v[] = { 3.0, 4.0 };

 int nElements = 2;
  
  accvec( a, v, nElements);
  printf("a = \n");
  display( a, nElements);
  printf("v = \n");
  display( v, nElements);
}

void display(double v[] , int nElements) {

  int iElement;

  for (iElement=0; iElement<nElements; iElement++)
    printf("%f\n",v[iElement]);
}

void accvec(double *a , double *v, int nElements) {

  int iElement;

  for (iElement=0; iElement<nElements; iElement++)
    a[iElement] += v[iElement];

}
