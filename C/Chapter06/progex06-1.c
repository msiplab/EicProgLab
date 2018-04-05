#include <stdio.h>
#define NCOLS 2

void display( double[][NCOLS] , int);
double getElement( double[][NCOLS] , int, int);

int main()
{
  double matrix[][NCOLS] = {{1.0, 2.0},
			    {3.0, 4.0}};
  int nRows = 2;
  int iRow, iCol;
  display( matrix , nRows);
  iRow = 0;
  iCol = 1;
  printf("\t matrix(%d,%d) = %f", iRow, iCol,
	 getElement(&matrix[0], iRow, iCol));
}

void display(double m[][NCOLS],
	     int nRows) {
  int iRow, iCol;

  for (iRow=0; iRow<nRows; iRow++){
    for (iCol=0; iCol<NCOLS; iCol++){
      printf("%f ", m[iRow][iCol]);
    }
    printf("\n");
  }
}

double getElement( double (*m)[NCOLS] ,
		   int iRow, int iCol) {

  return m[iRow][iCol];
}
