#include <stdio.h>
#include <stdlib.h>
#define NITERS 5

double f(double,double);

int main(int argc, char *argv[]) {
	double x, y, h; 
	double xnxt, ynxt;
	int count = 1;
	
	x = atof(argv[1]);
	y = atof(argv[2]);
	h = atof(argv[3]);
	
	while (count <= NITERS) {
		printf(" x = %6.2f, y = %8.4f\n",x, y);
		xnxt = x + h;
		ynxt = y + h*f(x,y);
		x = xnxt;
		y = ynxt;
		count++;
	}
	
	return 0;
}

double f(double x, double y) {
	return 1.0 - y;
}
