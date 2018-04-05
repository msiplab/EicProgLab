#include <stdio.h>

double factorial(int k) {
	double y = 1.0;
	int i;
	for (i=2; i<=k; i++)
		y *= (double)i;
	return y;
}

main()
{
  int n, k;

  scanf("%d%d",&n,&k);	

  printf("%20.14g\n",
	 factorial(n)/(factorial(k) * factorial(n-k)));

}
