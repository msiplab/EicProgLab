#include <stdio.h>

int main()
{
  
  int i;
  int a[10]={1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int *p;
  int b;

  for(i=0; i<10; i++) {
    p = (&a[0]+i); /* &a[0] は *a と同じ */
    b = *(&a[0]+i);
    printf("(&a[0]+%d) = %8p: *(&a[0]+%d)"
	   " = %2d\n",i,p,i,b);
  }
	
  return 0;
}
