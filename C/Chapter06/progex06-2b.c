#include <stdio.h>
#include <stdlib.h>

int main(int argc,char *argv[])
{
  /* 変数宣言 */
  double matrix[2][2];
  int i;

  /* 標準入力 */
  for (i=0; i<2; i++) 
     fscanf(stdin,"%lf, %lf", 
                &matrix[i][0], &matrix[i][1]);

  /* 標準出力 */
  for (i=0; i<2; i++) 
      fprintf(stdout,"%f, %f\n", 
	matrix[0][i], matrix[1][i]);

 /* 標準エラー */
      fprintf(stderr, "終了\n");
	
  return 0;
}
