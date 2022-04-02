#include <stdio.h>

int main()
{
  double factorial0, factorial1, factorial2;
  int i, n, k;

  scanf("%d%d",&n,&k);	

  factorial0 = 1.0;
  for(i=2; i<=n; i++)
    factorial0 *= (double)i;

  factorial1 = 1.0;
  for(i=2; i<=k; i++)
    factorial1 *= (double)i;

  factorial2 = 1.0;
  for(i=2; i<=n-k; i++)
    factorial2 *= (double)i;
  
  printf("%20.14g\n",
	 factorial0/(factorial1 * factorial2));
	
  return 0;

}
