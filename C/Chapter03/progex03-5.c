#include <stdio.h>

main()
{
  int n = 4;
  int d = 2;
  double a;

  a = n / d;
  printf("%d / %d = %8.4f\n",n,d,a);

  a = n / ( d + 1 );
  printf("%d / ( %d + 1 ) = %8.4f\n",n,d,a);

  a = n / (double)( d + 1 );
  printf("%d / (double)( %d + 1 )  = %8.4f\n",n,d,a);

  a = n / ( d + 1.0 );
  printf("%d / ( %d + 1.0 ) = %8.4f\n",n,d,a);

}
