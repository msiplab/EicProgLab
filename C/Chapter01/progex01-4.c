#include <stdio.h>

#define DELTA 1E-15 /* 誤差の上限 */
#define absdif(x,y) ((x>y) ? (x-y) : (y-x)) /* 差分絶対値 */

int main()
{
	/* 変数宣言 */
	double a; /* 平方根を求める値 */
	double x = 1.0; /* 平方根の近似値 */
	double e; /* 誤差 */
	int k = 0; /* 反復回数 */	
	
	/* 平方根を求める値の読み込み */
	scanf("%lf",&a);
	
	/* 反復計算 */
	e = absdif(x, a/x); /* 誤差 */
	while(e >= DELTA) {
		k++;
		x = ( x + a / x ) / 2.0; /* 値の更新 */
		e = absdif(x, a/x);      /* 誤差 */
	}

	/* 平方根の表示 */
	printf("%f の平方根:\n",a);
	printf(" %21.16g（反復回数 %d 回）\n", x, k);	
}
