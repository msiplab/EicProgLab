/*
 * example2_1.c
 *
 * プログラミングBI 演習例題2-1
 *
 * Copyright (C) 2020-2022, S. Muramatsu
 *
 */
#include <stdio.h>
#include <stdlib.h>

/* 関数プロトタイプ */
void inputVec(double* pVec, int nDIms); 
double getInnerProd(double* pVecX, double* pVecY, int nDims); 

int main()
{
  /* 変数宣言 */
  int nDims; /* ベクトルの次元 */
  double *pVecX, *pVecY; /* ベクトルのポインタ */
  char mode;

  /* ベクトルの次元の読み込み */
  do {
    printf("ベクトルの次元を入力して下さい．(>0): ");
    scanf("%d", &nDims);
  } while( nDims < 1 );

  /* ベクトルのための動的領域確保 */
  pVecX = (double*)malloc(sizeof(double)*nDims);
  pVecY = (double*)malloc(sizeof(double)*nDims);

  do {
    /* ベクトルxの要素の読み込み */
    printf("ベクトルx の要素の読み込み\n");
    inputVec(pVecX, nDims);

    /* ベクトルyの要素の読み込み */
    printf("ベクトルy の要素の読み込み\n");
    inputVec(pVecY, nDims);

    /* ベクトルの内積の計算と表示 */
    printf("ベクトルxとyの内積: %f\n\n", getInnerProd(pVecX,pVecY,nDims));

    /* 継続の確認 */
    printf("継続しますか？['y'で継続]: ");
    scanf(" %c", &mode); /* %cの前にスペースを入れる */
    printf("\n");
  } while ( mode=='y' || mode=='Y' );

  /* 領域解放 */
  free(pVecX);
  free(pVecY);  
  
  return 0;
}

/* ベクトルの要素を問い合わせる関数 */
void inputVec(double* pVec, int nDims)
{
    int iDim;
    for(iDim=0; iDim<nDims; iDim++) {
      printf("%d番目の要素を入力して下さい: ", iDim+1);
      scanf("%lf", &pVec[iDim] );
    }
    printf("\n");
}

/* ベクトルの内積を計算する関数 */
double getInnerProd(double* pVecX, double* pVecY, int nDims)
{

  static int nCalls = 0; /* 呼び出された回数（静的変数）*/
  int iDim;
  double innerProd;

  /* 呼出し回数の更新と表示 */
  nCalls++;
  printf("関数 getInnerProd の呼出し回数: %d\n", nCalls);

  /* ベクトルの内積の計算 */
  innerProd=0.0;
  for(iDim=0; iDim<nDims; iDim++)
    innerProd += pVecX[iDim] * pVecY[iDim];

  return innerProd;
}