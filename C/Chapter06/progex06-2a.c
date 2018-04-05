#include <stdio.h>
#include <stdlib.h>
/*
 * 端末上でコマンド引数を渡しながら実行
 */

int main(int argc,char *argv[])
{
  /* 変数宣言 */
  FILE *pfin, *pfout;
  double matrix[2][2];
  int i;

  /* 入力ファイル */
  pfin = fopen(argv[1], "r");
  if ( pfin == NULL ) {
    printf("%s: オープンに失敗しました．\n",argv[1]);
    exit(EXIT_FAILURE);
  } 

  /* 出力ファイル */
  pfout = fopen(argv[2], "w");
  if ( pfout == NULL ) {
    printf("%s: オープンに失敗しました．\n", argv[2]);
    exit(EXIT_FAILURE);
  } 

/* 入力 */
  for (i=0; i<2; i++) 
     fscanf(pfin,"%lf, %lf", 
                &matrix[i][0], &matrix[i][1]);

  /* 出力 */
  for (i=0; i<2; i++) 
      fprintf(pfout,"%f, %f\n", 
	matrix[0][i], matrix[1][i]);

  /* ファイルのクローズ */
  fclose(pfin);
  fclose(pfout);
}
