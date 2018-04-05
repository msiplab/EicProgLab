/*
 * example1_2.c
 *
 * プログラミング演習 例題1-2
 *
 * Copyright (C) 2010-2018, S. Muramatsu
 *
 */
#include <stdio.h>
#include <stdlib.h>

#define DELTA 1E-15 /* 誤差の上限 */
#define absdif(x,y) ((x>y) ? (x-y) : (y-x)) /* 差分絶対値 */

/* 平方根を求める関数 */
double mysqrt(double a) {

  	int k = 0; /* 反復回数 */
	double x = 1.0; /* 平方根 */
	double e = absdif(x,a/x); /* 誤差 */

	/* 反復計算 */
	printf(" %21.16g（反復回数 %d 回）\n", x, k);
	while(e >= DELTA && k < 1000) {
		k++;
		x = ( x + a/x )/2.0; /* 値の更新 */
		e = absdif( x, a/x ); /* 誤差 */
		printf(" %21.16g（反復回数 %d 回）\n", x, k);
	}
	x = ( x + a/x )/2.0; /* 値の更新 */

	return x;
}

/* メイン関数 */
int main()
{
	/* 変数宣言 */
	double a; /* 入力値 */
	double x; /* 平方根 */

	/* 平方根を求める値の読み込み */
	printf("正の実数値を入力して下さい: ");
	scanf("%lf",&a);

	/* 入力データの確認 */
	if ( !(a > 0) ) {
		printf("負の値は扱えません。終了します。\n");
		exit(EXIT_SUCCESS);
	}

	/* 平方根の計算 */
	x = mysqrt(a);

	/* 平方根の表示 */
	printf("%f の平方根:\n", a);
	printf(" %21.16g \n", x);
}
