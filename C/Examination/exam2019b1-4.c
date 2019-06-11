#include <stdio.h>
#define NROWS 2
#define NCOLS 2

void disp(double[]);
double det(double[][NCOLS]);
void solve(double[],double[][NCOLS],double[]);

int main() {
	
	double A[][NCOLS] = { { 2.0,  1.0 },
		                  { 1.0, -1.0 } };
	double b[] = { 3.0, 6.0 };
	double x[] = { 0.0, 0.0 };
	
	printf("x = ");
	disp(x);
	
	printf("|A| = %6.2f\n",det(A));
	
	solve(x,A,b);
	
	printf("x = ");
	disp(x);
	
	return 0;
}

void disp(double x[]) {
	int iRow;
	
	printf("[\n");
	
	for (iRow=0; iRow<NROWS; iRow++)
		printf("%6.2f\n", x[iRow]);
		
	printf("]\n");
}

double det(double A[][NCOLS]) {
	double d;
	
	d = A[0][0]*A[1][1]-A[0][1]*A[1][0];
	
	return d;
}

void solve(double x[],double A[][NCOLS],double b[]) {
	int iRow;
	double B[NROWS][NCOLS];
	
	for (iRow=0; iRow<NROWS; iRow++) {
		B[iRow][0] = b[iRow];
		B[iRow][1] = A[iRow][1];
	}
	printf("|B0| = %6.2f\n",det(B));
	x[0] = det(B)/det(A);
	
	for (iRow=0; iRow<NROWS; iRow++) {
		B[iRow][0] = A[iRow][0];
		B[iRow][1] = b[iRow];
	}
	printf("|B1| = %6.2f\n",det(B));
	x[1] = det(B)/det(A);
}
