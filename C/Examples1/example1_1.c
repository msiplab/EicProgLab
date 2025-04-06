/*
 * example1_1.c
 *
 * プログラミングBI 演習例題1-1
 *
 * Copyright (C) 2007-2025, S. Muramatsu
 *
 */
#include <stdio.h>

int main()
{
	/* 変数宣言 */
	double x; /* 独立変数 */
	double y; /* 従属変数 (関数の近似値) */
	int n; /* 近似次数 */

	/* 途中の計算に必要な変数の宣言 */
	int i; /* 繰り返し変数の宣言 */
	double f; /* 階乗値 */
	double p; /* x の累乗値 */

	/* データの読み込み(倍精度, 整数) */
	scanf("%lf%d",&x,&n);

	/* 近似値の初期化 */
	y = 1.0;
	f = 1.0;
	p = 1.0;
	for (i=1; i<=n; i++) {
		f = f * (double)i; /* f *= (double)i; とも書ける */
		p = p * x; /* p *= x; とも書ける */
		y = y + p / f; /* y += p / f; とも書ける */
	}

	/* e^x の近似値の表示 */
	printf("マクローリン展開による次数 %d までの e^(%g) の近似値\n"
		"    =%21.16g\n", n, x, y);
	
	return 0;
}
