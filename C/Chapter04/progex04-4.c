#include <stdio.h>

main()
{
  int i, j;
  int a[2][3] = { {1,2,3}, {4,5,6} };

  for(i=0; i<2; i++) {
    for(j=0; j<3; j++)
      printf("a[%d][%d] = %d \n",i,j,a[i][j]);
  }
  printf("\n");
  for(i=0; i<2; i++) {
    for(j=0; j<3; j++)
      printf("*(a[%d]+%d) = %d \n",i,j,*(a[i]+j));
  }

}
