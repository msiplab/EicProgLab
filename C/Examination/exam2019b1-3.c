#include <stdio.h>

double f(double);
double g(double);

int main() {
	double x;
	int iter;
	
	for (iter=1; iter<5; iter++) {
		x = (double)iter;
		printf("%d:\n", iter);
		printf(" f = %6.2f\n",f(x));
		printf(" g = %6.2f\n",g(x));
	}

	return 0;
}

double f(double x){
	static unsigned int count=1;
	static double mu=0.0;
	
	mu += (x-mu)/(double)count;
	count++;

	return mu;
}


double g(double x){
	int unsigned count=1;
	double mu=0.0;
	
	mu += (x-mu)/(double)count;
	count++;
	
	return mu;	
}
