#include <stdio.h>
#include <stdlib.h>

main()
{
  int i;
  int n;        /* 数列の要素数 */
  char str[16]; /* 入力用文字列 */
  double *a;    /* 数列用ポインタ */
  double mean = 0.0; /* 平均 */
  double var  = 0.0; /* 分散 */
  
  printf("要素数を入力して下さい: ", n);
  scanf("%d",&n);
  a = (double*)malloc(sizeof(double)*n);

  printf("数値を入力して下さい\n", n);
  for (i=0; i<n; i++) {
    printf("a[%2d] : ", i);
    scanf("%s",str);
    a[i] = atof(str);
    mean += a[i]; 
  } 

  mean /= n; /* 平均 */
  printf("\t 平均: %g\n", mean);

  for (i=0; i<n; i++)
    var += (a[i]-mean)*(a[i]-mean);

  var /= n; /* 分散 */
  printf("\t 分散: %g\n", var);

  free(a);
}
