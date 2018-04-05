/*
 * example2_1.c
 *
 * プログラミング演習 例題2-1
 *
 * Copyright (C) 2010-2017, S. Muramatsu
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double getNorm(double* pVector, int nElements); /* 関数プロトタイプ */

int main()
{

  /* 変数宣言 */
  int nElements; /* ベクトルの次元 */
  double *pVector; /* ベクトルのポインタ */
  int iElement;
  char mode;

  /* ベクトルの次元の読み込み */
  do {
    printf("ベクトルの次元を入力して下さい．(>0): ");
    scanf("%d", &nElements);
  } while( nElements < 1 );

  /* ベクトルのための動的領域確保 */
  pVector = (double*)malloc(sizeof(double)*nElements);

  do {
    /* ベクトルの要素の読み込み */
    for(iElement=0; iElement<nElements; iElement++) {
      printf("%d番目の要素を入力して下さい: ", iElement+1);
      scanf("%lf", &pVector[iElement] );
    }
    printf("\n");

    /* ベクトルの長さの計算 */
    printf("ベクトルの長さ: %f\n\n", getNorm(pVector,nElements));

    /* 継続の確認 */
    printf("継続しますか？['y'で継続]: ");
    scanf(" %c", &mode);
    printf("\n");

  } while ( mode=='y' || mode=='Y' );

  /* 領域解放 */
  free(pVector);
}

/* ベクトルの長さを計算する関数 */
double getNorm(double* pVector, int nElements)
{

  static int nCalls = 0; /* 呼び出された回数（静的変数）*/
  int iElement;
  double sqrdsum;

  /* 呼出し回数の更新と表示 */
  nCalls++;
  printf("関数 getNorm の呼出し回数: %d\n", nCalls);

  /* ベクトルの長さの計算 */
  sqrdsum=0.0;
  for(iElement=0; iElement<nElements; iElement++)
    sqrdsum += pVector[iElement] * pVector[iElement];

  return sqrt(sqrdsum);

}
