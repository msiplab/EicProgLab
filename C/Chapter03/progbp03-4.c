#include <stdio.h>

int main()
{
  
  int i;
  int a[10]={1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int acc = 0;

  for (i=0;i<10;i++)
    acc += a[i]; 

  printf("総和 : %d\n",acc);

}
