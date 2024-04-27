/*
 * example2_1.c
 *
 * プログラミングBI 演習例題2-1
 *
 * Copyright (C) 2010-2024, S. Muramatsu
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* 関数プロトタイプ */
void inputVec(double* pVec, int nDims); 
double getNorm(double* pVector, int nDims); 

int main()
{
  /* 変数宣言 */
  int nDims; /* ベクトルの次元 */
  double *pVector; /* ベクトルのポインタ */
  char mode;

  /* ベクトルの次元の読み込み */
  do {
    printf("ベクトルの次元を入力して下さい．(>0): ");
    scanf("%d", &nDims);
  } while( nDims < 1 );

  /* ベクトルのための動的領域確保 */
  pVector = (double*)malloc(sizeof(double)*nDims);

  do {
    /* ベクトルxの要素の読み込み */
    printf("ベクトルx の要素の読み込み\n");
    inputVec(pVector, nDims);

    /* ベクトルの長さ（ノルム）の計算と表示 */
    printf("ベクトルxの長さ（ノルム）: %f\n\n", getNorm(pVector,nDims));

    /* 継続の確認 */
    printf("継続しますか？['y'で継続]: ");
    scanf(" %c", &mode); /* %cの前にスペースを入れる */
    printf("\n");
  } while ( mode=='y' || mode=='Y' );

  /* 領域解放 */
  free(pVector);
    
  return 0;
}

/* ベクトルの要素を問い合わせる関数 */
void inputVec(double* pVector, int nDims)
{
    int iDim;
    for(iDim=0; iDim<nDims; iDim++) {
      printf("%d番目の要素を入力して下さい: ", iDim+1);
      scanf("%lf", &pVector[iDim] );
    }
    printf("\n");
}

/* ベクトルの長さ（ノルム）を計算する関数 */
double getNorm(double* pVector, int nDims)
{

  static int nCalls = 0; /* 呼び出された回数（静的変数）*/
  int iDim;
  double sqrdSum;

  /* 呼出し回数の更新と表示 */
  nCalls++;
  printf("関数 getNorm の呼出し回数: %d\n", nCalls);

  /* ベクトルの内積の計算 */
  sqrdSum=0.0;
  for(iDim=0; iDim<nDims; iDim++)
    sqrdSum += pVector[iDim] * pVector[iDim];

  return sqrt(sqrdSum);
}